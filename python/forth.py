# here we gonna understand about dictionary


info = {
    "name": "nikhil",
    "age": 19,
    "subject": ["dbms","oops in java", "cn","se"],
}
print(type(info))
print(info)
print(type(info["subject"]))
info["name"] = "gungun"
print(info)

info["pass"] = True
print(info)


student = {
     "name" : "nikhil",
     "age" : 99,
     "subject" : {
         "phys" : 99,
         "chemis" : 77,
         "data" : 88,
                   }
}

print(student)
print(student["subject"]["data"])
print(student.keys())
print(list(student.keys()))
print(student.values())
print(list(student.items()))
me = list(student.items())
print(me[0])
print(student.get("data"))
student.update({"city":"delhi"})
print(student)
print(student["name"])


# this is about set

set1 = {1,2,3,4,5,5,6,6,}
print(set1)
print(type(set1))
print(len(set1))

emptset = set()
print(type(emptset))
list= ["nikhil",8,3,3]
print(type(list))
dic = {"nikhil": "Mishra","age": 77}
print(type(dic))
tup = (1,2,3,4,5)
print(type(tup))

empt = set()
empt.add(1)
empt.add("nikhil")
empt.remove("nikhil")
empt.clear()
print(empt)
print(empt.pop())


# here are some set methods\
set1 = {1,2,3,4}
set2 = {2,5,6,7}

print(set1.union(set2))
print(set1.intersection(set2))

# practice set question


dic = {"cat":"a small animal",
       "table" : ["a peice of furniture ","look up to you"]
       }
print(dic)

set = {"python","java","c++","python","javascript","java","python","java","c++","c"}
print( len(set),"classroom required for each subject")

dic = {}

x = int(input("enter the marks of phys: "))
dic.update({"phys": x})

x  = int(input("enter the marks of maths: "))
dic.update({"maths" : x })

x  = int(input("enter the marks of eng: "))
dic.update({"eng" : x })

print(dic)

set = {9,9.0}
print(set)

dic = {
    88 : 00
}
print(dic)