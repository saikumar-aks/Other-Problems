A=list(map(int, input().split()))
x=len(A)
B=[]
j=0
count=0
while x>0:
 count=0
 for i in range(len(A)):
  if((A[i]%A[j]==0 or A[j]%A[i]==0) and i!=j):
      count+=1
 j+=1 
 B.append(count)
 x-=1
for i in B:
    print(i,end=' ')
