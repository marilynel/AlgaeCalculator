'''
Calculate the amount of algae to add to the algal reservoir
'''

#totalReservoirVolume = 60000
#totalCellsNeeded = 0        #TODO
##nannoProportion = 0
##isoProportion = 0.5
#chaetProportion = 0.5
#nannoDensity = 0
##isoDensity = 7700000
#chaetDensity = 8350000
#nannoReq = 0
#isoReq = 0
#chaetReq = 0



def nannoCellsNeeded(totalCellsNeeded, nannoProportion):
    '''
    TODO: why is this *8 and the others are not?
    '''
    return totalCellsNeeded * nannoProportion * 8


def cellsNeeded(totalCellsNeeded, proportion):
    '''
    For Chaetocerous and Isochrysis
    '''
    return totalCellsNeeded * proportion


def volumeToPullFromPBR(totalNeeded, density):
    '''
    TODO: may not be relevant for Nanno
    '''
    return totalNeeded / density


def densityReservoir1(totalCellsNeeded, totalReservoirVolume):
    return totalCellsNeeded / totalReservoirVolume


def totalCellsNeeded(val):
    '''
    TODO
    '''
    return 1.5 * val


def checkProportions(nannoProp, isoProp, chaetProp):
    if (nannoProp + isoProp + chaetProp == 1):
        return True
    else:
        return False


