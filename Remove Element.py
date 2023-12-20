#Remove Element
#page 163

class Solution(object):
    def removeElement(self, nums, val):
        if val == []:
            return 0
        else:
            for i in nums:
                if i==val:
                    nums.remove(i)
            print(len(nums))
        
nums = [3,2,2,3]
val = 3

S=Solution()
S.removeElement(nums,val)

