marks = [78.3,99.3,00.3,22.3,33.3]
print(marks)
str = ("nikhil is kuutta")
print(str)
print(str[0:len(str)])
print(type(marks))
print(marks[0])
print(len(marks))

student = ["nikhil", 99, 20 , "cs"]
print(student)
student[0]= "gungun"
print(student)

marks = [99,00,54,88,82,82]
print(marks[1:4])

list = [1,2,3,4,5,6,]
list.append(8)
print(list)
list.sort()
print(list)
list.sort(reverse = True)
print(list)
list.reverse()
print(list)
list.insert(1 ,9)
print(list)
list.remove(2)
print(list)
list.pop(5)
list.sort()
print(list)

# This is all about list and next we move on to the tuple


tup = (1,2,3,4,5,6)
print(type(tup))
print(tup.index(6))
print(tup.count(9))


# here wo goona for solving some questions

name1 = str(input("enter your 1st movie: "))
name2 = str(input("enter your 2st movie: "))
name3 = str(input("enter your 3st movie: "))

list = [name1,name2,name3]
print(list)
print(type(list))


list1 = [1,2,1]

copy_list1 = list1.copy()
copy_list1.reverse()

if (copy_list1 == list1):
    print("it is palindrome")

else:
    ("it is not palindrome")


grade = ["c","d","a","a","b","b","a"]
print(grade.count("a"))
grade.sort()
print(grade)