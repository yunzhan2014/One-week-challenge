from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        res = [[0]*n for i in range(m)]

        for i in range(m):
            for j in range(n):
                print(f"mat[i][i] is {mat[i][j]}")
                print(f"res[i][i] is {res[i][j]}")
                if mat[i][j] != 0:

                    depth = 0
                    que = [[i, j]]
                    directions = [[0,1],[0,-1],[1,0],[-1,0]]
                    while que:
                        print(que)
                        depth += 1
                        cur_x, cur_y = que.pop(0)
                        for x,y in directions:
                            new_x = cur_x + x
                            new_y = cur_y + y
                            
                            if 0<= new_x < m and 0<= new_y < n: 
                                if mat[new_x][new_y]==0:
                                    print(f"+++++++++{res[i][j]}")
                                    print(f"res[i][j] [i] is {i} [j] is {j}")
                                    print(f"Before res[i][j] is {res}")
                                    res[i][j] = res[i][j] +depth
                                    print(f"After res[i][j] is {res}")
                                    
                                    que.clear()
                                    break
                                else:
                                    print("---------")
                                    que.append([new_x,nex_y])
                            else:
                                print("===========")
                                continue
            
        return res

if __name__ == "__main__":
    s = Solution()
    case1 = [[0,0,0],[0,1,0],[0,0,0]]
    case2 = [[0,0,0],[0,1,0],[1,1,1]]

    s.updateMatrix(case1)