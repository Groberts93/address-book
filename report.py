import reportlab as rlab
import reportlab.platypus as plat
import reportlab.rl_config as rcfg

from reportlab.lib.units import inch
from dataclasses import dataclass

@dataclass
class ReportSpec:

    page_width: float =  rcfg.defaultPageSize[0]
    page_height: float =  rcfg.defaultPageSize[1]
    font_size: int = 15

class Report:

    def __init__(self, spec: ReportSpec):

        self._specs = spec
