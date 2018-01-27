class Solution:
  def matrixReshape(self, nums, r, c):
    """
    :type nums: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """
    res = []
    r1 = len(nums)
    c1 = len(nums[0])
    if r * c != r1 * c1:
      return nums
    else:
      index = 0
      for i in range(r):
        temp = []
        for j in range(c):
          temp.append(nums[index // c1][index % c1])
          index += 1
        res.append(temp)
      return res

  def matrixReshape2(self, nums, r, c):
    res = []
    r1 = len(nums)
    c1 = len(nums[0])
    if r * c != r1 * c1:
      return nums
    else:
      flatted = []
      for x in nums:
        flatted += x
      for i in range(0, len(flatted), c):
        res.append(flatted[i:i + c])
    return res


s = Solution()
nums = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
print(s.matrixReshape2(nums, 1, 12))
