class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s: return None
        dict1 = {}
        result = 0
        for i,v in enumerate(s):
            if v in dict1:
                dict1[v] = -1
            else:
                dict1[v] = i
        index_list = []
        for index in dict1.values():
            if index >=0:
                index_list.append(index)
                result = min(result, index)
            else:
                continue
        print(f'The index list is {index_list}')
        return min(index_list) if index_list else -1

if __name__ == "__main__":
    case1 = "leetcode"
    case2 = "loveleetcode"
    case3 = ''
    case4 = 'l'
    s = Solution()
    print(s.firstUniqChar(case1))
    print(s.firstUniqChar(case2))