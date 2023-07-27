class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 1. Brute Force
        # Time: O(nk)
        # Space: O(n-k+1)
        # if not nums:
        #     return []
        # if k == 1:
        #     return nums
        # res = []
        # for i in range(len(nums) - k + 1):
        #     res.append(max(nums[i:i+k]))
        # return res
        
        # 2. Deque
        # Time: O(n)
        # Space: O(n)
        if not nums:
            return []
        if k == 1:
            return nums
        res = []
        queue = deque()
        for i in range(len(nums)):
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            queue.append(i)
            if queue[0] == i - k:
                queue.popleft()
            if i >= k - 1:
                res.append(nums[queue[0]])
        return res
