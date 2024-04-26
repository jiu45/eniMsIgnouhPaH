import RVS

rv = RVS.RouteVarQuery('vars.json')

query1 = {"RouteNo": "56"}

query2 = {"RouteNo": "06", "Outbound": True}

rv.outputAsCSV('q1.csv', rv.searchByABC(query1))

rv.outputAsJSON('q2.json', rv.searchByABC(query2))

s = RVS.StopQuery('stops.json')

f = s.searchByABC({'StopId': 421})
frm = f[0]
print(frm.get('Name'))
t = s.searchByABC({'StopId': 299})
to = t[0]
print(to.get('Name'))
print(s.searchByVars(frm, to))

query3 = {'RouteId': "6"}

query4 = {"Name": "Đại học Sư Phạm"}

s.outputAsJSON('q3.json', s.searchByABC(query3))

s.outputAsCSV('q4.json', s.searchByABC(query4))

