__author__ = 'archmage'
# Code for Lectures 2, 3 and 4 of MIT 6.006, Fall 2011 OCW


def main():
    print "In Main method"
    # ins_sort([x for x in xrange(1000, 0, -1)])
    merge_sort([x for x in xrange(10000, 0, -1)])
    heap_sort([x for x in xrange(10000, 0, -1)])
    return


# Insertion sort code to compare performance with merge sort
def ins_sort(a):
    l = len(a)
    for x in xrange(1, l):
        t = x
        for y in xrange(x - 1, -1, -1):
            if a[t] < a[y]:
                a[t], a[y] = a[y], a[t]
                t = y
            else:
                break
    return a


def merge_sort(a):
    l = len(a)
    if l == 1:
        return a
    a_l = merge_sort(a[:l / 2])
    a_r = merge_sort(a[l / 2:])
    return merge(a_l, a_r)


def merge(a_l, a_r):
    l = 0
    r = 0
    l1 = len(a_l)
    l2 = len(a_r)
    arr = []
    while (l < l1) and (r < l2):
        if a_l[l] < a_r[r]:
            arr.append(a_l[l])
            l += 1
        elif a_l[l] == a_r[r]:
            arr.append(a_l[l])
            arr.append(a_r[r])
            l += 1
            r += 1
        else:
            arr.append(a_r[r])
            r += 1
    # Now, append remainder of pending array
    if l < l1:
        for x in xrange(l, l1):
            arr.append(a_l[x])
    if r < l2:
        for x in xrange(r, l2):
            arr.append(a_r[x])
    return arr


# Now, moving on to Heap Sort. We'll need the following methods:
# build_heap
# max_heapify
# extract_max
# insert


# max_heapify assumes that the children of a[i] are already max heaps
def max_heapify(a, i, l):
    if 2*i + 1 >= l:
        return
    elif 2*i + 2 >= l:
        if a[i] < a[2*i + 1]:
            a[i], a[2 * i + 1] = a[2 * i + 1], a[i]
        return
    if not (a[i] >= a[2 * i + 1] and a[i] >= a[2 * i + 2]):
        if a[2 * i + 1] >= a[2 * i + 2]:
            a[i], a[2 * i + 1] = a[2 * i + 1], a[i]
            max_heapify(a, 2 * i + 1, l)
        else:
            a[i], a[2 * i + 2] = a[2 * i + 2], a[i]
            max_heapify(a, 2 * i + 2, l)
    return


def build_heap(a):
    for x in xrange(len(a) / 2, -1, -1):
        max_heapify(a, x, len(a))
    return a


def heap_sort(a):
    a = build_heap(a)
    l = len(a)
    for x in xrange(1, l):
        a[0], a[-x] = a[-x], a[0]
        max_heapify(a, 0, l-x)
    return a

if __name__ == "__main__":
    import cProfile
    cProfile.run("main()")