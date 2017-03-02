__author__= 'wj'


def connectionRateLowCellSearch(rrcRequestNumber,rabRequestNumber,radioConnectionRate):
    if rrcRequestNumber > 200 and rabRequestNumber > 200:
        if radioConnectionRate < 95:
            return 1
        return 0
    return 0


def connectionRateHighCellSearch(radioConnectionRate):
    return 1 if radioConnectionRate > 98 else 0
