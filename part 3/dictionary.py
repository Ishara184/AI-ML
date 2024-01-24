#used to store key value pairs
#key is unique
#value can be any data type
#we can add elements
#can modify elements


#    key  value
#      |    |
d = {"id":100, "name":"Saman", "salary":50000.00}
#          |             |                  |
#      d["id"]        d["name"]         d["salary"]

print("\n")

#display dictionary
print(d)
#diplay type
print(type(d))

print("\n")

#accessing elements
print(d["id"])
print(d["name"])
print(d["salary"])

print("\n")

#add elements
d ["bonus"] = 10000.00
print(d)

print("\n")

#modify elements
d["salary"] = 40000.00
print(d)

print("\n")

#adding collections
#add dictionary to the dictonary
d["address"] = {"no":24, "street":"Saliyagama", "town":"Moragollagama"}
print(d)
print("\n")
#accress elements
print(d["address"])
print(d["address"]["street"])
print("\n")
#adding list
d["phone"] = ["0113335555", "0226668888"]
print(d)
print("\n")
#access elemts
print(d["phone"][1])
print("\n")
