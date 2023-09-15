
def is_min_heap(heap):

    # trivial cases
    if len(heap) <=1:
        return True

    if len(heap) == 2:
        return heap[0] < heap[1]

    # there is no need to check the leaf nodes
    num_items = (len(heap) - 2) // 2 + 1

    for i in range(num_items):
        # we have to check the heap property
        # the parent must be smaller than the children (min heap)
        if heap[i] > heap[(2*i)+1] or heap[i] > heap[(2*i)+2]:
            return False

    return True

if __name__ == '__main__':
    n = [1, 2, 3, 5, -4]
    print(is_min_heap(n))
