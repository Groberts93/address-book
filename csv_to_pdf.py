import os 
import os.path as op
import pandas as pd




def main(basepath):

    datapath = op.join(basepath, 'data')

    files = os.listdir(datapath)
    filepath = op.join(datapath, files[0])
    address_table = pd.read_csv(filepath)

    print(address_table)


if __name__ == '__main__':
    basepath = op.dirname(__file__)
    main(basepath)