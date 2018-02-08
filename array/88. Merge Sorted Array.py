class Solution:
  def merge(self, nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    cur_index = m + n - 1
    while m >= 1 or n >= 1:
      if m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
          nums1[cur_index] = nums1[m - 1]
          m -= 1
          cur_index -= 1
          continue
        else:
          nums1[cur_index] = nums2[n - 1]
          n -= 1
          cur_index -= 1
          continue
      else:
        if m > 0:
          nums1[cur_index] = nums1[m - 1]
          m -= 1
          cur_index -= 1
          continue
        else:
          nums1[cur_index] = nums2[n - 1]
          n -= 1
          cur_index -= 1
          continue


s = Solution()
num1 = [0]
num2 = [1]
s.merge(num1, 0, num2, 1)
print(num1)
