import RVS

s = RVS.StopQuery('stops.json')

s.outputAsJSON('cmp2.json', s.searchByABC({'RouteId': '6'}))