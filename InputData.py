import xlrd
from numpy import *
from numpy.linalg import *


class InputMatrix(object):
    def ReadExcle(self, file, OffsetRow, OffsetCol):
        workbook = xlrd.open_workbook(file)
        table1 = workbook.sheets()[1]
        nrows = table1.nrows
        ncols = table1.ncols
        array = zeros((nrows - OffsetRow, ncols - OffsetCol), dtype=float)
        for i in range(OffsetRow, nrows):
            for j in range(2, ncols):
                if table1.cell(i, j).value is None:
                    pass
                elif table1.cell(i, j).value == 1:
                    array[i - 2, j - 2] = 1
        return array
