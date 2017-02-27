__author = 'wj'

def handoverSuceessRateLowCellSearch(handoverRequestNumber, handoverSuccessRate):
    if handoverRequestNumber > 1000 and handoverSuccessRate < 90:
        return True
    return False