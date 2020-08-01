#defining function solution
def solution(A,B):
	D=A+B # adding A and B lists
	C=[i for i in A if i in B]# for finding the common elements from both the list
	if len(C)!=0: # if there are common elements then we remove those common elements

		D=set(D)#converting list into set as it would remove the duplicate elements from the list
		for i in range(0,len(C)):
			D.remove(C[i])

			D=list(D)
			print(D)
	else: #else we would return the merged list
		print(D)


A=[]
B=[]
#taking input lists from the user
A = [item for item in input("Enter the  A list items : ").split()] 
B = [item for item in input("Enter the  B list items : ").split()] 
#calling function solution
solution(A,B)