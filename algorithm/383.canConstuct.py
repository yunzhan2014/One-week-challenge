class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        len1, len2 = len(ransomNote), len(magazine)
        dict_hash = {}
        for char in magazine:
            if char in dict_hash:
                dict_hash[char] += 1
            else:
                dict_hash[char] = 1
        for i in ransomNote:
            if i in dict_hash:
                if dict_hash[i] > 1:
                    dict_hash[i] -= 1
                else:
                    dict_hash.pop(i)
            else:
                return False
        return True

   