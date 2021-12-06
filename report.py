import reportlab as rlab
import reportlab.lib.styles as rstl
import reportlab.platypus as plat
import reportlab.rl_config as rcfg

from reportlab.lib.units import inch
from dataclasses import dataclass

from filepaths import Filepaths
import os.path as op

import pandas as pd
import re
import numpy as np


@dataclass
class ReportSpec:

    page_width: float = rcfg.defaultPageSize[0]
    page_height: float = rcfg.defaultPageSize[1]
    font_size: int = 15
    title: str = "Report Title"
    page_info: str = "Report Info"
    font: str = "Helvetica-Bold"
    top_margin: float = 108
    styles = rstl.getSampleStyleSheet()
    filename = "output"


class Report:
    def __init__(self, spec: ReportSpec, paths: Filepaths, data: pd.DataFrame):

        self._spec = spec
        self._paths = paths
        self._data = data

    def _first_page(self, canvas, doc):
        """Describe first page of document.  This method gets
        passed to reportlab method 

        Parameters
        ----------
        canvas : Reportlab canvas
            
        doc : [type]
            [description]
        """
        canvas.saveState()
        canvas.setFont(self._spec.font, self._spec.font_size)
        canvas.drawCentredString(
            self._spec.page_width / 2.0,
            self._spec.page_height - self._spec.top_margin,
            self._spec.title,
        )

        canvas.setFont(self._spec.font, self._spec.font_size)
        canvas.drawString(inch, 0.75 * inch, f"{self._spec.page_info}")
        canvas.restoreState()

    def _later_pages(self, canvas, doc):
        """Description of subsequent pages for reportlab

        Parameters
        ----------
        canvas : [type]
            [description]
        doc : [type]
            [description]
        """
        canvas.saveState()
        canvas.setFont(self._spec.font, 9)
        canvas.drawString(
            # inch, 0.75 * inch, "Page %d %s" % (doc.page, self._spec.page_info)
            inch, 0.75 * inch, f"Page {doc.page}"
        )
        canvas.restoreState()

    def generate(self):
        doc = plat.SimpleDocTemplate(
            op.join(self._paths.pdf, f"{self._spec.filename}.pdf")
        )

        Story = [plat.Spacer(1, 0.5 * inch)]
        style = self._spec.styles["BodyText"]

        cards = dataframe_to_cards(self._data)

        for card in cards:

            text = card.generate()
            p = plat.Paragraph(text, style)
            Story.append(p)
            Story.append(plat.Spacer(1, 0.2 * inch))

        doc.build(Story, onFirstPage=self._first_page, onLaterPages=self._later_pages)


@dataclass
class CardData:

    name: str
    house: str
    line1: str
    line2: str
    town: str
    code: str
    region: str


class Card:
    def __init__(self, card_data: CardData):

        self._data = card_data

    def generate(self) -> str:

        lines = []

        lines.append(self._data.name)

        if re.findall("\d+", self._data.house):
            house_road = f"{self._data.house} {self._data.line1}"
            lines.append(house_road)
        else:
            lines.append(self._data.house)
            lines.append(self._data.line1)

        if not pd.isna(self._data.line2):
            lines.append(self._data.line2)

        lines.append(self._data.town)
        lines.append(self._data.code)
        lines.append(self._data.region)

        return "<br/>".join(lines)


def series_to_carddata(df: pd.Series):

    return CardData(
        name=df["Name"],
        house=df["House"],
        line1=df["Address Line 1"],
        line2=df["Address Line 2"],
        town=df["Town/City"],
        code=df["Postcode"],
        region=df["Region"],
    )


def dataframe_to_cards(df: pd.DataFrame) -> list[Card]:

    cards: list[Card] = []

    for irr, record in df.iterrows():
        card_data = series_to_carddata(record)
        cards.append(Card(card_data))

    return cards


def card_to_paragraph(card: Card) -> plat.Paragraph:

    para = plat.Paragraph(card.generate())
    return para
