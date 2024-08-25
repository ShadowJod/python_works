# # sum all the item in list

# list = [1,2,3,4,5]

# sum = 0
# for i in list:
#     sum = sum + i
# print(sum)

# # Multiply all the items in list

# list = [1,2,3,4,5]

# sum = 1
# for i in list:
#     sum = sum * i
# print(sum)

# # Largest number in the list

# list = [1,2,3,4,5,7]

# print(max(list))

# # Smallest Number in the list

# list = [1,2,3,4,5,7,8]

# print(min(list))

# # Copying the list

# list = [1,2,3,4,5,6,7]

# list1 = list
# print(list1)

# # Empty list or not

# list = [1,2,3,4,5,6,7]
# emptylist = []
# if(list == emptylist):
#     print("It is a empty list")

# else:
#     print("It is not a empty list")


# # count the string 1 and last index is same count 

# list = ["aba","xyz","aba","1221"]

# count = 0
# for i in list:
#     if(i[0]==i[len(i)-1]):
#         count+=1

# print(count)
    

# # Inserting value in empty list

# list = []
# while True:
#     a = int(input("Enter the number you insert :"))
#     list.append(a)
#     print(list)


# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]


# list = [(2,5),(1,2),(4,4),(2,3),(2,1)]

# i = 0
# while(i<len(list)):
#     print(list[i][1])
#     # a.sort()
#     i+=1


# Write a Python program to find the list of words that are longer than n from a given list of words.

list = ["apple","mango","banana","peas","orange"]

n =6 
count = 0
for i in list:
    length = len(i)
    if(length >= n):
        count+=1

print(count)