from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
            # 求岛的长度和宽度
            m = len(grid)
            n = len(grid[0])
            
            visited = []
            max_island = 0
            count = m*n 

            for i in range(m):
                print(f"==============={i}+++++++++")
                for j in range(n):
                    # 当前的坐标
                    cur_l = [i, j]
                    print(f"---------------{cur_l}++++++++")
                    # 如果来过这个坐标，则不再访问
                    if cur_l in visited:
                        print("before continue")
                        continue
                        print("after continue")
                    # 如果没来过这个坐标且坐标为0，则加入访问列表
                    elif grid[cur_l[0]][cur_l[1]] == 0:
                        visited.append([i,j])
                    # 如果没来过，坐标也不是0，那么坐标肯定是1，则开始进行搜索
                    else:
                        print(f"_____--{cur_l}")
                        visited.append(cur_l)
                        que = []
                        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                        que.append(cur_l)
                        cur_island = 1
                        while que:
                            x1, y1 = que.pop(0)
                            print(f"-----------{x1},{y1}----------")
                            for x,y in directions:
                                # 既在边界内，又等于1，这里不再确实是否访问过了，因为不存在这种情况
                                if 0 <= x+x1 < m  \
                                and 0<= y+y1 < n \
                                and grid[x+x1][y+y1] == 1 \
                                and [x+x1, y+y1] not in visited:
                                    cur_island += 1
                                    que.append([x+x1, y+y1])
                                    visited.append([x+x1, y+y1])
                        print(f"++++++{cur_island}+++")
                        max_island = max(cur_island, max_island)
            return max_island
                        
if __name__ == "__main__":
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    grid2 = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
    grid3 = [[1,0,0,0,1,1,1,1,0,1,0,0,1,1,1,0,0,0,1,0,1,0,0,1,1,1,0],[1,1,1,0,0,0,1,0,0,1,0,1,1,0,0,0,1,0,0,0,1,0,1,0,1,0,1],[1,0,1,0,1,0,0,0,0,1,0,1,1,1,0,0,0,1,0,0,1,1,0,1,1,0,0],[0,0,0,1,1,1,0,0,0,1,1,1,0,1,1,0,0,1,0,1,0,1,1,0,1,0,0],[1,0,0,0,1,1,0,0,1,0,0,1,1,0,0,1,0,1,1,0,0,1,1,1,0,1,1],[0,0,1,1,1,1,0,1,1,0,1,0,0,0,1,1,0,0,0,1,1,0,1,1,0,1,1]]
    s = Solution()
    result = s.maxAreaOfIsland(grid3)
    print(result)




