#Given an array A of N integers. Count the number of elements that have at least 1 elements greater than itself.

a=[1,4,6,2,7,9,3,9,3]
n = len(a)
print(n)
max_el = a[0]
max_el_count = 0
for i in range(n):
    if a[i] >max_el:
        max_el = a[i]
        max_el_count = 1
        print(max_el,max_el_count)
    elif a[i]==max_el:
        max_el_count+=1
        print(max_el, max_el_count)
print(n - max_el_count)

