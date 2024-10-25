nums = []
while 1:
    num = input("Anna luku: ")
    if num == "":
        nums.sort()
        print("Isoin numero:", nums[-1])
        print("Pienin numero:", nums[0])
        break
    nums.append(int(num))
