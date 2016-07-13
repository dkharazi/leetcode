# Kth Smallest Element in Unsorted Array

def kthSmallest(a, k):
    a1 = a[:]

    for i in xrange(k):
        kthsmallest = min(a1)
        a1.remove(kthsmallest)

    return kthsmallest

def kthSmallest2(a, k):
    return sorted(a)[k-1]

if __name__ == "__main__":
    a = [8,0,4,1,0,3,2,9]
    k = 3

    print kthSmallest(a, k)
    print kthSmallest2(a, k)
