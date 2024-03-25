class Solution(object):
    def majorityElement(self, nums):
        
        prev = 1000

        results = {}
        
        nums.sort()

        for num in nums:
            if num in results.keys():
                results[num]+=1
            else:
                results[num] = 1
        
        return max(results, key=results.get)
        
print(Solution.majorityElement(0,[1,1,1,3,3,0,5]))




#lambda function

multNumbers = lambda x,y: x*y

print(multNumbers(10,5))


        