from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0  # Current count of consecutive 1's
        maxi = 0  # Maximum count of consecutive 1's
        for num in nums:
            if num == 1:
                cnt += 1
            else:
                cnt = 0
            maxi = max(maxi, cnt)
        return maxi

if __name__ == "__main__":
    nums = [1, 1, 0, 1, 1, 1]
    obj = Solution()
    ans = obj.findMaxConsecutiveOnes(nums)
    print("The maximum consecutive 1's are", ans)
