def sum(t,n):
	s = 0
	for i in range(1,t+1):
	    s += i**n
	    
	return s
			 

print("Hello! This is a sum calculator.")
print("\nHow many terms you want?")

while True:   
    
    a = input()
    a = int(a)
    if a < 0:
	    print("Please input a non-negative number into the calculator.")
	    print("\nHow many terms you want?")
	    continue
    else:
        break
	    
if a == 0:
	print(0)
        
        
else:
    print("\nHow much the power you want?")
    b = input()
    b = int(b)
        
    c = sum(a,b)
    print(c)
    
        
