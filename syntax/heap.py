import heapq
a = (-1, 2)
b = (0, 1)
c = (0, 3)
d = (0, 4)
e = (0, 5)
heap = []
heapq.heappush(heap, a)
heapq.heappush(heap, b)
heapq.heappush(heap, c)
heapq.heappush(heap, d)
heapq.heappush(heap, e)

while heap:
    print(heap.pop())