import sys


class Solution:
  def jump(self, nums):
    mintimes = [0] + [sys.maxsize] * (len(nums) - 1)
    for i in range(0, len(nums) - 1):
      for j in range(1, min(nums[i] + 1, len(nums) - i)):
        mintimes[i + j] = min(mintimes[i + j], mintimes[i] + 1)
    return mintimes[-1]


s = Solution()
nums = [6, 2, 6, 1, 7, 9, 3, 5, 3, 7, 2, 8, 9, 4, 7, 7, 2, 2, 8, 4, 6, 6, 1, 3]
print(s.jump2(nums))
