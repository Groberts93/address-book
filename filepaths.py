import os
import os.path as op

class Filepaths:

    def __init__(self, base: str):
        self._base = base
        
        self.csv = op.join(base, 'csv')
        self.pdf = op.join(base, 'pdf')
