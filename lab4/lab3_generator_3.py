def my_function(x):
    for i in range(x):
        if (i%3==0 and i%4==0):
            print(i,end=",")
my_function(x=int(input()))