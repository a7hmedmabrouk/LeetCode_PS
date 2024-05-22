class Solution(object):
    def partition(self, s):
        \\\
        :type s: str
        :rtype: List[List[str]]
        \\\
        def isPalindrome(sub):
            return sub == sub[::-1]
        
        def backtrack(start, path):
            if start == len(s):
                result.append(list(path))
                return
            for end in range(start, len(s)):
                if isPalindrome(s[start:end+1]):
                    path.append(s[start:end+1])
                    backtrack(end + 1, path)
                    path.pop()
        
        result = []
        backtrack(0, [])
        return result