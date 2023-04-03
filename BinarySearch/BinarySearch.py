# BinarySearch

nums = [4,6,2,4,3,7,8,1,9,5,34,65,82,35,65]
nums.sort()
print(nums)

search_obj = 9

lowest = 0
highest = len(nums) - 1
index = None

while lowest <= highest and index is None:
    mid = (lowest + highest) // 2

    if nums[mid] == search_obj:
        index = mid
    else:
        if search_obj<nums[mid]:
            highest = mid - 1
        else:
            lowest = mid + 1

print(f"Found it under {index} index.")


