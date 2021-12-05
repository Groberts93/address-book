import os
import os.path as op
import pandas as pd
from report import ReportSpec, Report 
from filepaths import Filepaths

def main(basepath):

    paths = Filepaths(basepath)

    files = os.listdir(paths.csv)
    filepath = op.join(paths.csv, files[0])

    address_table = pd.read_csv(filepath)

    default_report_spec = ReportSpec()
    default_report_spec.filename = 'christmas'
    default_report = Report(default_report_spec, paths)

    default_report.generate()

if __name__ == "__main__":
    basepath = op.dirname(__file__)
    main(basepath)
