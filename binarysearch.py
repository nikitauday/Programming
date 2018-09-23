"""n=input("enter count")
arr = []
print("Enter",n,"values")
for i in range(int(n)):
	x = int(input())
	arr.append(x)   """
def count(arr,f,n):
	l=0
	r=n-1
	i=first(arr,l,r,f,n)
	if(i==-1):
		return i
	j=last(arr,i,n-1,f,n)
	return j-i+1
'''f=input("enter element to be searched")'''
def first(arr,l,r,f,n):
	if(l<=r):
		m=int((l+r)/2)
		if(m==0 or (int(arr[m-1])<f)and int(arr[m])==f):
			return m
		elif(arr[m]>f or arr[m]==f):
			return first(arr,l,(m-1),f,n)
		else:
			return first(arr,(m+1),r,f,n)
		return -1
def last(arr,l,r,f,n):
	if(l<=r):
		m=int((l+r)/2)
		if((m==n-1 or f<int(arr[m+1]))and int(arr[m])==f):
			return m
		elif(arr[m]<f or arr[m]==f):
			return last(arr,(m+1),r,f,n)
		else:
			return last(arr,l,(m-1),f,n)
		return -1




arr = [1, 2, 2, 2, 2, 3, 3, 3,5,7,8,9,9,11] 
f= 9# Element to be counted in arr[] 
n = len(arr)
c = count(arr, f, n) 
print ("%d occurs %d times "%(f, c)) 