from random import randint
n = int(input("Enter a number: "))
nums = [randint(0, 10) for _ in range(n)]
print(nums)
n = nums.sort() # sorts from smallest to biggest
print(nums)
averages = []
for i in range(len(nums)//2):
    minNum = nums[0]
    maxNum = nums[-1]
    print("Max: ", maxNum)
    print("Min: ", minNum)
    x = ((maxNum + minNum) / 2) # average calculated
    nums.remove(maxNum)
    nums.remove(minNum)
    print("Numbers: ", nums)
    print("Averages", averages)
    averages.append(x) # appending averages into list
print(averages, len(averages))



