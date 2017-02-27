__author__= 'wj'

def connectionRateLowCellSearch(rrcRequestNumber,rabRequestNumber,radioConnectionRate):
    if rrcRequestNumber > 200 and rabRequestNumber > 200:
        if radioConnectionRate < 95:
            return 1
        return 0
    return 0
