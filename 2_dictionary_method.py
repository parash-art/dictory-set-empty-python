mydict = {
     "fast":"in the faster bike create by anyone",
    "parash": "I am a programming",
    "marks":[1, 2, 5, 9, 7],
    "anotherdict": {'harry': 'player'},
    1: 2
}
#dictionary methods
#print(mydict.keys()) 
print(list(mydict.keys())) # prints the keys of the dictionary
print(list(mydict.values())) # prints the keys of the dictionary
print(list(mydict.items())) # prints the keys of the dictionary keys, view all the contains
print(mydict)
updatedict = {
    "lookup":"firnd of the devils",
    "marks":[1, 2, 5, 9, 7],
    14:45
    
}
mydict.update(updatedict) #update the dictionary by adding key-value pairs from updatedict
print(mydict)

print(mydict.get("parash")) # print values associated with the key "harry" 

print(mydict["parash"])#  print values associated with the key "harry"

#difference between .get and [] syntax in dictionaries

print(mydict.get("parash2")) # it iwll not show you error but 

print(mydict["parash2"])# it will show you a error in this. throws an error as parash2 is not present in the dict.