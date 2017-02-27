#coding=utf-8
import time

import pandas as ps

KPI_FILE_NAME = '/home/wj/PycharmProjects/TopCellSearch/meta/20170101-0201KPI.csv'
def getKPI(KPI_FILE_NAME=KPI_FILE_NAME):
    dataFrame = ps.read_csv(KPI_FILE_NAME, header=0, encoding='gbk')
    return dataFrame


def inputStream(KPI_FILE_NAME=KPI_FILE_NAME, duration=30):
    df = getKPI(KPI_FILE_NAME)
    axes = list()
    axes.append(u'索引')
    axes.extend([each for each in df.axes[1]])
    hd = None
    date = None
    for row in df.itertuples():
        _row = [each for each in row]
        data = dict(zip(axes, _row))
        if date is None:
            date = data[u'日期']
            hd = open(date, mode='a+')
        if data[u'日期'] != date:
            date = data[u'日期']
            hd.close()
            time.sleep(duration)
            hd = open(date, mode='a+')
        hd.write(str(data) + '\n')
    hd.close()



if __name__ == '__main__':
    inputStream()