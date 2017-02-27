#coding=utf-8
from pyspark import SparkConf
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

from methods.coreMethods import *


#os.environ["SPARK_HOME"] = "/usr/local/spark-2.0.spark-bin-hadoop2.7"
def add(x, y):
    return x + y


if __name__ == '__main__':
    conf = SparkConf().setAppName("TopCellSearch").setSparkHome("/usr/local/spark-2.0.spark-bin-hadoop2.7").setMaster('local')
    sc = SparkContext(conf=conf)
    ssc = StreamingContext(sc,batchDuration=CIRCLE)
    ssc.checkpoint(Check_Point_Path)
    dstream = ssc.textFileStream('/home/wj/PycharmProjects/TopCellSearch/meta')
    dropDstream = dstreamConnectionLowSearch(dstream)
    dropDstreamWindow = dropDstream.reduceByKeyAndWindow(func=add, invFunc=None, windowDuration=CIRCLE * 3,
                                                                                                slideDuration=CIRCLE)
    dropDstreamWindow.pprint()


    #dropRateRDD = dstream.flatMap(lambda x: x.split()).map(lambda x: (x,1)).reduceByKey(lambda x,y: x+y)
    #dropRateWindow = dropRateRDD.window(windowDuration=CIRCLE*3,slideDuration=CIRCLE)
    #dropRateWindow.pprint()
    ssc.start()
    ssc.awaitTermination()
