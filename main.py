
from calculator1 import *
from calculator2 import *



def totalFlowRate(flowRates):
    return sum(flowRates)

def main():
    totalReservoirVolume = 60000
    totalNeeded = 80870400000
    nannoProp = 0
    isoProp = 0.5
    chaetProp = 0.5
    nannoDensity = 0
    isoDensity = 7700000
    chaetDensity = 8350000

    numTanks = 4
    swFlow = 72
    desiredOutflowAlgalDensity = 10000
    grazing = 55000  # TODO: may be able to calculate this?
    densityOfCellsInReservoir = 1347840

    if checkProportions(nannoProp, isoProp, chaetProp):
        isoNeeded = cellsNeeded(totalNeeded, isoProp)
        chaetNeeded = cellsNeeded(totalNeeded, chaetProp)
        print(f"Volumes of algae needed:\n"
              f"Nanno: TBD\n"
              f"Iso: {round(volumeToPullFromPBR(isoNeeded, isoDensity))} mL\n"
              f"Chaet: {round(volumeToPullFromPBR(chaetNeeded, chaetDensity))} mL\n"
            )

        print(f"Cell density in reservoir 1: {round(densityReservoir1(totalNeeded, totalReservoirVolume))} cells/mL\n")

        totalFlowTreatmentManifold = totalFlowInSWTreatementManifold(numTanks, swFlow)

        print(f"Number of cells needed: "
              f"{ findCellsNeeded(totalFlowTreatmentManifold, desiredOutflowAlgalDensity, grazing)}")





    else:
        print("Proportions do not add up. Exiting.")
        exit()


if __name__ == "__main__":
    main()