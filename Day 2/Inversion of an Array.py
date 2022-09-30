
def merge(arr, temp, start, mid, end):
    inv_count = 0
    i = start
    j = mid+1
    k = start
    while i<=mid and j<=end:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1
            
    while i<=mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    while j<=end:
        temp[k] = arr[j]
        j += 1
        k += 1
        
    for i in range(start, end+1):
        arr[i] = temp[i]
    
    return inv_count

def mergeSort(arr, temp, start, end):
    inv_count = 0
    if start < end:
        mid = start + (end - start)//2
        inv_count += mergeSort(arr, temp, start, mid)
        inv_count += mergeSort(arr, temp, mid+1, end)
        inv_count += merge(arr, temp, start, mid, end)
    return inv_count

def getInversions(arr, n) :
    temp = [0]*n
    return mergeSort(arr,temp, 0, n-1)
