import functools


class Solution:
  def largestNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: str
    """
    num = [str(x) for x in nums]
    num.sort(key=functools.cmp_to_key(
        lambda x, y: int(str(x) + str(y)) - int(str(y) + str(x))), reverse=True)
    return ''.join(num).lstrip('0') or '0'


s = Solution()
print(s.largestNumber([3, 30, 34, 5, 9]))
