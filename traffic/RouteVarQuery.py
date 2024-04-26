import csv
import json

class RouteVarQuery(object):
    def __init__(self):
        self.output = []
    
    def searchByAtrribute(self, attributes, ds):
        for key, value in attributes.items():
            tmp = []
            for d in ds:
                if d[key] == value:
                    tmp.append(d)
            ds = tmp.copy()
        
        for d in ds:
            self.output.append(d)

    def outAsCSV(self, filename):
        s = "RouteId, RouteVarId, RouteVarName, RouteVarShortName, RouteNo, StartStop, EndStop, Distance, Outbound, RunningTime"
        fields = s.split(", ")
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(self.output)
        print("Done convert to csv.")

    def outAsJSON(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.output, file)
        
        print("Done convert to JSON file.")
        