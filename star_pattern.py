#Here we are goning to form a star Star_pattern using functions and loops
# Here we use for loop and one functions

def increasing(n):    #This function is for first line for increasing stars
    for i in range (0,n):
        for j in range (0,i+1):
            print "*", #In Python 3.x instead of "," we use the function  end=""
        print

def decreasing(n):    #This function is for last line for decreasing stars
    for i in range (1,n):
        for j in range (n,i,-1):
            print "*",
        print


n=int(input("Enter the no. of line you want in Star_pattern : "))
increasing(n)
decreasing(n)
