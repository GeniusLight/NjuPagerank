# -*- coding:utf-8 -*-
import pagerank
import OutputData
from numpy import *
import InputData


matrixfile = 'gather.csv'
OffsetRow = 1
OffsetCol = 1
pi = pagerank.pagerankmain(matrixfile, OffsetRow, OffsetCol) #计算网站的pagerank值

urlfile = 'id_url.csv'
InputUrl = InputData.InputUrl()
list = InputUrl.ReadUrl(urlfile)

n1 = len(list)
n2 = pi.shape[1]
if n1 == n2:
    for i in range(n2):
        data = {"_id": i, "url": list[i], "pr": pi[0][i]}
        outputer = OutputData.Outputpi()
        outputer.OutputMongo(data)
