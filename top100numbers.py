# Problem: Retrieving the max top 100 numbers from one hundred million of numbers

# Algorithm:
# Run them all through a min-heap of size 100:
# for each input number k, replace the current min m with max(k, m).
# Afterwards the heap holds the 100 largest inputs.

import heapq

def funnel(k, numbers):
    if k == 0:
        return []
    heap = numbers[:k]
    # heapify: Transform list into a heap, in-place, in linear time.
    heapq.heapify(heap)
    for num in numbers[k:]:
        # heappushpop: Push item on the heap, then pop and return the smallest item from the heap.
        # ref: https://gengwg.blogspot.com/2018/04/heapq-heap-queue-algorithm.html
        heapq.heappushpop(heap, num)
        #if heap[0] < num:
            #heapq.heapreplace(heap, num)
    return heap

if __name__ == '__main__':
    print funnel(4, [3,1,4,1,5,9,2,6,5,3,5,8])
    import random
    # nums = [i for i in range(100)]
    nums = [random.randint(0,100) for i in range(100)]
    print funnel(10, nums)

