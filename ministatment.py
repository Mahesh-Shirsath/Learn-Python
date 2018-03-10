#   Here we are going to make ATM tranjection like credit and Debit
#   And give a Mini slip after all oprations

def main():
	a=[]
	b=[]
	c=[]
	name=raw_input("Enter user name : ")
	bankno=int(input("Enter user bank account no. : "))
	balance=int(input("Enter the balance in your account : "))
	a.append(balance)
	while 1:
		print "1.Credit"
		print "2.Debit"
		print "3.Mini-statment"
		choice=int(input("Enter the choice : "))
		b.append(choice)
		if choice==1:
			add=int(input("Enter the amount you wanted to add : "))
			balance=balance+add
			print "balance is : ",balance
			a.append(balance)
			c.append(add)

		elif choice==2:
			sub=int(input("Enter the amount you wanted to remove : "))
			if balance >=sub:
				balance=balance-sub
				print "balance is : ",balance
				a.append(balance)
				c.append(sub)
			else:
				print "Your accout does not have that much balance. "
		elif choice==3:
			break
		else:
			print "Your choice is wrong."
	print "Your name is :",name
	print "mini slip="
	print "Frist balance ",a[0]
	for i in range(0,len(a)):
		if b[i]==1:
			print "You credit ",c[i]," and balance become : ",a[i+1]
		elif b[i]==2:
			print "You debit  ",c[i]," and balance become : ",a[i+1]
		else:
			break
	print "And now your balance is : ",balance
main()
