def quick_sort_cache(seq):
    if len(seq) < 2:
        return seq
    # pivot index
    ipivot = len(seq)//2
    pivot = seq[ipivot]

    before = [x for i, x in enumerate(seq) if x <= pivot and i != ipivot]
    after = [x for i, x in enumerate(seq) if x > pivot and i != ipivot]
    return quick_sort_cache(before) + [pivot] + quick_sort_cache(after)

def partition_devided(seq):
    pivot, seq = seq[0], seq[1:]
    before = [x for x in seq if x <=pivot]
    after = [x for x in seq if x > pivot]
    return before, pivot, after

def quick_sort_cache_devided(seq):
    if len(seq) < 2:
        return seq
    before, pivot, after = partition_devided(seq)
    return quick_sort_cache_devided(before) + [pivot] + quick_sort_cache_devided(after)

def test_quick_sort():
    seq = [3, 5, 2, 6, 8, 1, 0, 3, 5, 7, 2]
    assert(quick_sort_cache(seq) == sorted(seq))
    assert(quick_sort_cache_devided(seq) == sorted(seq))
    print("test passed")

if __name__ == "__main__":
    test_quick_sort()