import graph
import path
import json
import linstr

class General:
    def __init__(self):
        self.g = graph.Graph()
        self.sc = graph.RVS.StopQuery('stops_con.json')
        self.doneAll = False
    
    def graph(self):
        rv = graph.RVS.RouteVarQuery('vars.json')
        lq = linstr.LineStringQuery('converted.json')
        for p in lq.Paths:
            routeId = p.get('RouteId')
            routeVarId = p.get('RouteVarId')
            lines = p.get_linestring()
            vars = rv.searchByABC({'RouteId': int(routeId), 'RouteVarId': int(routeVarId)})
            minutePerKilo = vars[0].get('RunningTime') * 1000 / vars[0].get('Distance')
            stops = self.sc.searchByABC({'RouteId': routeId, 'RouteVarId': routeVarId})
            for i in range(len(stops) - 1):
                frm = (stops[i].get('Lng'), stops[i].get('Lat'))
                to = (stops[i + 1].get('Lng'), stops[i + 1].get('Lat'))
                self.g.add_edge(stops[i].get('StopId'), stops[i + 1].get('StopId'), frm, to, minutePerKilo, lines)
                
        print("Done Graph")
       
    
    def shortest_path_all(self):
        for vertex in self.g.get_vertices():
            if graph.djikstra(self.g, self.g.get_vertex(vertex)):
                break
        print('Done')
        self.doneAll = True
    
    def shortest_path_to_file(self):
        with open('shortest_path.json', 'w') as f:
            for vertex in self.g.get_vertices():
                start = self.g.get_vertex(vertex)
                if graph.djikstra(self.g, start):
                    break
                for other in self.g.get_vertices():
                    d = {}
                    d['StartStopId'] = vertex
                    d['EndStopId'] = other
                    d['PassStop'] = [s.get_stopId() for s in start.get_shortest_route(self.g.get_vertex(other))]
                    json_data = json.dumps(d, ensure_ascii=False)
                    f.write(json_data + '\n')
        print('Done')
    
    def shortest_path(self, frm:dict, to:dict):
        st = self.sc.searchByABC(frm)
        start = self.g.get_vertex(st[0].get('StopId'))
        tt = self.sc.searchByABC(to)
        end = self.g.get_vertex(tt[0].get('StopId'))
        if self.doneAll == True:
            return [self.get_stop(s.get_stopId()).get('Name') for s in start.get_shortest_route(end)]
        graph.djikstra(self.g, start)
        return [self.get_stop(s.get_stopId()).get('Name') for s in start.get_shortest_route(end)]
    
    def x_yAsJson(self):
        paths = path.PathQuery('paths.json')
        with open('converted.json', 'w') as f:
            for pa in paths.Paths:
                output = graph.pp.x_y_coords(pa.get('lng'), pa.get('lat'), pa.get('RouteId'), pa.get('RouteVarId'))
                json_data = json.dumps(output, ensure_ascii=False)
                f.write(json_data + '\n')
    
    def stops_convert(self):
        self.g = graph.Graph()
        s = graph.RVS.StopQuery('stops.json')
        with open('converted.json', 'r') as file:
            lines = file.readlines()
            for line in lines:
                p = json.loads(line)
                coords = p['coords']
                routeId = p["RouteId"]
                routeVarId = p["RouteVarId"]
                lines = graph.pp.make_line_con(coords)
                stops = s.searchByABC({'RouteId': routeId, 'RouteVarId': routeVarId})
                for stop in stops:
                    self.g.add_vertex_2(stop, lines)
                    (x, y) = self.g.get_vertex2(stop).get_coordinates()
                    stop.set('Lng', x)
                    stop.set('Lat', y)
            s.outputAsJSON('stops_con.json', self.s.stops)
    
    def one_xy_as_json(self):
        paths = path.PathQuery('paths.json')
        l = paths.searchByABC({'RouteId': "6"})
        output = [graph.pp.x_y_coords(pa.get('lng'), pa.get('lat'), pa.get('RouteId'), pa.get('RouteVarId')) for pa in l]
        with open('converted.json', 'w') as f:
            for dic in output:
                json_data = json.dumps(dic, ensure_ascii=False)
                f.write(json_data + '\n')
    
    def zz_as_json(self):
        paths = path.PathQuery('paths.json')
        output = [graph.pp.x_y_coords(pa.get('lng'), pa.get('lat'), pa.get('RouteId'), pa.get('RouteVarId')) for pa in paths.Paths]
        with open('converted.json', 'w') as f:
            for dic in output:
                json_data = json.dumps(dic, ensure_ascii=False)
                f.write(json_data + '\n')

    def get_stop(self,stopId):
        l = self.sc.searchByABC({'StopId': stopId})
        return l[0]
    
    def take_most_important(self, num=10):
        for vertex in self.g.get_vertices():
            if graph.count_dijktra(self.g, self.g.get_vertex(vertex)):
                break
        print('Done')

        l = [self.get_stop(s[1].get_stopId()) for s in graph.maintain_heap(self.g, num)]
        self.sc.outputAsJSON('mostIm.json', l, True)
    

    def shortest_path_to_file(self, frm:dict, to:dict):
        sq = graph.RVS.StopQuery('stops.json')
        lq = linstr.LineStringQuery('converted.json')  
        paths = path.PathQuery('paths.json')
        st = self.sc.searchByABC(frm)
        start = self.g.get_vertex(st[0].get('StopId'))
        tt = self.sc.searchByABC(to)
        end = self.g.get_vertex(tt[0].get('StopId'))
        if self.doneAll == False:
            graph.djikstra(self.g, start)
        passStops = start.get_shortest_route(end)
        d = {}
        d['StartStopId'] = start.get_stopId()
        d['EndStopId'] = end.get_stopId()
        d['PassStop'] = [self.get_stop(s.get_stopId()).get('Name') for s in passStops]
        lat = []
        lng = []
        var_lst = []
        for i in range(len(passStops) - 1):
            f = sq.searchByABC({'StopId': passStops[i].get_stopId()})
            frm = f[0]
            t = sq.searchByABC({'StopId': passStops[i + 1].get_stopId()})
            to = t[0]
            vars = sq.searchByVars(frm, to)
            if not vars:
                print(self.get_stop(passStops[i].get_stopId()).get('Name'))
                print(self.get_stop(passStops[i + 1].get_stopId()).get('Name'))

            line = lq.searchByABC({'RouteId': vars[0]['RouteId'], 'RouteVarId': vars[0]['RouteVarId']})
            p = paths.searchByABC({'RouteId': vars[0]['RouteId'], 'RouteVarId': vars[0]['RouteVarId']})
            pat = p[0]
            li = line[0].get_linestring()
            tup = graph.pp.connect_2_stops(passStops[i].get_coordinates(), passStops[i + 1].get_coordinates(), li)
            lat.append(frm.get('Lat'))
            lng.append(frm.get('Lng'))
            if tup is not None:
                pat_lat = pat.get('lat')
                pat_lng = pat.get('lng')
                lat.extend(pat_lat[tup[0]:tup[1]])
                lng.extend(pat_lng[tup[0]:tup[1]])
            var_lst.append(p[0])

        lat.append(to.get('Lat'))
        lng.append(to.get('Lng')) 
        d['Lat'] = lat
        d['Lng'] = lng
        rmd = dict.fromkeys(var_lst)
        var_lst = list(rmd)
        with open('shortest.json', 'w') as f:
            json_1 = json.dumps(d, ensure_ascii=False)
            f.write(json_1 + '\n')
            for line in var_lst:
                json_data = json.dumps(line.get_dict(), ensure_ascii=False)
                f.write(json_data + '\n')
        return
    
def find_min(vars:list, rv:graph.RVS.RouteVarQuery):
    vs = [t[0] for var in vars for t in rv.searchByABC({'RouteId': var['RouteId'], 'RouteVarId': var['RouteVarId']})]
    value = vars[0].get('RunningTime') * 1000 / vars[0].get('Distance')
    back = vs[0]
    for v in vs:
        mm = v.get('RunningTime') * 1000 / v.get('Distance')
        if mm < value:
            back = v
            value = mm
    return back