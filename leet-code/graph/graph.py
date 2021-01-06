# V = 4
# def colorGraph(G, color, pos, c):  
      
#     if color[pos] != -1 and color[pos] != c:  
#         print("thissss")
#         return False 
          
#     # color this pos as c and all its neighbours and 1-c  
#     color[pos] = c  
#     ans = True 
#     for i in range(0, V):  
#         if G[pos][i]: 
#             print("check i ",pos, i) 
#             if color[i] == -1:  
#                 ans &= colorGraph(G, color, i, 1-c)
#                 print("pos ", pos)  
#                 print(i)
#             print(color)
#             if color[i] !=-1 and color[i] != 1-c: 
#                 print("COloer ",pos,i) 
#                 return False 

#         if not ans:  
#             return False 
       
#     return True 
   
# def isBipartite(G):  
      
#     color = [-1] * V  
          
#     #start is vertex 0  
#     pos = 0 
#     # two colors 1 and 0  
#     return colorGraph(G, color, pos, 1)  
  
# if __name__ == "__main__":  
   
#     G = [[0, 1, 0, 1],  
#          [1, 0, 1, 1],  
#          [0, 1, 0, 1],  
#          [1, 1, 1, 0]]  
       
#     if isBipartite(G): print("Yes")  
#     else: print("No")

# a = [1,3,5,6,7]
# b = [1,10]

# all_ = all(True, False)

from collections import defaultdict
arr = defaultdict(list)
seen = [[False for x in range(5)] for y in range(4)] 
#seen[2][1] = 20
seen[0][0]= True
ans = 0
ans += 1 if True else ans
print(ans)