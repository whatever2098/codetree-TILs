def is_palindrome(s):
    def helper(left, right):
        if left >= right:
            return True
        if s[left] != s[right]:
            return False
        return helper(left + 1, right - 1)

    return helper(0, len(s) - 1)
