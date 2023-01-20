class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elementSum = 0
        for x in range(len(nums)):
            elementSum+= nums[x]
        digitSum = 0
         
        for x in range(len(nums)):
            if len(str(nums[x])) > 1:
                for num in str(nums[x]):
                    digitSum += int(num)
            else:
                digitSum += nums[x]
        return elementSum - digitSum
