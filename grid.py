# Here we are goning to form a grid pattrn to form a table.
# Befor program see logic and all in grid.txt file,this can help you.

def frist(num):   # Here we do code for our first line of grid
    for i in range(0,num):
        print "+ - - - -",
    print "+"   # Here we create code for whole first line.

def second(num):  # This is for second-line of grid
    for i in range(0,4):
        for j in range(0,num):
            print "|        ",
        print "|"

def main():
    row=input("Enter the no of rows you want in your table : ")
    columns=input("Enter the no of columns you want in your table : ")
    for i in range (0,row):
        frist(columns)
        second(columns)
    frist(columns)

main()
