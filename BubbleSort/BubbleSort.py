# BubbleSort algorythm

def bs(a):
    i = 0
    while i < len(a) - 1:
        j = 0
        while j < len(a) - 1 - i:
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
            j += 1
        i += 1

    print(a)

list = [1,4,2,6,3,14,65,345,43,1,9]
print(bs(list))