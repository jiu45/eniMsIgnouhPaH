from pyproj import Transformer
from shapely import Point, LineString, line_merge, MultiLineString


def convert_coordinates(coord:tuple):
    (lng, lat) = coord
    transformer = Transformer.from_crs(4326, 3405, always_xy=True)
    (x, y) = transformer.transform(lng, lat)
    return (x, y)

def map_stop(lng, lat, line:LineString):
    t = (lng, lat)
    (x, y) = convert_coordinates(t)
    point = Point((x, y))
    ma = line.interpolate(line.project(point))
    return (ma.x, ma.y)

def get_length(frm:tuple, to:tuple, lines:LineString):
    back = lines.project(Point(to)) - lines.project(Point(frm))
    if back < 0:
        if lines.project(Point(to)) < 0.8:
            return lines.length + back
        elif lines.length -  lines.project(Point(frm)) < 1000:
            return lines.length - lines.project(Point(frm))
    return back

def make_line(lng:list, lat:list):
    coords = [convert_coordinates(x, y) for (x, y) in zip(lng, lat)]
    line = LineString(coords)
    return line

def connect_2_stops(frm:tuple, to:tuple, lines:LineString):
    start = LineString.line_locate_point(lines, Point(frm))
    end = LineString.line_locate_point(lines, Point(to))
    l = []
    l.append(frm)
    if end < start:
        if LineString.line_locate_point(lines, Point(to)) < 0.8:
            end = lines.length
        elif lines.length - LineString.line_locate_point(lines, Point(frm)) < 1000:
            end = lines.length
    coords = list(lines.coords)
    for i in range(len(coords)):
        if LineString.line_locate_point(lines, Point(coords[i])) > start and LineString.line_locate_point(lines, Point(coords[i])) < end:
            l.append(coords[i])
        elif lines.line_locate_point(Point(lines.coords[i])) >= end:
            break
    if len(l) == 1:
        return None
    else:
        tup = (coords.index(l[1]), coords.index(l[-1]) + 1)
        return tup


def connect_stops(coords:list):
    newline = LineString(coords) 
    return newline

def x_y_coords(lng:list, lat:list, routeId, routeVarId):
    d = {}
    d['coords'] = [convert_coordinates((x, y)) for (x, y) in zip(lng, lat)]
    d['RouteId'] = routeId
    d['RouteVarId'] = routeVarId
    return d

def make_line_con(coords:list):
    line = LineString([tuple(a) for a in coords])
    return line

def reverse_coordinates(coord:tuple):
    (x, y) = coord
    transformer = Transformer.from_crs(3405, 4236, always_xy=True)
    (lng, lat) = transformer.transform(x, y)
    return (lng, lat)






