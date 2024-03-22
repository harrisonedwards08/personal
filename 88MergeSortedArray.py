class Solution(object):
    def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        nums1.extend(nums2)
        nums1.sort()

        for number in nums1:
            if number == 0:

                nums1.remove(number)
        return nums1
    
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    print(merge (nums1,m,nums2,n))




class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        nums1[m:] = nums2
        nums1.sort()

        # Remove all occurrences of 0 from nums1
        nums1[:] = [num for num in nums1 if num != 0]
        return nums1

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
solution = Solution()
print(solution.merge(nums1, m, nums2, n))



