class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        len1, len2 = len(s), len(t)
        if len1 != len2:
            return False
        elif len1 == 1:
            if s!= t:
                return False
            else:
                return True
        else:
            dict1 = {}
            dict2 = {}
            for i, j in zip(s, t):
                if i in dict1:  
                    dict1[i] += 1
                else:
                    dict1[i] = 1
                if j in dict2:
                    dict2[j] += 1
                else:
                    dict2[j] = 1
            print(f"-----{dict1}----")
            print(f"+++++{dict2}++++")
            if dict2 == dict1:
                return True
            else:
                return False


if __name__ == "__main__":
    case1 = ["anagram", "nagaram"]
    s = Solution()
    s.isAnagram(case1[0], case1[1])

