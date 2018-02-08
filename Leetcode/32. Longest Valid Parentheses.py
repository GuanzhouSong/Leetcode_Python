class Solution:
  def longestValidParentheses(self, s):
    """
    :type s: str
    :rtype: int
    """
    st = []
    res = 0
    for i in range(len(s)):
      if s[i] == '(':
        st.append(i)
      else:
        if len(st) > 0:
          if s[st[-1]] == '(':
            st.pop()
          else:
            st.append(i)
        else:
          st.append(i)
    if len(st) <= 0:
      return len(s)
    else:
      b, a = 0, len(s)
      while len(st) > 0:
        b = st.pop()
        res = max(res, a - b - 1)
        a = b
      res = max(res, a)
    return res


so = Solution()
s = "(()"
print(so.longestValidParentheses(s))
