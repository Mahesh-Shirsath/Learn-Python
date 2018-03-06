# Here we going impliment the logic of Tower Of Hanoi

# Here n is no of discks, A,B,C are the towers
# Where A is begien tower, B is end tower  and C is auxillary tower

def TOH(n,A,B,C):
    if n>=1:
        TOH(n-1,A,C,B)
        print "The move is",A,"to",B
        TOH(n-1,C,B,A)

n=input("Enter the no. of discks")
a='A'
b='B'
c='C'
TOH(n,a,b,c)
