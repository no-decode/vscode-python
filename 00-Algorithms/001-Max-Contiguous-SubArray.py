def kadane_max_subarray(arr):
    current_max = arr[0]
    global_max = arr[0]
    start_index = 0
    end_index = 0
    temp_start_index = 0

    for i in range(1, len(arr)):
        if arr[i] > current_max + arr[i]:
            temp_start_index = i
            current_max = arr[i]
        else:
            current_max = current_max + arr[i]

        if current_max > global_max:
            global_max = current_max
            start_index = temp_start_index
            end_index = i

    max_subarray = arr[start_index:end_index + 1]
    return global_max, max_subarray

# Example usage:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, subarray = kadane_max_subarray(arr)
print("Maximum sum:", max_sum)
print("Maximum sum subarray:", subarray)
arr = [-8,-2]
max_sum, subarray = kadane_max_subarray(arr)
print("Maximum sum:", max_sum)
print("Maximum sum subarray:", subarray)

