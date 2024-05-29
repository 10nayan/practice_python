# 1. Generate an infinite Fibonacci series using a generator.
# 2. Sort a list without using the keyword Sort.
# 3. Check whether a string is palindrome or not?
# 4. Sort a dictionary dict comprehension.
# 5. Find the pair with a given number in a list. two elements sum to the given number.
# 6. Create a Fibonacci series using recursion.
# 7. String manipulation. "The Sky is Blue" to "Blue is The Sky"
# 8. Find the maximum repeated character in a string without having o(n2) complexity.
# 9. Find a maximum and minimum value in a List without using any predefined function.
import time
import math
from functools import reduce
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

def fib_series(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a+b
# print("Fib series", list(fib_series(10)))

def wrapper_function(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        print("start")
        returned_value = func(*args, **kwargs)
        t2 = time.time()
        print("end")
        print("total time", t2-t1)
        return returned_value
    return wrapper

def fib_element(n):
    if n < 0:
        raise Exception("Invalid no")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib_element(n-1) + fib_element(n-2)

@wrapper_function
def custom_selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr

# 4. Sort a dictionary/ dict comprehension.
def sort_dict(input_dict):
    sorted_dict = {k:v for k, v in sorted(input_dict.items(), key=lambda item: item[1])}
    return sorted_dict

def custom_dict_sort(input_dict):
    sorted_dict = {k:v for k,v in sorted(input_dict.items(), key=lambda x:x[0])}
    return sorted_dict

def find_sum(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (target - arr[i]) == arr[j]:
                return [arr[i], arr[j]]
    return [0, 0]

def check_occurance(input_str):
    input_dict = {}
    for i in input_str:
        if i not in input_dict:
            input_dict[i] = 1
        else:
            input_dict[i] += 1
    max_occ = {k:v for k,v in sorted(input_dict.items(), key=lambda i:i[1], reverse=True)}
    max_occ_chr = list(max_occ.keys())[0] if max_occ.keys() else None
    return max_occ_chr

def check_if_prime(num):
    if num > 1:
        # Iterate from 2 to n // 2
        for i in range(2, (num//2)+1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

class Animal():
    def __init__(self, age):
        self.age = age

    def is_old(self):
        if self.age > 5:
            return True
        else:
            return False
    
    def make_sound(self):
        print("Haaa")
    
class Cow(Animal):
    def __init__(self, age, colour):
        super().__init__(age)
        self.colour = colour

    def is_old(self):
        if self.age >10:
            return True
        else:
            return False

    def make_sound(self):
        super().make_sound()
        print("hamaaaaa")

a = Animal(2)
c = Cow(12, "brown")
c.make_sound()
a.make_sound()

# list1 = list(range(10))
# square_list = list(map(lambda x:x**2, list1))
# even_list = list(filter(lambda x:True if x%2 == 0 else False, list1))
# sum = reduce(lambda x, y: x+y, list1)
# sqrt_list = list(filter(lambda x: True if math.sqrt(x).is_integer() else False, list1))
# cubicrt_list = [i for i in list1 if math.pow(i, 1/3).is_integer()]
# print(square_list, even_list, sum, sqrt_list, cubicrt_list)

# print(list(fib(10)))
# print(list(map(fibonacci, range(1, 11))))
# print(find_sum([1, 2, 3, 4, 5], 9))
# print(check_occurance("nayannyyyy"))
# print(custom_dict_sort({1: "x", 2: "y", 3: "z", 0:"a"}))
# print(fib_element(10))
# print(check_if_palindrome("nn"))
# print(check_palindrome("nn"))
# print(selection_sort([5,1,8,1,3,7,4,2]))
# print(custom_selection_sort([5,1,8,1,3,7,4,2]))