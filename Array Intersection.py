import sys

def intersections(arr1, n, arr2, m) :
    l=[]
    for ele in arr1:
        if ele in arr2:
            l.append(ele)
            arr2.remove(ele)
    for i in l:
        print(i,end=" ")
    
    #Your code goes here























#Taking Input Using Fast I/O
def takeInput() :
    n = int(sys.stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, sys.stdin.readline().strip().split(" ")))
    return arr, n


#main
t = int(sys.stdin.readline().strip())

while t > 0 :
    arr1, n = takeInput()
    arr2, m = takeInput()
    

    intersections(arr1, n, arr2, m)
    print()

    t -= 1
