#coding=utf-8
from operator import delitem
from pyspark import SparkConf
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

from CellContainer import *
from conf.config import *
from methods.coreMethods import *


def inQueue(x, cell):
    if x[0] not in cell.cellDict:
        cell.addCell(x)
        return x[0], 1
    return x[0], 0


def deQueue(x, cell):
    if x[0] in cell.cellDict:
        delitem(cell.cellDict, x[0])
        return x[0], 1
    return x[0], 0


def updateState(x, y):
    if x in None:
        x = dict()
        return x
    else:
        x[y[u'日期']] = y[u'状态']
        return x


def addByValue(x, y):
    return x[0] + y[0], x[1]


if __name__ == '__main__':

    cell = CellContainer()

    conf = SparkConf().setAppName("TopCellSearch").setSparkHome(Spark_Home).setMaster('local[2]')
    sc = SparkContext(conf=conf)
    ssc = StreamingContext(sc, batchDuration=Duration)
    ssc.checkpoint(Check_Point_Path)

    dstream = ssc.textFileStream(Meta_Content)
    dstream.cache()

    dropDstreamLow, dropDstreamHigh = dstreamConnectionLowSearch(dstream)

    dropDstreamWindowLow = dropDstreamLow.reduceByKeyAndWindow(func=lambda x, y: (x[0] + y[0], x[1]),
                                                invFunc=None,windowDuration=Duration * 3,slideDuration=Duration)

    rdd_in = dropDstreamWindowLow.filter(lambda x: x[1][0] >= 2)

    dropDstreamWindowHigh = dropDstreamHigh.reduceByKeyAndWindow(func=lambda x, y: (x[0] + y[0],x[1]),
                                                invFunc=None, windowDuration=Duration * 3,slideDuration=Duration)

    rdd_out = dropDstreamWindowHigh.filter(lambda x: x[1][0] >= 3)

    rdd_in.map(lambda x: inQueue(x, cell)).pprint()
    rdd_out.map(lambda x: deQueue(x, cell)).filter(lambda x: x[1] == 1).pprint()

    ssc.start()
    ssc.awaitTermination()


