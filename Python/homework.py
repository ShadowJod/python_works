# # 6 Wap to reverse a given number

# user_input = input("Enter the Value : ")
# length = len(user_input)

# i = length
# while(i > 0):
#     print(user_input[i-1])
#     i-=1



# # 3 Wap to find the sum of first 10 natural numbers using for loop

# sum = 0
# i = 0
# for n in range(11):
#     i = i + sum
#     sum += 1

# print("The Sum of First 10 Natural Number is :", i)



# # 2 Wap to print all even number between 1 to 100 using while loop

# i = 0
# while i <101:
#     if(i %2 == 0):
#         print(i)
        
#     i+=1




# #5 Wap to calculate factorial of a number

# user_input = int(input("Enter the Number : "))
# factorial = 1

# i = user_input
# while(i > 0):
#     factorial = factorial * i
#     i-=1
# print(factorial)

# print(f"The factorial of {user_input} is :", factorail)





# # 7 Wap takes in a number and finds the sum of digit in a number
# sum = 0
# user_input = input("Enter the Digit :")

# for i in user_input:
#     sum =  sum + int(i)

# print(sum)



#8 Wap to check whether it a palindrome or not

# def paln(user_input):

#     a = len(user_input)
#     palindrome = ""
#     for i in user_input:
#         b = user_input[a-1]
#         palindrome = palindrome + b
#         a-=1
#     return palindrome


# a = input("Enter the Digit : ")
# if(a == paln(a)):
#     print("It is Palindrome")
# else:
#     print("It is not a Palindrome")
    



#Wap to print fiboonic seriesd
userInput = int(input("Enter The Value : "))


a = 0 
b = 1
i = 0
while i <= userInput:
    print(i)
    a = b
    b = i
    i = a+b