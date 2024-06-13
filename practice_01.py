# 1. Generate an infinite Fibonacci series using a generator.
# 2. Sort a list without using the keyword Sort.
# 3. Check whether a string is palindrome or not?
# 4. Sort a dictionary dict comprehension.
# 5. Find the pair with a given number in a list. two elements sum to the given number.
# 6. Create a Fibonacci series using recursion.
# 7. String manipulation. "The Sky is Blue" to "Blue is The Sky"
# 8. Find the maximum repeated character in a string without having o(n2) complexity.
# 9. Find a maximum and minimum value in a List without using any predefined function.
#10. Check if a no is prime or get the prime nos upto n
#11. Group amalgam words
#12. Convert this list [1, 2, [3, 4],[5,6,[7,8,[9,10]]]] to [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#13. Convert these two lists [1,2,3,4] and [5,6,7,8] to {1:5 ,2:6, 3:7, 4:8}
#14 Class inheritance and method overriding

import time
import math
from functools import reduce

# 6
def fibonacci(n):
    if n <= 0:
        return None
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
# 1
def fib(n):
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a, b = b, a+b

# 3
def check_if_palindrome(input_str):
    if input_str == input_str[::-1]:
        return True
    else:
        return False

# 3
def check_palindrome(input_str):
    for i in range(len(input_str)//2 + 1):
        if input_str[i] == input_str[-i-1]:
            continue
        else:
            return False
    return True

# 2
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr

# 1
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

# 6
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

# 4
def sort_dict(input_dict):
    sorted_dict = {k:v for k, v in sorted(input_dict.items(), key=lambda item: item[1])}
    return sorted_dict

def custom_dict_sort(input_dict):
    sorted_dict = {k:v for k,v in sorted(input_dict.items(), key=lambda x:x[0])}
    return sorted_dict

# 5 (O(n2))
def find_sum(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if (target - arr[i]) == arr[j]:
                return [arr[i], arr[j]]
    return [0, 0]

# 8
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

# 10
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

# 14
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

list1 = [1, 2, [3, 4],[5,6,[7,8,[9,10]]]]
list2 =[1,2,3,4]
new_list = []

# 12
def format_list(input):
    if isinstance(input, int):
        new_list.append(input)
        return
    for i in range(len(input)):
        if isinstance(input[i], int):
            print(input[i])
            new_list.append(input[i])
        elif isinstance(input[i], list):
            if isinstance(input[i], list):
                format_list(input[i])

# group anagram
input_list = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# 11
def find_anagram(arr):
    result = {}
    for word in arr:
        sorted_word = "".join(sorted(word))
        if sorted_word in result:
            result[sorted_word].append(word)
        else:
            result[sorted_word] = [word]
    return list(result.values())
    
print(find_anagram(input_list))

list1 = [1,2,3,4]  
list2 = [5,6,7,8]
# outout :{1:5 ,2:6, 3:7, 4:8}

# 13
def get_output(list1, list2):
    result = {k:v for k,v in zip(list1, list2)}
    return result
    
print(get_output(list1, list2))

# 10
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
        else:
            continue
    return True
        
print(is_prime(1))
print([i if is_prime(i) == True else 0 for i in range(1, 10)])

# 5
def find_pair_with_sum(lst, target_sum):
    # Dictionary to store the elements and their indices
    seen_elements = {}
    
    # Iterate through the list
    for index, element in enumerate(lst):
        # Calculate the complement
        complement = target_sum - element
        
        # Check if the complement is already in the dictionary
        if complement in seen_elements:
            # Return the pair
            return (complement, element)
        
        # Add the element to the dictionary
        seen_elements[element] = index
    
    # If no pair is found, return None
    return None

# Example usage
lst = [2, 7, 11, 15]
target_sum = 9
result = find_pair_with_sum(lst, target_sum)
print(result)  # Output: (2, 7)

# Lamda, list comprehension, map, filter, reduce examples
list1 = list(range(10))
square_list = list(map(lambda x:x**2, list1))
even_list = list(filter(lambda x:True if x%2 == 0 else False, list1))
sum = reduce(lambda x, y: x+y, list1)
sqrt_list = list(filter(lambda x: True if math.sqrt(x).is_integer() else False, list1))
cubicrt_list = [i for i in list1 if math.pow(i, 1/3).is_integer()]
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
