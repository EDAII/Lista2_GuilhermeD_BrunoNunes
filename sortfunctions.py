def selectionSort(input):
    for i in range(len(input)):
        min_idx = i
        for j in range(i + 1, len(input)):
            if input[min_idx] > input[j]:
                min_idx = j

        input[i], input[min_idx] = input[min_idx], input[i]

    return input



def quicksort(arr):
   if len(arr) <= 1: return arr
   m = arr[0]
   return quicksort(filter(lambda i,j=m: i<j, arr)) + \
          filter(lambda i,j=m: i==j, arr) + \
          quicksort(filter(lambda i,j=m: i>j, arr))
