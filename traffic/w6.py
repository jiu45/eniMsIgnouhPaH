import json
import path
import linstr
import pp

base = {
  "type": "FeatureCollection",
  "features": []
}

ele = {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [],
        "type": "LineString"
      }
    }

f_name = "map"
tag = ".geojson"

def make_paths():
    p = path.PathQuery('paths.json')
    for pth in p.Paths:
        blocal = base.copy()
        nlocal = ele.copy()
        lat = pth.get("lat")
        lng = pth.get("lng")
        routeId = pth.get("RouteId")
        routeVarId = pth.get("RouteVarId")
        
        for i in range(len(lng) - 1):
            for j in range(2):
                l = [lng[i + j], lat[i + j]]
                nlocal["geometry"]["coordinates"].append(l)
            blocal["features"].append(nlocal)
        
        file_name = f_name + "_" + routeId + "_" + routeVarId
        create_file(blocal, file_name)


def make_a_path():
    p = path.PathQuery('paths.json')
    blocal = base.copy()
    nlocal = ele.copy()
    route6 = p.searchByABC({"RouteId": "35", 'RouteVarId': '70'})
    lat = route6[0].get("lat")
    lng = route6[0].get("lng")
    routeId = route6[0].get("RouteId")
    routeVarId = route6[0].get("RouteVarId")
    
    for i in range(len(lng) - 1):
        for j in range(2):
            l = [lng[i + j], lat[i + j]]
            nlocal["geometry"]["coordinates"].append(l)
        blocal["features"].append(nlocal)
    
    file_name = f_name + "_" + routeId + "_" + routeVarId
    create_file(blocal, file_name)



def create_file(geo_dict, file_name):
    with open(file_name, 'w') as f:
        json.dump(geo_dict, f)

def shortest_path():
    blocal = base.copy()
    nlocal = ele.copy()
    with open('shortest.json', 'r') as f:
        lines = f.readlines()
        data = json.loads(lines[0])
        lat = data["Lat"]
        lng = data["Lng"]
        routeId = "s"
        routeVarId = "n"
    
    for i in range(len(lng) - 1):
        for j in range(2):
            l = [lng[i + j], lat[i + j]]
            nlocal["geometry"]["coordinates"].append(l)
        blocal["features"].append(nlocal)
    
    file_name = f_name + "_" + routeId + "_" + routeVarId
    create_file(blocal, file_name)

def make_xy_path():
    lq = linstr.LineStringQuery('converted.json')
    blocal = base.copy()
    nlocal = ele.copy()
    route6 = lq.searchByABC({"RouteId": "6", 'RouteVarId': '2'})
    
    coords = route6[0].get('coords')
    a = [pp.reverse_coordinates(c) for c in coords]
    x, y = zip(*a)
    lng = list(x)
    lat = list(y)
    routeId = route6[0].get("RouteId")
    routeVarId = route6[0].get("RouteVarId")
    
    for i in range(len(lng) - 1):
        for j in range(2):
            l = [lng[i + j], lat[i + j]]
            nlocal["geometry"]["coordinates"].append(l)
        blocal["features"].append(nlocal)
    
    file_name = f_name + "_" + routeId + "_" + routeVarId
    create_file(blocal, file_name)

shortest_path()
        
                
            
            
    


