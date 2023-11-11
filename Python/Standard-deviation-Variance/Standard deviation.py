number_list = [10, 8, 5, 10, 12]
 

print(The original list   + str(number_list))
 

mean = sum(number_list)  len(number_list)
variance = sum([((x - mean)  2) for x in number_list])  len(number_list)
res = variance  0.5
 
print(Standard deviation of sample is   + str(res))