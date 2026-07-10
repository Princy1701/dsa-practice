def linear_search(arr,target):
    indices =[]
    for i in range(0,len(arr)-1):
        if arr[i]==target:
            indices.append(i)
    return indices
arr=[2,3,4,7,1,8,2,5,7,5]
target =2
index=linear_search(arr,target)
print(index)