def is_palindrome_array(arr):
    for num in arr:
        if str(num) != str(num)[::-1]:
            return False
    return True