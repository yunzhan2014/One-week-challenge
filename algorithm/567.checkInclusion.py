class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        flag = False
        for i,v in enumerate(s2):
            for k in s1:
                if k != v:
                    flag = False
                    break;
                else:
                    flag = True
            if flag: break;
        return flag
            

if __name__ == "__main__":
    s = Solution()
    case1 = ["ab", "eidbaooo"]
    case2 = ["ab", "eidabooo"]
    print(s.checkInclusion(case1[0], case1[1]))
    print(s.checkInclusion(case2[0], case2[1]))
