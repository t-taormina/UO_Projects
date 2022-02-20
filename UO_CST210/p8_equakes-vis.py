'''
CIS 210 Project 8-1: Earthquake Watch

Author: Tyler Taormina

Date: March 2, 2021

Credits: N/A

Description: Shows a k-means cluster of earth quake data plotted on a map

'''
from math import sqrt
import random
import turtle


def readfile(fname):
    '''
    (str) -> dict

    Reads a file skipping the header lines. Returns a dictionary with
    latitude and longitude storeds as values.

    EXAMPLES:
    >>> readfile('equake.txt')
    {1: (-33.6142, -178.4753), 2: (35.6305, 74.6387), 3: (35.6024, 74.6175),
    4: (27.3836, 56.5402), 5: (27.8431, 142.8263), 6: (-52.8602, 11.3306),
    7: (-5.5011, 151.7733), 8: (4.6912, 125.3986), 9: (17.8846, -66.864),
    10: (-30.3893, -177.5618), 11: (1.4714, 128.5553), 12: (-44.6079, 37.0941)}
    
    '''
    with open(fname, 'r') as myf:
        myf.readline()

        equakeDict = {}
        keyValue = 1

        for line in myf:
            vals = line.strip().rstrip().split(',')
            lat_long = (float(vals[1]), float(vals[2]))
            equakeDict[keyValue] = lat_long
            keyValue += 1
        return equakeDict


def euclidD(point1, point2):
    '''
    (tuple, tuple) -> int

    Returns the distance between two points

    EXAMPLES:
    >>>euclidD((1,4), (2, 7)
    3.1622776601683795

    >>>euclidD((0,0), (0,0))
    0.0

    >>>euclidD((0,0), (1, 1))
    1.4142135623730951
    
    '''
    total = 0
    for index in range(len(point1)):
        difference = (point1[index] - point2[index]) ** 2
        total = total + difference

    euclidDistance = sqrt(total)
    return euclidDistance

    
def createCentroids(num_centroids, equakeDict):
    '''
    (int, dict) -> list

    Returns a list of tuples/coordinates for use as centroids

    EXAMPLES:
    >>> createCentroids(2, edict)
    [(-5.5011, 151.7733), (35.6024, 74.6175)]
    

    '''
    centroids = []
    cCount = 0
    centroidKeys = []

    while cCount < num_centroids:
        rKey = random.randint(1, len(equakeDict))
        
        if rKey not in centroidKeys: #don't use the same key twice
            centroids.append(equakeDict[rKey]) #make centroid list
            centroidKeys.append(rKey)
            cCount += 1
            
    return centroids


#!!!!!seek explanation about this function!!!!!
def createClusters (k, centroids, equakeDict, iterations):
    '''
    (num, list, dict,  num) -> list

    returns a list of lists that uses the euclidD function to
    append the lists with the shortest possible distance from each
    individual set of coordinates(equakeDict) to the centroids.

    EXAMPLES:
    >>> createClusters(2, centroids, edict, 2)
    *****PASS 1 ***
    CLUSTER
    (-33.6142, -178.4753) (17.8846, -66.864) (-30.3893, -177.5618) 
    CLUSTER
    (35.6305, 74.6387) (35.6024, 74.6175) (27.3836, 56.5402) (27.8431, 142.8263)
    (-52.8602, 11.3306) (-5.5011, 151.7733) (4.6912, 125.3986)
    (1.4714, 128.5553) (-44.6079, 37.0941) 
    *****PASS 2 ***
    CLUSTER
    (-33.6142, -178.4753) (17.8846, -66.864) (-30.3893, -177.5618) 
    CLUSTER
    (35.6305, 74.6387) (35.6024, 74.6175) (27.3836, 56.5402) (27.8431, 142.8263)
    (-52.8602, 11.3306) (-5.5011, 151.7733) (4.6912, 125.3986)
    (1.4714, 128.5553) (-44.6079, 37.0941)
    

    '''
    for aPass in range(iterations):
        print('*****PASS', aPass + 1, '***')

        clusters = [] #create empty lists for the number of clusters wanted
        for i in range(k):
            clusters.append([])

        for aKey in equakeDict: #find distance to centroid
            distances = []
            for clusterIndex in range(k):
                distTo = euclidD(equakeDict[aKey], centroids[clusterIndex])
                distances.append(distTo)

            minDist = min(distances) #find minimum distance and it's index in distances list
            index = distances.index(minDist)

            clusters[index].append(aKey) #add to cluster

        dimensions = len(equakeDict[1]) #reconfigure clusters

        for clusterIndex in range (k):
            sums = [0] * dimensions

            for aKey in clusters[clusterIndex]:
                dataPoints = equakeDict[aKey]

                for ind in range(len(dataPoints)):
                    sums[ind] = sums[ind] + dataPoints[ind]

            for ind in range(len(sums)):
                clusterLen = len(clusters[clusterIndex])
                if clusterLen != 0:
                    sums[ind] = sums[ind] / clusterLen

            centroids[clusterIndex] = sums

        for c in clusters:
            print('CLUSTER')
            for key in c:
                print(equakeDict[key], end = ' ')
            print()
    return clusters
            


k = 4
iterations = 1


def visualizeQuakes(fname):
    '''
    (str) -> image

    returns a world map with the earth quake data from the file
    of choice plotted on the map

    TO SEE EXAMPLES...
    RUN PROGRAM WITH FILE: equake.txt 

    '''
    equakeDict = readfile(fname)
    quakeCentroids = createCentroids(k, equakeDict)
    clusters = createClusters(k, quakeCentroids, equakeDict, iterations)

    quakeT = turtle.Turtle()
    quakeWin = turtle.Screen()
    quakeWin.bgpic('worldmap.gif')
    quakeWin.screensize()

    wFactor = (quakeWin.screensize()[0] / 2) / 180
    hFactor = (quakeWin.screensize() [1] / 2) / 90

    quakeT.hideturtle()
    quakeT.up()

    colorList = ['red', 'lawngreen', 'blue', 'orange', 'cyan', 'yellow']

    for clusterIndex in range(4):
        quakeT.color(colorList[clusterIndex])
        for aKey in clusters[clusterIndex]:
            lat = equakeDict [aKey] [0]
            lon = equakeDict [aKey] [1]
            quakeT.goto(lat * hFactor, lon * wFactor)
            quakeT.dot()
    quakeWin.exitonclick()
    


def main():
    
    '''Program driver'''
    
    #fname = 'equakes.csv'
    fname = 'equake.txt'
    k = 4
    iterations = 4
    visualizeQuakes(fname)
    
if __name__ in '__main__':
    main()
      

    
    
    
    

    



            
            
        
       
    
