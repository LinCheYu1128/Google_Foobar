import heapq

# Create an empty list
heap = []

# Use heapq to push elements onto the heap
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
print 'Heap after push operations:', heap

min_element = heapq.heappop(heap)
print 'Popped element:', min_element
print 'Heap after pop operation:', heap