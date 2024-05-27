# 1. Generate an infinite Fibonacci series using a generator.
# 2. Sort a list without using the keyword Sort.
# 3. Check whether a string is palindrome or not?
# 4. Sort a dictionary dict comprehension.
# 5. Find the pair with a given number in a list. two elements sum to the given number.
# 6. Create a Fibonacci series using recursion.
# 7. String manipulation. "The Sky is Blue" to "Blue is The Sky"
# 8. Find the maximum repeated character in a string without having o(n2) complexity.
# 9. Find a maximum and minimum value in a List without using any predefined function.
def fibonacci(n):
    if n <= 0:
        return None
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def fib(n):
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a+b
print(list(fib(10)))
print(list(map(fibonacci, range(1, 11))))

def check_if_palindrome(input_str):
    if input_str == input_str[::-1]:
        return True
    else:
        return False
    
def check_palindrome(input_str):
    for i in range(len(input_str)//2 + 1):
        if input_str[i] == input_str[-i-1]:
            continue
        else:
            return False
    return True

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr

    
print(check_if_palindrome("nn"))
print(check_palindrome("nn"))
print(selection_sort([5,1,8,1,3,7,4,2]))