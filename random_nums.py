import random
# rands = random.randint(1, 10)
# print(rands)
numbers_list = []
for i in range(10):
    rands = random.randint(1, 10)
    numbers_list.append(rands)
    print(numbers_list)

print(numbers_list)
print(len(numbers_list))
print(set(numbers_list))