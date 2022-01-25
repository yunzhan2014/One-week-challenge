from typing import List

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        if image[sr][sr] == newColor:
            return image
        x_len = len(image)
        y_len = len(image[0]) 
        cur_color = image[sr][sr]
        que = []
        que.append([sr,sc])
        direction = [[0,1], [0,-1], [1,0], [-1,0]]
        count = x_len*y_len
        while que:
            count -= 1
            # 取出来染色
            print(str(que))
            print(f'============{len(que)}=========')
            h = que.pop(0)
            image[h[0]][h[1]] = newColor
            
            # 进行广度优先搜索
            for d in direction:
                v = [x+y for x,y in zip(h, d)]
                if 0<=v[0]<x_len and 0<=v[1]<y_len and image[v[0]][v[1]] == cur_color:
                    que.append(v)
            print(f'++++++++++++{len(que)}=========')
            if count <= 0:
                break
        return image
    

    def floodFilldfs(self, image, sr, sc, newColor):
        if image[sr][sr] == newColor:
            return image
        x_len = len(image)
        y_len = len(image[0]) 
        cur_color = image[sr][sr]
        stack = []
        stack.append([sr,sc])
        direction = [[0,1], [0,-1], [1,0], [-1,0]]
        count = x_len*y_len
        while stack:
            count -= 1
            # 取出来染色
            h = stack.pop()
            image[h[0]][h[1]] = newColor
            
            # 进行广度优先搜索
            for d in direction:
                v = [x+y for x,y in zip(h, d)]
                if 0<=v[0]<x_len and 0<=v[1]<y_len and image[v[0]][v[1]] == cur_color:
                    stack.append(v)
            print(f'++++++++++++{len(stack)}=========')
            if count <= 0:
                break
        return image

            
if __name__ == "__main__":
    s = Solution()
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    newColor = 2
    print(s.floodFilldfs(image, sr, sc, newColor))

            
