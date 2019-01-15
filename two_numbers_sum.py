""""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].


由于题目说了有且只有唯一解，可以考虑两遍扫描求解：第一遍扫描原数组，将所有的数重新存放到一个dict中，该dict以原数组中的值为键，
原数组中的下标为值；第二遍扫描原数组，对于每个数nums[i]查看target-nums[i]是否在dict中，若在则可得到结果。 
"""

class Solution():
	def twoSums(nums,target):
		if len(nums)<=1:
			return False
		b_dict={}
		for i in range(len(nums)):
			if nums[i] in b_dict:
				return [b_dict[nums[i]],i]
			else:
				b_dict[target-nums[i]]=i