class Solution:
  def firstMissingPositive(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    i = 0
    while i < n:
      if nums[i] == i + 1 or nums[i] <= 0 or nums[i] > n:
        i += 1
      elif nums[nums[i]-1] != nums[i]:
        self.swap(nums, i, nums[i] - 1)
      else:
        i += 1
    i = 0
    while i < n and nums[i] == i+1:
        i+=1
    return i+1

  def swap(self, A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


solution = Solution()
print(solution.firstMissingPositive(nums=[1,1]))
