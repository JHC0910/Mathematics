def joseph(n,step,stay):
#n=total number of people; step;stay
	people = list(range(1,n+1))
	check = 0
	while len(people) > stay:
		for i in people[:]:
			check += 1
			if check == step:
				check = 0
				people.remove(i)
				print("No.{} has leaved! ".format(i))
	return people

save = 	joseph(150,11,8)
print("People who saved: ",save)		
			
		

