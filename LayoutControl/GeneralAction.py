#   Import universal scripts
import Globals
import MessageContainer

#   Import full supporting scripts

#   Import partial supporting scripts

#   Import Python modules

# --------------------------------------- #


def InverseDirection(currentPath):
    if currentPath.direction[-1] == "-":
        currentPath.direction[-1] = "+"
    else:
        currentPath.direction[-1] = "-"
    
    return currentPath


def InverseBool(flag):
    if flag == True:
        flag = False
    else:
        flag == True

    return flag


def TerminateSearch(path):
    path.endSearch = True