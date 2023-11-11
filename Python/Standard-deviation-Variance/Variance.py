number_list = [26, 77, 13, 29, 10, 15]


print("The original list is : " + str(number_list))


mean = sum(number_list) / len(number_list)
res = sum((i - mean) ** 2 for i in number_list) / len(number_list)

print("The variance of list is : " + str(res))