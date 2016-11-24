import time
import csv
import InputData


# def exeTime(func):
#     def newFunc(*args, **args2):
#         t0 = time.time()
#         print "@%s, {%s} start" % (time.strftime("%X", time.localtime()), func.__name__)
#         back = func(*args, **args2)
#         print "@%s, {%s} end" % (time.strftime("%X", time.localtime()), func.__name__)
#         print "@%.3fs taken for {%s}" % (time.time() - t0, func.__name__)
#         return back
#
#     return newFunc
#
#
# @exeTime
# def foo():
#     for i in xrange(10000000):
#         pass
#
#     foo()


# def ReadCsv(file):
#     OpneFile = open(file)
#     CsvReader = csv.reader(OpneFile)
#     # num = 0
#     # for row in CsvReader:
#     #     num += 1
#     # print num
#     spamreader = csv.reader(OpneFile)
#     for row in spamreader:
#         for col in row:
#             print col, '\n'

file = 'www1.csv'
# ReadCsv(file)
OffsetRow = 1
OffsetCol = 1
ReadMatrix = InputData.InputMatrix()
array = ReadMatrix.ReadCsv(file, OffsetRow, OffsetCol)
print array



