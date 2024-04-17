
nums = [12, 34, 5, 3, 2, 423, 2, 23, 44]
total = 0
index = 0
while index < len(nums):
    if nums[index] % 2 == 0:
        total += nums[index]
    index += 1
print(total)





# Faylga sonlarni yozish
with open('txt.fayl', 'w') as file:
    for i in range(1, 101):
        file.write(str(i) + '\n')