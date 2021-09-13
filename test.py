# This is a function finding the max sum of a sub-array in a list of integers

def maxSubArray(nums):
	current_subarray = max_subarray = nums[0]
	for num in nums[1:]:
		current_subarray = max(num, current_subarray + num)
		max_subarray = max(max_subarray, current_subarray)
	return max_subarray

print(maxSubArray([1,2,3-5,4,2,4]))
