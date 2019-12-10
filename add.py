# Python3 program to add two numbers 

def main(args): 
	num1 = args.get("num1")
	num2 = args.get("num2")
	#num1 = 5
	#num2 = 2
	# Adding two numbers 
	# User might also enter float numbers 
	sum = num1 + num2 
       	# Display the sum 
	# will print value in float 
	#print("The sum of {0} and {1} is {2}" .format(num1, num2, sum)) 

	return {"sum": sum}


