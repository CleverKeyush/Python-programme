l=[1,2,2,3,5,6,8,7,5,2,8,6,5,89,7,5,54,515,]
uniq=[]
mode1=[]
for i in l :
    if i not in uniq :
        uniq.append(i)
    else:
        mode1.append(i)
        
print(set(mode1))