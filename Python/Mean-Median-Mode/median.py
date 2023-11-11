l=[48,47,46,45,44]
N=len(l) #len of the list 
if N%2==0:
    median1 = l[N//2]
    median2 = l[N//2 -1]
    median = (median1 + median2)/2
else:
    median = l[N//2]
print("Median of l is ",median)