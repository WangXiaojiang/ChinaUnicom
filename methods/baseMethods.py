#coding=utf-8
from methods.LTEConnectionRateLowCellSearch import *


def connectionLowSearch(x, date, cell, rrcReqSucNum, rrcReqNum, e_rabReqSucNum, e_rabReqNum):
    data = dict()
    if x[rrcReqNum] >= 1 and x[e_rabReqNum] >= 1:
        connectionRate = 100 * x[rrcReqSucNum] / x[rrcReqNum] * x[e_rabReqSucNum] / x[e_rabReqNum]
    else:
        connectionRate = 100.0
    data[date] = x[date]
    data[cell] = x[cell]
    data[rrcReqNum] = x[rrcReqNum]
    data[rrcReqSucNum] = x[rrcReqSucNum]
    data[e_rabReqSucNum] = x[e_rabReqSucNum]
    data[e_rabReqNum] = x[e_rabReqNum]
    data[u'接通率'] = connectionRate
    data[u'状态'] = connectionRateLowCellSearch(data[rrcReqNum], e_rabReqNum, connectionRate)
    return data[cell],data[u'状态']


def dropHighSearch(x, date, cell, e_rabAbRelNum, e_rabNmRelNum, ueConAbRelNum, ueConNmRelNum):
    data = dict()
    if (x[e_rabAbRelNum] + x[e_rabNmRelNum] + x[ueConAbRelNum] + x[ueConNmRelNum]) >= 1:
        dropRate = 100 * (x[e_rabAbRelNum] + x[ueConAbRelNum]) /(x[e_rabAbRelNum] + x[e_rabNmRelNum] +
                                                                 x[ueConAbRelNum] + x[ueConNmRelNum])
    else:
        dropRate = 0.0
    data[date] = x[date]
    data[cell] = x[cell]
    data[e_rabAbRelNum] = x[e_rabAbRelNum]
    data[e_rabNmRelNum] = x[e_rabNmRelNum]
    data[ueConAbRelNum] = x[ueConAbRelNum]
    data[ueConNmRelNum] = x[ueConNmRelNum]
    data[u'掉线率'] = dropRate
    return data


def rruHighSearch(x, date, cell, e_rabAbRelNum, e_rabNmRelNum, ueConAbRelNum, ueConNmRelNum):
    pass