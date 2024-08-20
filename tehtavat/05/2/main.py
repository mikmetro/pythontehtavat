nums = []
num = input("Anna luku: ")
while num != "":
    nums.append(int(num))
    num = input("Anna luku: ")
nums.sort(reverse=True)
for i in range(5):
    print(f"#{i+1}", nums[i])
