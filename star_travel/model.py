straightLineDistances = {"Arad" : 366, "Bucharest" : 0, "Craiova" : 160, "Dobreta" : 242, "Eforie" : 161,
                         "Fagaras" : 178, "Giurgiu" : 77, "Hirsova" : 151, "Iasi" : 226, "Lugoj" : 244,
                         "Mehadia" : 241, "Neamt" : 234, "Oradea" : 380, "Pitesti" : 98, "Rimnicu Vilcea" : 193,
                         "Sibiu" : 253, "Timisoara" : 329, "Urziceni" : 80, "Vaslui" : 199, "Zerind" : 374}

romaniaMap = {
    "Arad" : [("Zerind",75),("Timisoara",118)],
    "Bucharest" : [("Giurgiu",90),("Pitesti",101),("Urziceni",85)],
    "Craiova" : [("Dobreta",120),("Pitesti",138),("Rimnicu Vilcea",146)],
    "Dobreta" : [("Craiova",120),("Mehadia",75)],
    "Eforie" : [("Hirsova",86)],
    "Fagaras" : [("Bucharest",211),("Sibiu",99)],
    "Giurgiu" : [("Bucharest",90)],
    "Hirsova" : [("Eforie",86),("Urziceni",98)],
    "Iasi" : [("Neamt",87),("Vaslui",92)],
    "Lugoj" : [("Mehadia",70),("Timisoara",111)],
    "Mehadia" : [("Dobreta",75),("Lugoj",70)],
    "Neamt" : [("Iasi",87)],
    "Oradea" : [("Sibiu",151),("Zerind",71)],
    "Pitesti" : [("Bucharest",101),("Craiova",138),("Rimnicu Vilcea",97)],
    "Rimnicu Vilcea" : [("Craiova",146),("Pitesti",97),("Sibiu",80)],
    "Sibiu" : [("Arad",140),("Fagaras",99),("Oradea",151),("Rimnicu Vilcea",80)],
    "Timisoara" : [("Arad",118),("Lugoj",70)],
    "Urziceni" : [("Bucharest",85),("Hirsova",98),("Vaslui",142)],
    "Vaslui" : [("Iasi",92),("Urziceni",142)],
    "Zerind" : [("Arad",75),("Oradea",71)] 
}

def getLocations():
    
    locations = []
    
    for location in romaniaMap.keys():
        locations.append(location)
    return locations

locations = getLocations()

def getNeighbors(location):
    
    if location in romaniaMap:
        return romaniaMap[location]
    else:
        return None

def aStarSearch(initLocation):
    
    goalLocation = "Bucharest"
    openList = [initLocation]
    closedList = []
    gDistance = {}
    gDistance[initLocation] = 0
    conections = {}
    conections[initLocation] = initLocation
    
    while(len(openList) > 0):
        
        location = None
        
        for lowerFLocation in openList:
           if (location == None or (gDistance[lowerFLocation] + straightLineDistances[lowerFLocation] < gDistance[location] + straightLineDistances[location])):
               location = lowerFLocation
        if location == goalLocation or romaniaMap[location] == None:
            pass
        else:
            for(neighbor,weight) in getNeighbors(location):
                if(neighbor not in openList and neighbor not in closedList):
                    openList.append(neighbor)
                    conections[neighbor] = location
                    gDistance[neighbor] = gDistance[location] + weight
                else:
                    if(gDistance[neighbor] > gDistance[location] + weight):
                        gDistance[neighbor] = gDistance[location] + weight
                        conections[neighbor] = location
                        if  neighbor in closedList:
                            closedList.remove(neighbor)
                            openList.add(neighbor)
        if(location == None):
            print("No se encontró una ruta")
            return None
        if (location == goalLocation):
            bestPath = []
            while(conections[location] != location):
                bestPath.append(location)
                location = conections[location]
            
            bestPath.append(initLocation)
            bestPath.reverse()
            print("The best path is: {}".format(bestPath))
            return bestPath
        openList.remove(location)
        closedList.append(location)
    
    print("Path does not exist :(")
    return None


aStarSearch("Eforie")