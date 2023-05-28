arr = input("Please input a series of numbers: ")
arr = [int(n) for n in arr.split()] #分割字串
arr1=arr[:]
arr2=arr[:]
for i in range(1, len(arr1)): 
    key = arr1[i] 
    j = i-1
    while j >=0 and key < arr1[j] : 
        arr1[j+1] = arr1[j] 
        j -= 1
    arr1[j+1] = key 
print("The result of insertion sort: ",arr1) #插入排序
for i in range(len(arr2)):
    for j in range(0, len(arr2)-i-1):
        if arr2[j] > arr2[j+1] :
            arr2[j], arr2[j+1] = arr2[j+1], arr2[j]
print("The result of insertion sort: ",arr2) #泡沫排序
Continue = 'y'
while Continue == 'y' :
    find = int(input("\nPlease specify a number: "))
    a=0
    low = 0
    high = len(arr1)-1
    while low <= high: #二元搜尋
        mid = int((low + high) / 2)
        if find == arr1[mid]:
            print("The target number {} found by binary search at location {}".format(find,mid+1))
            a=1
            break
        elif find > arr1[mid]:
            low = mid + 1
        else:
            high = mid - 1
    if a==0:
        print("The target number {} cannot be found by binary search".format(find))
    Continue = input("Want to keep going (y/n): ")