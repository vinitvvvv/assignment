class User:
    def __init__(self, name, roles):
        self.name = name
        self.roles = roles
    
    def getName(self):
        return self.name
    
    def getRole(self):
        return list(map(lambda x: x.getRoleName(), self.roles))

    def isAllowed(self, resource, permission):
        for role in self.roles:
            if(role.isAllowed(resource, permission)):
                return True
        return False

    def __str__(self):
        return self.name + str(self.roles)
    
    def __repr__(self):
        return self.__str__()

    def addRole(self, role):
        self.roles.append(role)

    def getPermissionAndResource(self):
        ret = {}
        for role in self.roles:
            ret[role.getRoleName()] = role.getAccess()
        return ret


    