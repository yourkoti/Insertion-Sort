# Insertion Sort Algorithm Impplementation Using Python

def insertion_sort(list):
	for i in range(0,len(list)):
		for j in range(i-1,0,-1):
			if list[j]>list[j+1]:
				#swapping
				list[j],list[j+1] = list[j+1],list[j]
	return list

list = [10,25,15,45,30]
print(insertion_sort(list))

# output:[10,15,25,30,45]