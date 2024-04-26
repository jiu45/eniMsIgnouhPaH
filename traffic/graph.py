import RVS
import sys
import pp
from heapq import heapify, heappop, heappush, heappushpop

class Vertex:
    tag = 0
    def __init__(self, stopId, tup:tuple):
        self.stopId = stopId
        self.adjacent = {}
        self.shortest_route = {}
        self.distance = 20000000
        self.visited = False
        self.prev = None
        self.importance = 0
        (self.x, self.y) = tup
    
    def add_neighbour(self, neighbour, dist, time_weight=0):
        d = {'time': time_weight, 'dist': dist}
        self.adjacent[neighbour] = d
    
    def get_adjacent(self):
        return self.adjacent.keys()
    
    def get_stopId(self):
        return self.stopId
    
    def get_time_weight(self, neighbour):
        if self.adjacent.get(neighbour):
            return self.adjacent[neighbour]['time']
        else:
            return None
    
    def get_dist_weight(self, neighbour):
        return self.adjacent[neighbour].get('dist')
    
    def get_distance(self):
        return self.distance
    
    def get_coordinates(self):
        return (self.x, self.y)
    
    def set_visited(self):
        self.visited = True
    
    def set_distance(self, dist):
        self.distance = dist
    
    def set_unvisted(self):
        self.visited = False
    
    def set_prev(self, prev):
        self.prev = prev

    def set_time_weight(self, neighbour, time):
        self.adjacent[neighbour]["time"] = time
    
    def get_shortest_route(self, to):
        return self.shortest_route.get(to, [])
    def set_shortest_route(self, to, l:list):
        self.shortest_route[to] = l
    def clear_shortest_route(self):
        self.shortest_route.clear()

    
class Graph:
    def __init__(self):
        self.edge = {}
    
    def add_vertex(self, stopId, tup:tuple):
        if stopId in self.edge:
            return
        new_vertex = Vertex(stopId, tup)
        self.edge[stopId] = new_vertex
    
    def add_vertex_2(self, stop:RVS.Stop, lines:pp.LineString):
        if stop in self.edge:
            return
        tup = pp.map_stop(stop.get("Lng"), stop.get("Lat"), lines)
        new_vertex = Vertex(stop, tup)
        self.edge[stop] = new_vertex
    
    def get_vertex(self, n):
        if n in self.edge:
            return self.edge[n]
        else:
            return None
    
    def get_vertex2(self, n:RVS.Stop):
        if n in self.edge:
            return self.edge[n]
        else:
            return None
    
    def add_edge(self, frmId, toId, frm_coords:tuple, to_coords:tuple, minutesPerKilo, lines:pp.LineString):
        if frmId in self.edge and toId in self.edge:
            ti = self.edge[frmId].get_time_weight(self.edge[toId])
            if ti is not None:
                self.edge[frmId].set_time_weight(self.edge[toId], min(ti, minutesPerKilo * self.edge[frmId].get_dist_weight(self.edge[toId]) / 1000))
                return
        else:
            if frmId not in self.edge:
                self.add_vertex(frmId, frm_coords)
            if toId not in self.edge:
                self.add_vertex(toId, to_coords)
            
        dist = pp.get_length(self.edge[frmId].get_coordinates(), self.edge[toId].get_coordinates(), lines)
        time_weight = minutesPerKilo * dist / 1000
        self.edge[frmId].add_neighbour(self.edge[toId], dist, time_weight)
    
    def get_vertices(self):
        return self.edge.keys()
    
    def reset(self):
        for stop in self.edge:
            self.edge[stop].set_distance(sys.maxsize)
            self.edge[stop].set_unvisted()
            self.edge[stop].set_prev(None)
            self.edge[stop].clear_shortest_route()


def djikstra(aGraph:Graph, startStop:Vertex):
    aGraph.reset()
    startStop.set_distance(0)
    startStop.set_visited()
    hq = []
    heapify(hq)
    heappush(hq, (startStop.get_distance(), startStop))

    while hq:
        tup = heappop(hq)
        src = tup[1]
        src.set_visited()
        l = startStop.get_shortest_route(src.prev).copy()
        l.append(src)
        startStop.set_shortest_route(src, l)
        for stop in src.get_adjacent():
            if src.get_time_weight(stop) < 0:
                print(src.get_stopId())
                print(stop.get_stopId())
                print([t.get_stopId() for t in src.get_adjacent()])
                while len(hq):
                    heappop(hq)
                return True
            if stop.visited:
                continue
            newdist = src.get_distance() + src.get_time_weight(stop)
            if newdist < stop.get_distance():
                stop.set_distance(newdist)
                stop.set_prev(src)
                heappush(hq, (newdist, stop))
            
    return False

def get_route(frm:Vertex, to:Vertex):
    lst = []
    while to is not frm:
        lst.append(to)
        to = to.prev
    lst.append(frm)
    return list(reversed(lst))

def count_dijktra(aGraph:Graph, startStop:Vertex):
    aGraph.reset()
    startStop.set_distance(0)
    startStop.set_visited()
    hq = []
    heapify(hq)
    heappush(hq, (startStop.get_distance(), startStop))

    while hq:
        tup = heappop(hq)
        src = tup[1]
        src.set_visited()
        l = startStop.get_shortest_route(src.prev).copy()
        l.append(src)
        for s in l:
            s.importance+= 1
        startStop.set_shortest_route(src, l)
        for stop in src.get_adjacent():
            if stop.visited:
                continue
            newdist = src.get_distance() + src.get_time_weight(stop)
            if newdist < stop.get_distance():
                stop.set_distance(newdist)
                stop.set_prev(src)
                heappush(hq, (newdist, stop))
            
    return False

def maintain_heap(aGraph:Graph, num):
    hq = []
    for vertex in aGraph.get_vertices():
        t:Vertex = aGraph.get_vertex(vertex)
        if len(hq) < num:
            heappush(hq, (t.importance, t))
        else:
            heappushpop(hq, (t.importance, t))
    return hq



            
        

