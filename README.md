# ps
daily problem solving





----
python 값 제거 할 때 주의사항
```
a = [1, 2, 3]
remove_list = []
for i in range(len(a)):
  if a[i] == 3:
    #p1 del a[i] --> range가 꼬임.
    #p2 remove_list.append(i)
    remove_list.append(a[i])
for r in remove_list:
  #p2 del a[r] --> index가 꼬임.
  a.remove(r) #--> 첫 번쨰 원소만 삭제. 값이 유일 할 때 허용
```
----
queue.PriorityQueue 보다 heapq가 더 빠르다.

```
import heapq
h = []
heapq.heappush(h, 1)
heapq.heappush(h, 3)
heapq.heappush(h, 2)
val = heapq.heappop(h)
val = heapq.heappop(h)
val = heapq.heappop(h)
# or
h = [1, 3, 2]
heapq.heapify(h)
```

----

[DEBUG]
devide by zero
stack overflow
