# A SAVOLNING JAVOBI
# a=int(input())
# b=a/2
# if a%2==0 and b%2==0:
#   print("YES")
# else:
#   print("NO")



# B SAVOLNING JAVOBI
# a=int(input())
# b=list(map(int,input().split()))
# m=max(b)
# c=0
# for i in b:
#     if i*2<m:
#         c+=1
# print(c)




# C SAVOLNING JAVOBI
# k = int(input())

# teshik = False
# qonunlar = []

# for i in range(k):
#     j = list(map(int, input().split()))
#     qonunlar.append(j)

# for j in range(0, k - 1):
#     if (qonunlar[j][1] * ( 1 - (qonunlar[j][2] / 100)) >= qonunlar[(j + 1)][0] * (1 - (qonunlar[(j + 1)][2] / 100))):
#         teshik = True
#         print("YES")
#         break

   
# if not teshik:
#     print("NO")




# D SAVOLNING JAVOBI
# k=int(input())
# l=1
# r=2*10**18
# while l<r:
#     m=(l+r)//2
#     p=m.bit_length()
#     if m-p>=k:
#         r=m
#     else:
#         l=m+1
# print(l)

# YOKI
# k=int(input())
# p=1
# while (p<=k):
#   k+=1
#   p*=2
# print(k)


# E SAVOLNING JAVOBI


# import sys

# # Recursion limitini oshiramiz
# sys.setrecursionlimit(10**6)


# def solve():
#     input = sys.stdin.read
#     data = input().split()

#     if not data:
#         return

#     N = int(data[0])

#     edges = []
#     adj = {}

#     idx = 1
#     for i in range(N):
#         u = int(data[idx])
#         v = int(data[idx + 1])
#         idx += 2
#         edges.append((u, v))

#         if u not in adj:
#             adj[u] = []
#         if v not in adj:
#             adj[v] = []

#         adj[u].append((v, i))
#         adj[v].append((u, i))

#     ans = ['a'] * N
#     visited_nodes = set()
#     visited_edges = set()

#     max_heroes = 0

#     for start_node in list(adj.keys()):
#         if start_node in visited_nodes:
#             continue

#         # Komponentadagi tugunlar va qirralarni yig'amiz
#         component_nodes = []
#         component_edges = []

#         stack = [start_node]
#         visited_nodes.add(start_node)

#         while stack:
#             curr = stack.pop()
#             component_nodes.append(curr)

#             for neighbor, edge_idx in adj[curr]:
#                 if edge_idx not in visited_edges:
#                     visited_edges.add(edge_idx)
#                     component_edges.append(edge_idx)

#                 if neighbor not in visited_nodes:
#                     visited_nodes.add(neighbor)
#                     stack.append(neighbor)

#         V = len(component_nodes)
#         E = len(component_edges)

#         # Maksimal qahramonlar soni: min(V, E)
#         heroes_cnt = min(V, E)
#         max_heroes += heroes_cnt

#         # Endi kartalarni to'g'ri yo'naltiramiz
#         # Agar sikl bo'lsa, xohlagan tugun ildiz.
#         # Agar daraxt bo'lsa (E = V-1), tanlanmaydigan 1 ta tugunni ildiz qilib olamiz.

#         # Qirralar bo'yicha kichik daraxt (DFS tree) tuzamiz
#         tree_adj = {node: [] for node in component_nodes}
#         for e_idx in component_edges:
#             u, v = edges[e_idx]
#             tree_adj[u].append((v, e_idx))
#             tree_adj[v].append((u, e_idx))

#         used_edges = set()
#         root = component_nodes[0]

#         # DFS orqali ildizdan pastga yo'naltiramiz
#         def dfs(u, p_edge):
#             for v, e_idx in tree_adj[u]:
#                 if e_idx in used_edges:
#                     continue
#                 used_edges.add(e_idx)

#                 # e_idx kartasi u va v ni bog'laydi
#                 if edges[e_idx][0] == v:
#                     ans[e_idx] = 'a'  # v ni tanladik
#                 else:
#                     ans[e_idx] = 'b'  # v ni tanladik

#                 dfs(v, e_idx)

#         dfs(root, -1)

#     print(max_heroes)
#     print("".join(ans))


# if __name__ == "__main__":
#     solve()









# 10-SINF
# A SAVOLNING JAVOBI

# a,b,c,d=map(int,input().split())
# vaqt=d*60
# if a+b<=vaqt or a+c<=vaqt or c+b<=vaqt:
#   print("YES")
# else:
#   print("NO")


# B SAVOLNING JAVOBI


# a,b,c=map(int,input().split())
# x,y=map(int,input().split())
# if x<a:
#   somsa=x%a
# else:
#   somsa=a
# if y<b:
#   piyola=y%b
# else:
#   piyola=b
# if x>a and y>b:
#   ikkalasi=min((x-a),(y-b))
# else:
#   ikkalasi=0
# print(somsa+piyola+ikkalasi)
  


C SAVOLNING JAVOBI















