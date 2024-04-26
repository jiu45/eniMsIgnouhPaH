import json
import csv

# Class RouteVar
class RouteVar:
    def __init__(self, route_var_dict):
        self.rv = route_var_dict

    def get(self, attr):
        return self.rv.get(attr, None)

    def set(self, attr, value):
        self.rv[attr] = value
    
    def get_dict(self):
        return self.rv
    
    def get_all_attr(self):
        return [key for key in self.rv]

# Class RouteVarQuery
class RouteVarQuery:
    def __init__(self, vars_json_file):
        self.output = []
        with open(vars_json_file, 'r') as f:
            lines = f.readlines()
            self.route_vars = [RouteVar(rv) for line in lines for rv in json.loads(line) if rv]          

    def searchByABC(self, attributes):
        self.output.clear()
        n_route_var = self.route_vars.copy()
        for key, value in attributes.items():
            n_route_var =  [rv for rv in n_route_var if rv.get(key) == value]
        self.output.extend(n_route_var)
        return self.output

    def outputAsCSV(self, csv_file, list):
        with open(csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.route_vars[0].get_all_attr())
            writer.writeheader()
            for output in list:
                writer.writerow(output.get_dict())

    def outputAsJSON(self, json_file, list):
        with open(json_file, 'w') as f:
            for line in list:
                json_data = json.dumps(line.get_dict(), ensure_ascii=False)
                f.write(json_data + '\n')
            

# Class Stop
class Stop:
    def __init__(self, stop_dict):
        self.s = stop_dict

    def get(self, attr):
        return self.s.get(attr, None)

    def set(self, attr, value):
        self.s[attr] = value
    
    def get_dict(self):
        return self.s
    
    def get_all_attr(self):
        return [key for key in self.s]

# Class StopQuery
class StopQuery:
    def __init__(self, stops_json_file):
        self.output = []
        with open(stops_json_file, 'r') as f:
            lines = f.readlines()
            self.Vars = []
            self.stops = []
            ss = [json.loads(line) for line in lines if line]
            if stops_json_file == 'stops.json':  
                self.Vars.extend(ss)     
                for var in self.Vars:
                    st = []
                    for stop in var["Stops"]:
                        tmp = stop
                        tmp["RouteId"] = var["RouteId"]
                        tmp["RouteVarId"] = var["RouteVarId"]
                        st.append(tmp)
                    l = [Stop(s) for s in st]
                    var['Stops'] = l
                    self.stops.extend(l)
            else:
                self.stops = [Stop(s) for s in ss]
            
    def searchByABC(self, attributes):
        self.output.clear()
        st = self.stops.copy()
        for key, value in attributes.items():
            st =  [s for s in st if s.get(key) == value or (isinstance(value, list) and all(val in value for val in s.get(key).split(", ")))]
        self.output.extend(st)
        return self.output

    def outputAsCSV(self, csv_file, list):
        with open(csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.stops[0].get_all_attr())
            writer.writeheader()
            for output in list:
                writer.writerow(output.get_dict())

    def outputAsJSON(self, json_file, list, justStop=False):
        with open(json_file, 'w') as f:
            for line in list:
                d = line.get_dict().copy()
                if justStop:
                    del d['RouteId']
                    del d['RouteVarId']
                json_data = json.dumps(d, ensure_ascii=False)
                f.write(json_data + '\n')

    def searchByVars(self, frm:Stop, to:Stop):
        l = []
        frm_id = frm.get('StopId')
        to_id = to.get('StopId')
        for var in self.Vars:
            ids = [s.get('StopId') for s in var['Stops']]
            if frm_id in ids and to_id in ids:
                if ids.index(to_id) - ids.index(frm_id) == 1:
                    l.append(var) 
        return l
