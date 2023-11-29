# python3
import sys

def compute_min_refills(distance, tank, stops):
    numrefill, location= 0,0 #set the location as 0, number of refills # you need a pointer for location and a refil counter 
    stops = [0] + stops + [distance] #include the start and end points in the stops list   
    if distance <= tank:
        return 0
    else:
        while location < len(stops)-1: #location is less than the total stops - first starting point
            lastrefill = location #set the last refill point? before the location updated so at 0
            # print(location, lastrefill, len(stops))
            while location < len(stops)-1 and stops[location+1] - stops[lastrefill] <=tank: #above condition and subtracting +1 location from last fill giving total cost and updating location
                #if the value of the distance is less than the tank, its possible so location gets +1. No need to calculate each distance
                location += 1

            if location == lastrefill: #if location is equal to last refill means that we couldnt go next because not possible
                return -1
            if location < len(stops)-1: #if location is still less then +1 for num refill as refill occured ebfore jumping next locations
                numrefill +=1

        return numrefill


if __name__ == '__main__':
    d = list(map(int, input().split()))[0]
    m = list(map(int,input().split()))[0]
    n = list(map(int, input().split()))
    stops = list(map(int, input().split()))

    print(compute_min_refills(d, m, stops))
