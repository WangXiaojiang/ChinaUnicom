__author__ = 'wj'

def ulStrongInterfereCellSearch(avgInterferenceNoisePowerPerPRB,dlTraffic):
    if avgInterferenceNoisePowerPerPRB >= -100 and dlTraffic > 100:
        return True
    return False
