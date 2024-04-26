class Stop(object):
    def __init__(self, StopId, Code, Name, StopType, Zone, Ward, AddressNO, Street, SupportDisability, Status, Lng, Lat, Search, Routes):
        self.StopId = StopId
        self.Code = Code
        self.Name = Name
        self.StopType = StopType
        self.Zone = Zone
        self.Ward = Ward
        self.AddressNo = AddressNO
        self.Street = Street
        self.SupportDisability = SupportDisability
        self.Status = Status
        self.Lng = Lng
        self.Lat = Lat
        self. Search = Search
        self.Routes = Routes

    def get_StopId(self):
        return self.StopId
    
    def get_Code(self):
        return self.Code
    
    def get_Name(self):
        return self.Name
    
    def get_StopType(self):
        return self.StopType
    
    def get_Zone(self):
        return self.Zone
    
    def get_Ward(self):
        return self.Ward
    
    def get_Street(self):
        return self.Street
    
    def get_AddressNo(self):
        return self.AddressNo
    
    def get_SupportDisability(self):
        return self.SupportDisability
    
    def get_Status(self):
        return self.Status
    
    def get_Lng(self):
        return self.Lng
    
    def get_Lat(self):
        return self.Lat
    
    def get_Search(self):
        return self.Search
    
    def get_Routes(self):
        return self.Routes
    
    def set_StopId(self, stopid):
        self.StopId = stopid
    
    def set_Code(self, newcode):
        self.Code = newcode
    
    def set_Name(self, name):
        self.Name = name
    
    def set_StopType(self, type):
        self.StopType = type
    
    def set_Zone(self, zone):
        self.Zone = zone
    
    def set_Ward(self, ward):
        self.Ward = ward
    
    def set_Street(self, street):
        self.Street = street
    
    def set_AddressNo(self, an):
        self.AddressNo = an
    
    def set_SupportDisability(self, IsSupport):
        self.SupportDisability = IsSupport
    
    def set_Status(self, status):
        self.Status = status
    
    def set_Lng(self, lng):
        self.Lng = lng
    
    def set_Lat(self, lat):
        self.Lat = lat
    
    def set_Search(self, search):
        self.Search = search
    
    def set_Routes(self, routes):
        self.Routes = routes

        