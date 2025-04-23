#quadratic complexity

"""
class Solution(object):
    def twoSum(self, nums, target):

        for count1, value1 in enumerate(nums):
            print(count1, value1)    
            
            for count2, value2 in enumerate(nums[count1 + 1:]):
                print(count2, value2)
            
                if (value1 + value2 == target):
                    print("bingo!", target, "=", value1, "+", value2)  
                    return(count1, count2 + count1 + 1)
                    
"""
                    
#proper solution

class Solution(object):
   def twoSum(self, nums, target):
      dict = {}
      for i in range(len(nums)):
         if target - nums[i] in dict:
            return [dict[target - nums[i]],i]
         else:
            dict[nums[i]]=i
input_list = [2,8,12,15]
ob1 = Solution()
print(ob1.twoSum(input_list, 20))

# Another solution
#for i in range 
#target - i == k
#check if k is among the rest of i's
