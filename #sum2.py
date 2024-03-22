#sum2


nums = [3,2,4]
target = 6

class Solution(object):
    def twoSum(nums, target):

        output = []
        for i in range (len(nums)):
            for j in range (len(nums)):
                
                if nums[i] + nums[j] == target and i != j:
                    output.append(i)
                    output.append(j)
                    break
            if nums[i] + nums[j] == target:
                break
            

        return output


    print(twoSum(nums,target))


