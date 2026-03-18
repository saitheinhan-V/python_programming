nums = list(map(int,input("Enter numbers: ").split()))
target = int(input("Enter target: "))

rtype = []
for x in range(len(nums)):
    z = x + 1
    if z == len(nums): break
    for y in range(len(nums)-x-1):
        if nums[x] + nums[y+z] == target:
            rtype.append(x)
            rtype.append(y+z)
            break

print(rtype)