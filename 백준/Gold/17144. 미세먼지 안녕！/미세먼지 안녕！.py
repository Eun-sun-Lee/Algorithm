# 시간초과 난 코드 

import sys 
from collections import deque 

r, c, t = map(int, sys.stdin.readline().split())
graph = []
# rNorth = []
# cNorth = []
# rSouth = []
# cSouth = [] 
north = deque()
south = deque()


clearNorth= [0,0]
clearSouth= [0,0]

dy = [1, 0, -1, 0, 0]
dx = [0, 1, 0, -1, 0]

first = False
for i in range(r):
    l = list(map(int, sys.stdin.readline().split()))
    if l[0] == -1:
        if first == False:
            first = True
            clearNorth[0] = i 
        else:
            clearSouth[0] = i

    graph.append(l)

# print(graph)
# print(clearNorth, clearSouth)
def spreadDust(clearNorth, clearSouth, graph, r, c, t):
    for ii in range(t):
        newGraph = [[0 for _ in range(c)] for _ in range(r)]
        newNorth = deque()
        newSouth = deque()
        absorbDust = False 
    
        for i in range(r):
            for j in range(c): 
                if graph[i][j] != 0 and graph[i][j] != -1:
                    newDust = graph[i][j] // 5
                    remainDust = graph[i][j]
                    absorbDust = False
                    for k in range(5):
                        ny = dy[k] + i 
                        nx = dx[k] + j 
                        if 0 <= ny <= r - 1 and 0 <= nx <= c - 1:
                            # if (ny, nx) == clearNorth or (ny, nx) == clearSouth: continue 
                            if ny == clearNorth[0]:
                                if nx == 0: continue 
                                if nx == c - 1: # 공기 청정기이므로 확산 X
                                    ny -= 1
                                else: 
                                    nx += 1
                            elif ny == clearSouth[0]:
                                if nx == 0: continue # 공기 청정기이므로 확산 X
                                if nx == c - 1:
                                    ny += 1
                                else: 
                                    nx += 1
                            elif ny == 0:
                                if nx == 0:
                                    ny += 1
                                else:
                                    nx -= 1
                            elif ny == r - 1:
                                if nx == 0:
                                    ny -= 1
                                else:
                                    nx -= 1
                            elif ny < clearNorth[0] - 1:
                                if nx == 0:
                                    ny += 1
                                elif nx == c - 1: # 디버깅 3
                                    ny -= 1 
                            elif ny == clearNorth[0] - 1:
                                if nx == 0: 
                                    # 디버깅1
                                    absorbDust = True 
                                    ny += 1
                                    # continue 
                                elif nx == c - 1: # 디버깅 3
                                    ny -= 1
                            elif ny == clearSouth[0] + 1:
                                if nx == 0: 
                                    # 디버깅1
                                    absorbDust = True 
                                    ny -= 1
                                elif nx == c - 1: # 디버깅 3
                                    ny += 1
                            else: # ny > clearSouth[0] + 1:
                                if nx == 0:
                                    ny -= 1
                                elif nx == c - 1: # 디버깅 3
                                    ny += 1
                            
                            if k < 4:
                                if absorbDust == True:
                                    # newGraph[ny][nx] = 0
                                    absorbDust = False 
                                else:
                                    newGraph[ny][nx] += newDust                                    
                                remainDust -= newDust # 디버깅 4 (absortDust = True여도 확산은 되고, 공기청정기에 흡수된 것이므로 빼줘야함 )
                            else:
                                if absorbDust == True:
                                    # newGraph[ny][nx] = 0
                                    absorbDust = False 
                                else:
                                    newGraph[ny][nx] += remainDust 
                    # print(remainDust, newDust)
        
        graph = newGraph
        # print(newGraph)
        # print("t: ", ii, end=" ")

    #     total_sum = sum(sum(row) for row in graph)
    #     print(total_sum)

    #     for i in range(r):
    #         print(newGraph[i])

    # print(graph)
    total_sum = sum(sum(row) for row in graph)
    print(total_sum)

spreadDust(clearNorth, clearSouth, graph, r, c, t)
