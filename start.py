import os
import sys, traceback
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.loadData import ROLES, RESOURCES, USERS
from model.role import Resource, Role
from model.user import User

ROLE_DB = {} # name as pk : obj as value

RESOURCE_DB = {} # name as pk : obj as value

USER_DB = {}

for resource in RESOURCES:
    r = Resource(resource)
    RESOURCE_DB[resource] = r

def init():
    for role, access in ROLES.items():
        res = []
        perm = []
        for a in access:
            if(a["RESOURCE"] not in RESOURCE_DB):
                raise Exception("Resource not found in db")
            resource = RESOURCE_DB[a["RESOURCE"]]
            permission = tuple(a["ACCESS"])
            res.append(resource)
            perm.append(permission)
        r = Role(role, res, perm)
        ROLE_DB[role] = r

    for user in USERS:
        roles = []
        for role in USERS[user]:
            if(role not in ROLE_DB):
                raise Exception("Role not found")
            roles.append(ROLE_DB[role])
        u = User(user, roles)
        USER_DB[user] = u


init()
# print(ROLE_DB, RESOURCE_DB, USER_DB)
def getRoleNames():
    ret = []
    temp = {}
    for idx, key in enumerate(ROLE_DB.keys()):
        ret.append(f'Press {idx} for {key}')
        temp[idx] = ROLE_DB[key]
    return '\n'.join(ret), temp

def getUserNames():
    ret = []
    temp = {}
    for idx, key in enumerate(USER_DB.keys()):
        ret.append(f'Enter {key} to login as  {key}')
        temp[key] = key
    return '\n'.join(ret), temp


curr_user = USER_DB['admin']

def getUserInput():
    message, keymap = getUserNames()
    username = input(f"{message}\nEnter username :::").strip()
    if(username not in keymap):
        raise Exception("User not found")
    return USER_DB[username]

def getRoleInput():
    message, keyMap = getRoleNames()
    roleIdx = int(input(f"Enter Rolename \n {message}\n"))
    if(roleIdx not in keyMap):
        raise Exception("Invalid Selection, rolling back")
    return keyMap[roleIdx]

def run():
    global curr_user
    while(True):
        curr_user_name = curr_user.getName()
        curr_user_role = curr_user.getRole()
        print(f"Hi! you are logged in as {curr_user_name} (role) {curr_user_role}")
        try:
            if('ADMIN' in curr_user.getRole()):
                print("Press 0 to exit")
                print("Press 1 for login as another user")
                print("Press 2 for create user")
                print("Press 3 for add role to user")
                print("Press 4 to see users roles")
                inp = int(input())
                if(inp not in [0,1,2,3,4]):
                    raise Exception("Invalid key pressed")
                if(inp == 0):
                    break
                if(inp == 1):
                    curr_user = getUserInput()
                elif(inp == 2):
                    username = input("enter username:: ")
                    if(username in USER_DB):
                        raise Exception("Username already exists")
                    role = getRoleInput()
                    u = User(username, [role])
                    USER_DB[username] = u
                elif(inp == 3):
                    tempUser = getUserInput()
                    tempRole = getRoleInput()
                    tempUser.addRole(tempRole)
                elif(inp == 4):
                    tempUser = getUserInput()
                    print(tempUser.getRole())
            else:
                print("Press 0 to exit")
                print("Press 1 for login as another user")
                print("Press 2 to see your roles")
                print("Press 3 to see your resources and permissions")
                inp = int(input())
                if(inp not in [0,1,2,3]):
                    raise Exception("Invalid key pressed")
                if(inp == 0):
                    break
                if(inp == 1):
                    curr_user = getUserInput()
                elif(inp == 2):
                    print("YOUR ROLES ARE :: ",curr_user.getRole())
                elif(inp == 3):
                    print("YOUR CAN ACCESS ::",curr_user.getPermissionAndResource())
            print('\n\n')
        except Exception as e:
            print(sys.exc_info()[1])

run()