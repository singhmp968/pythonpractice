def mergsort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        mergsort(left)
        mergsort(right)
        i=0
        j=0
        k=0
        leftlen=len(left)
        rightlen=len(right)
        while i<leftlen and j<rightlen:
            if left[i]<right[j]:
                arr[k]=left[i]
                i=i+1
            else:
                arr[k]=right[j]
                j=j+1
            k=k+1
        while i<leftlen:
            arr[k]=left[i]
            i=i+1
            k=k+1
        while j<rightlen:
            arr[k]=right[j]
            j=j+1
            k=k+1
n=int(input())
arr = list(map(int, input().split()))
mergsort(arr)
for i in range(0 , len(arr),1):
    print(arr[i],end=' ')
