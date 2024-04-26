import json
import csv

class Path:
    def __init__(self, Path_dict):
        self.p = Path_dict

    def get(self, attr):
        return self.p.get(attr, None)

    def set(self, attr, value):
        self.p[attr] = value
    
    def get_dict(self):
        return self.p
    
    def get_all_attr(self):
        return [key for key in self.p]

# Class PathQuery
class PathQuery:
    def __init__(self, Paths_json_file):
        self.output = []
        with open(Paths_json_file, 'r') as f:
            lines = f.readlines()
            self.Paths = [Path(json.loads(line)) for line in lines if line]

    def searchByABC(self, attributes):
        self.output.clear()
        st = self.Paths.copy()
        for key, value in attributes.items():
            st =  [p for p in st if p.get(key) == value or (isinstance(p.get(key), list) and value in p.get(key))]
        self.output.extend(st)
        return self.output

    def outputAsCSV(self, csv_file, list):
        with open(csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.Paths[0].get_all_attr())
            writer.writeheader()
            for output in list:
                writer.writerow(output.get_dict())

    def outputAsJSON(self, json_file, list):
        with open(json_file, 'w') as f:
            for line in list:
                json_data = json.dumps(line.get_dict(), ensure_ascii=False)
                f.write(json_data + '\n')
