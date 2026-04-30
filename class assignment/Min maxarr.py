def find_min_max(arr):
        min = arr[0]
        max = arr[0]
        for num in arr:
            if num < min:
                min = num
            elif num> max:
                max = num
        return [min , max]
arr = [1, 4, 3, 5, 8, 6]
print(find_min_max(arr))