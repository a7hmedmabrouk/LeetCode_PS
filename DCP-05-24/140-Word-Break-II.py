class Solution(object):
    def wordBreak(self, s, wordDict):
        \\\
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        \\\
        word_set = set(wordDict)
        memo = {}

        def dfs(s):
            if s in memo:
                return memo[s]
            if not s:
                return []
            
            res = []
            for word in word_set:
                if s.startswith(word):
                    if len(word) == len(s):
                        res.append(word)
                    else:
                        result_of_the_rest = dfs(s[len(word):])
                        for item in result_of_the_rest:
                            res.append(word + ' ' + item)
            
            memo[s] = res
            return res

        return dfs(s)