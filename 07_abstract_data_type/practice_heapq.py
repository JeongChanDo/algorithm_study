import heapq


"""
우선순위 큐 priority queue
- 스택, 큐와 비슷하나 항목마다 우선순위를 가짐.
- 우선순위 같은 경우 큐 순서 따름.
- 힙으로 구현

힙 heap
- 노드의 값이 하위보다 작거나 큰 이진트리
"""
list1 = [4, 6, 8, 1]

# heapify : 리스트를 힙으로 변환
heapq.heapify(list1)
print(list1)

h = []

heapq.heappush(h, (1, "food"))
heapq.heappush(h, (2, "have fun"))
heapq.heappush(h, (3, "work"))

print(h)

#heappop : 가장 작은 항목 제거, 반환
print(heapq.heappop(list1))
print(list1)

#heappushpop(heap, item) : 새항목을 힙에 추가 후 가장 작은걸 반환
print(heapq.heappushpop(list1, 5))
print(list1)

