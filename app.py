import os
import os.path as op
import pandas as pd
from report import ReportSpec, Report
from filepaths import Filepaths
import names 

def main(basepath):

    paths = Filepaths(basepath)

    files = os.listdir(paths.csv)
    filepath = op.join(paths.csv, files[0])

    address_table = pd.read_csv(filepath)
    raw_names = address_table['Name'].to_list()
    family_names = list(map(names.extract_family_name, raw_names))

    address_table['Family'] = family_names
    address_table.sort_values('Family', inplace=True)

    default_report_spec = ReportSpec(page_info="Christmas list", title="Christmas list")
    default_report_spec.filename = "christmas"
    default_report = Report(default_report_spec, paths, address_table)

    default_report.generate()


if __name__ == "__main__":
    basepath = op.dirname(__file__)
    main(basepath)
