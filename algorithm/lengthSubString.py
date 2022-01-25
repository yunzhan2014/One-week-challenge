class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = []
        lookup_len = []
        for i,v in enumerate(s):
            if v in lookup:
                lookup_index = lookup.index(v)
                lookup_len.append(len(lookup))
                lookup = lookup[lookup_index+1:]
                lookup.append(v)
            else:
                lookup.append(v)
        return max(lookup_len)
    
if __name__ == "__main__":
    s = Solution()
    case1 = 'abcabcdabcdefabc'
    print(s.lengthOfLongestSubstring(case1))