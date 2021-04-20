class Resource:
    def __init__(self, name):
        self.name = name
   
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.__str__()

class Role:
    def __init__(self, role_name, resources, permission):
        self.role_name = role_name
        self.access = {}
        if(len(resources) != len(permission)):
            raise Exception("uneven length of resource and permission")
        l = len(resources)
        for i in range(l):
            self.access[resources[i]] = permission[i]

    def __str__(self):
        return self.role_name
    
    def __repr__(self):
        return self.__str__()
    
    def getRoleName(self):
        return self.role_name
    
    def getAccess(self):
        return self.access

    def addAccess(self, resource, permission):
        if(resource in self.access and permission in self.access[resource]):
            raise Exception("Permission already provided")
        self.access[resource] = permission
        
    def isAllowed(self, resource, permission):
        if(resource in self.access and permission in self.access[resource]):
            return True
        return False
    



