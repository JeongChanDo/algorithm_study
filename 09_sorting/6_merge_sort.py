def merge_sort(seq):
    """
    1) pop을 이용한 병합 정렬
    """
    if len(seq) < 2:
        return seq
    mid = len(seq) // 2
    left, right = seq[:mid], seq[mid:]
    if len(left) > 1:
        left = merge_sort(left)
    if len(right) > 1:
        right = merge_sort(right)
    
    res = []
    while left and right:
        if left[-1] >= right[-1]:
            res.append(left.pop())
        else:
            res.append(right.pop())
    res.reverse()
    return (left or right) + res

def merge_sort_seq(seq):
    if len(seq) < 2:
        return seq
    mid = len(seq) // 2
    left = merge_sort_seq(seq[:mid])
    right = merge_sort_seq(seq[mid:])
    return merge(left, right)

def merge(left, right):
    if not left or not right:
        return left or right
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if left[i:]:
        result.extend(left[i:])
    if right[j:]:
        result.extend(right[j:])
    return result

def test_merge_sort():
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 6, 2]
    seq_sorted = sorted(seq)
    assert(merge_sort(seq) == seq_sorted)
    assert(merge_sort_seq(seq) == seq_sorted)
    print("test passed")

if __name__ == "__main__":
    test_merge_sort()