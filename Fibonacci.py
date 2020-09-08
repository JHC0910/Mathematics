print("Welcom to Fibonacci generator!! ")
print("\nHow many terms you want?")
while True:
    terms = input()
    terms = int(terms)

    n1 = 0
    n2 = 1
    step = 2


    if terms <= 0:
	    print("Error!! Please input a positive integer.\n")
	    print("How many terms you want?")
	    continue

    elif terms == 1:
	    print(n1,end=" , ")

    elif terms == 2:
	    print(n1,",",n2,end=" , ")

    else:
	    print(n1,",",n2,end=" , ") 
	    while step < terms:
		    nn = n1 + n2
		    print(nn,end=" , ")
		
		    n1 = n2
		    n2 = nn
		    step += 1
    break
		    	


