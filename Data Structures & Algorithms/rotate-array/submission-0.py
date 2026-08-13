class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverseArr(arr,start, end):
            l = start
            r = end
            while l<r:
                arr[l], arr[r] =  arr[r], arr[l]
                l+=1
                r-=1
            return arr
        n = len(nums)
        k = k%n
        nums = reverseArr(nums,0,len(nums)-1)
        nums = reverseArr(nums, 0, k-1)
        nums = reverseArr(nums,k , len(nums)-1)

            