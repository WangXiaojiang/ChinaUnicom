#coding=utf-8
from operator import delitem


class CellContainer(object):

    def __init__(self):

        self.cellDict = dict()
        self.currentDate = None

    def addCell(self, cellInfo):
        '''
        将上榜小区加入self.cellDict中，记录当前窗口上榜小区
        :param cellInfo: 小区信息
        :return: self 返回对象本身
        '''
        self.cellDict[cellInfo[0]] = cellInfo[1] if cellInfo[0] not in self.cellDict else self.cellDict[cellInfo[0]]

    def deleteCell(self, cellName):

        delitem(self.cellDict, cellName)

    def revokeCell(self):

        return self
        pass

    @classmethod
    def revokeMethod(cls):

        pass

    def outPut(self):
        '''
        输出当前窗口上榜小区
        :return:
        '''
        for key,value in self.cellDict:
            print (key, value)

    def processDataFromStream(self, dataStream):
        self.currentDate = dataStream[0]
        for each in dataStream[1]:
            if each[0] in self.cellDict:
                pass
            else:
                self.cellDict[each[0]] = each[1]
        pass


class ConenctionRateLowCellContainer(CellContainer):

    def __init__(self):
        super(ConenctionRateLowCellContainer,self).__init__()

    @classmethod
    def revokeMethod(cls):
        pass
