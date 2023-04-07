def compare(a,b):
	if(a>b):
		print(a,"is greater than ",b)
	elif(b>a):
		print(b,"is greater than",a)
	print(a,"is equal to be",b)	
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
compare(a,b)