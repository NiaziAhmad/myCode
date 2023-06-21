""" Created on Thu Apr  6 05:00:42 2023.
@author: Administrator
"""
charachter = {}
print(len(charachter) == 0)
charachter = {97: "a", 98: "b", 99: "c", 65: "A", 66: "B", 67: "C"}
print(charachter.keys())
print(charachter.values())
charachter[68] = "D"
print(len(charachter))
print(charachter[99])
print(charachter.pop(97))
print(charachter.get(100, "false"))
charachter.clear()
print(len(charachter))
