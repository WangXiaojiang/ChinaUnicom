__author__ = 'wj'

def dlRadioResourceUtilizationHighCellSearch(dlRadioReasourceUtiization, rrcConnectionMaxNumber):
    if dlRadioReasourceUtiization > 100 and rrcConnectionMaxNumber > 100:
        return True
    return False
