def outer():
    x = 1
    
    def inner():
        nonlocal x
        # global x
        x = 2

    


    inner()
    print(x)

outer()