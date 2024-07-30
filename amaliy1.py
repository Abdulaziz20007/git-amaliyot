with open("./raqamlar.txt", 'r') as file:
    data = file.readlines()
nums = []
for data in data:
    nums.append(int(data))
print(sum(nums))

