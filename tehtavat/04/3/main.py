nums = []
num = input("Anna luku: ")
while num != "":
    nums.append(int(num))
    num = input("Anna luku: ")
nums.sort()
print("Isoin numero:", nums[-1])
print("Pienin numero:", nums[0])