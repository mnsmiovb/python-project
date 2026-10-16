travelDistance=int(input("Write  travel distance in km:"))
startingFee=2
if travelDistance>=0:
    if travelDistance<=5:
        distanceRate=0.7
    elif travelDistance<=15:
        distanceRate=0.6
        
    else:
         distanceRate=0.5
    distanceFee=travelDistance*distanceRate
    totalFare=startingFee+distanceFee
    print("Starting fee is",startingFee,"AZN.Distance fee is",distanceFee,'AZN. Then total fare is',totalFare)
else:
    print("Invalid distance")