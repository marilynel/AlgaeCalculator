from calculator1 import *


#numTanks = 4
#swFlow = 72
#totalFlow = numTanks * swFlow


def totalFlowInSWTreatementManifold(numTanks, swFlow):
    return numTanks * swFlow


def findTotalFlow(numTanks, swFlow):
    return numTanks * swFlow


#desiredOutflowAlgalDensity = 10000
#grazing = 55000             # TODO: may be able to calculate this?

#cellsNeeded = totalFlow * (desiredOutflowAlgalDensity + grazing)
def findCellsNeeded(totalFlowTreatmentManifold, desiredOutputAlgalDesnity, grazingRate):
    return totalFlowTreatmentManifold * (desiredOutputAlgalDesnity + grazingRate)


#densityOfCellsInReservoir = 1347840

#flowRateMeteringPump = cellsNeeded / densityOfCellsInReservoir
def findFlowRateMeteringPump(cellsNeeded, densityOfCellsInReservoir):
    return cellsNeeded / densityOfCellsInReservoir


# TODO: where did these values come from???
#strokeRate = round((1.2123108961 * flowRateMeteringPump) - 0.8736643925)
#actualFlowRateUsed = (0.824012048 * strokeRate) + 0.7349112036

def findStrokeRate(flowRateMeteringPump):
    return round((1.2123108961 * flowRateMeteringPump) - 0.8736643925)

def findActualFlowRateUsed(strokeRate):
    return (0.824012048 * strokeRate) + 0.7349112036