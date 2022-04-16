import heapq
pq = []
arr = [("b", 3, 0, ""),("a", 1, -100, ""),("c", 1000, - 1, "")]
for n in arr:
    heapq.heappush(pq,n)

print("element at top = ", pq[0])
print("check the heapq : ", pq)