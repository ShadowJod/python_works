# count = 1
# while count <= 10:
#     print("hello nikhil")
#     count = count + 1

# i = 10
# while i >= 1:
#     print(i)
#     i= i - 1
# print("loop ended")

# question set for loops

# i = 0
# while i <= 100:
#     print(i)
#     i = i + 1

# i = 100
# while i >= 1:
#     print(i)
#     i = i - 1 


# i = 3
# while i <= 30:
#     print(i)
#     i = i + 1 * 3 

# i = 1
# n = int(input("enter the number :"))
# while i <= 10:
#     print(n*i)
#     i = i + 1

# nums = [1,4,9,16,25,36,49,64,81,100]

# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx = idx + 1

# nums = (1,4,9,16,25,36,49,64,81,100)
# x = int(input("enter the number you wanna search: "))
# i = 0

# while i < len(nums):
#     if(nums[i] == x):
#         print("we found the number at index:", i)
#     i = i + 1

# next we will studt about break and continue

# i = 1
# while i <= 5:
#     print(i)
#     if (i==3):
#        break
#     i = i +1

# print("we are outside of loop")


# i = 0 
# while i <= 10:
#     if(i%2!=0):
#         i = i+1
#         continue
#     print(i)
#     i = i +1    

# next is for loop

# list = [1,2,3,4,5,6]
# for i in list:
#     print(i)

# str = "saymyname"
# for i in str:
#     if (i=="m"):
#         print("i got you")
#         break
    
#     print(i)
  

# i = (1,4,9,16,25,36,49,64,81,100)
# x = 100
# index=0
# for p in i:
#     if( p==x):
#         print("number found",index)
#         break
#     index = index + 1



# for i in range(10):
#     print(i)
# for i in range (2,10):
#     print(i)
# for i in range(2,10,2):
#     print(i)


# for i in range(100 , 0, -1):
#     print(i)

# n = int(input("enter the number: "))
# for i in range(1,11):
#     print(n*i)

# for i in range(10):
#     pass
# print("hwll9")


# qestion set 

# n = 5
# i = 1
# fact = 1
# while i <=n:
#     fact = fact * i
#     i = i + 1
# print(fact)

fact = 1
n = 5
for i in range (1,n+1):
    fact = fact * i

print(fact)