"""
developeraccount
FILE: util
Created: 6/16/15 12:11 AM
Basic conversion tools
"""
__author__ = 'Mark Scrimshire:@ekivemark'

def str2int(inp):
    output = 0 + int(inp)

    return output

def str2bool(inp):
    if inp.upper() == "TRUE":
        output = True
    elif inp.upper() == "FALSE":
        output = False

    return output

