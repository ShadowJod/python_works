# # WAP TO PRINT ONLY AT 18,60,78 USING LOOP 1 TO 100 USING CONTINUE

# i = 0 
# while i <= 100:
#     if(i == 18 or i == 60 or  i == 78):
#         print(i)
#         i+= 1
#         continue
#     i += 1


# # WAP TO PRINT ALL EVEN NUMBER USING FUNCTION


# def even(a):
#     i = 0
#     while i<= a:
#         if(i % 2==0):
#             print(i)

#         i+=1

# even(98)


# WAP TO SEARCH FOR A ELEMENT FROM A LIST


# list = [10,9,8,7,6,5,4,3,2,1]
# def search(j):
#     a = 0
#     for i in list:
#        if( i == j):
#            print("i found the element at index : ",a)
          
#        else:
            
#             a+=1
            
           
    
           
       
     
        
        
    
# search(6)


# WAP TO PRINT FIBAANAIC SERIES

userInput = int(input("Enter The Value : "))


a = 0 
b = 1
i = 0
while i <= userInput:
    print(i)
    a = b
    b = i
    i = a+b
    