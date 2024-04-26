class RouteVar(object):
    def __init__(self, RouteId, RouteVarId, RouteVarName, RouteVarShortName, RouteNo, StartStop, EndStop, Distance, Outbound, RunningTime):
        self.RouteId = RouteId
        self.RouteVarId = RouteVarId
        self.RouteVarName = RouteVarName
        self.RouteVarShortName = RouteVarShortName
        self.RouteNo = RouteNo
        self.StartStop = StartStop
        self.EndStop = EndStop
        self.Distance = Distance
        self.Outbound = Outbound
        self.RunningTime = RunningTime
    
    def get_RouteId(self):
        return self.RouteId
    
    def get_RouteVarId(self):
        return self.RouteVarId
    
    def get_RouteVarName(self):
        return self.RouteVarName
    
    def get_RouteVarShortName(self):
        return self.RouteVarShortName
    
    def get_RouteNo(self):
        return self.RouteNo
    
    def get_StartStop(self):
        return self.StartStop
    
    def get_EndStop(self):
        return self.EndStop
    
    def get_Distance(self):
        return self.Distance
    
    def get_Outbound(self):
        return self.Outbound
    
    def get_RunningTime(self):
        return self.RunningTime
    
    def set_RouteId(self, id):
        self.RouteId = id
    
    def set_RouteVarId(self, rvid):
        self.RouteVarId = rvid
    
    def set_RouteVarName(self, fname):
        self.RouteVarName = fname
    
    def set_RouteVarShortName(self, sname):
        self.RouteVarShortName = sname
    
    def set_RouteNo(self, n):
        self.RouteNo = n
    
    def set_StartStop(self, start):
        self.StartStop = start
    
    def set_EndStop(self, end):
        self.EndStop = end
    
    def set_Distance(self, distance):
        self.Distance = distance
    
    def set_Outbound(self, outbound):
        self.Outbound = outbound
    
    def set_RunningTime(self, time):
        self.RunningTime = time
    
    