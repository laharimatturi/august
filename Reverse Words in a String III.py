class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        left = 0

        for i in range(len(s) + 1):
            if i == len(s) or s[i] == ' ':
                right = i - 1

                while left < right:
                    s[left], s[right] = s[right], s[left]
                    left += 1
                    right -= 1

                left = i + 1

        return ''.join(s)
