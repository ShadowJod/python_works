# a = 9 
# b = 9
 
# sum = a+b
# print(sum)

# def sum(a,b):
#     sum = a + b
#     print(sum)
#     return sum

# sum(1,2)

# sum(9,8)

# sum(7,7)

# def sumh(a,b):
#     return a + b

# sum = sumh(9,2)
# print(sum)


# def print_hello():
#     print("hello")
#     return print

# new = print_hello()
# print(new)


# def avg_sum(a,b,c):
#     sum = a+b+c
#     avg = sum/3
#     print(avg)
#     return avg

# avg_sum(6,8,9)

# 1st practice set of 
cities = ["newdelhi", "haryaana", "gurugaon","masoori", 'noida']
heores = ["thor", "ironman","shaktiman","captain" , "spiderman"]

# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(heores)

# def list(list):
#     for i in list:
#         print(i , end =" ")

# list(cities)

# def converter(a):
#     c = a*83
#     print("This is your indian ruppes: " ,c)

# converter(88)


# def main(a):
#     if(a %2 ==0):
#         print("this is an even number")
#     else:
#         print("this is an odd number")

# main(3)



# recusrion

def show(n):
    if(n==10):
        return
    print(n)
    show(n+1)

show(1)