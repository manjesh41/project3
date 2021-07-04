'''
1 Write a Python function to find the Max of three numbers
'''
def maximum (a,b,c):
	if a>b>c:
		print(f"{a} is the maximum number")
	elif b>c>a:
		print(f'{b} is the maxmum number')
	else:
		print(f'{c} is the maximum number')
	return
maximum(10,20,40)