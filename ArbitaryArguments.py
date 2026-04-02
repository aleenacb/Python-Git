def myFun(*args, **kwargs):
    print("Non Keyword arguments:")
    for arg in args:
        print(arg)
    print("\n Keyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}=={value}")
myFun('Hey','Welcome',first='This is ',mid='my',last='Python Program')