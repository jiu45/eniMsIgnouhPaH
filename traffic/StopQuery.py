import csv
import json

class StopQuery(object):
    def __init__(self):
        self.output = []
    
    def searchByAtrributes(self, attributes, ds):
        for key, value in attributes.items():
            tmp = []
            for d in ds:
                if d[key] == value:
                    tmp.append(d)
            ds = tmp.copy()
        
        for d in ds:
            self.output.append(d)

    def outAsCSV(self, filename):
        fields = ['StopId', 'Code', 'Name', 'StopType', 'Zone', 'Ward', 'AddressNO', 'Street', 'SupportDisability', 'Status', 'Lng', 'Lat', 'Search', 'Routes']
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(self.output)
        
        print("Done convert to csv file.")

    def outAsJSON(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.output, file)
        
        print("Done convert to JSON file.")