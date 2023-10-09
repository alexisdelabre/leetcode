def plusOne(digits):
    return [int(d) for d in str(int("".join(map(str, digits))) + 1)]

print(plusOne([1,2,3]))

def plusOneAdv(digits):
    for i in range(len(digits)-1, -1, -1):
        print(digits[i])
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] = digits[i] + 1
            return digits
    return [1] + digits 

print(plusOneAdv([1,2,9]))
print(plusOneAdv([9,9]))

# The provided `plusOne` function, while clever, is less efficient than the first one you showed (`plusOneAdv`) for several reasons:

# 1. **Multiple Conversions**: 
#     - First, the function converts each digit in the `digits` list to a string with `map(str, digits)`.
#     - Then, it joins them together with `"".join(...)`.
#     - After that, it converts the combined string back to an integer with `int(...)`.
#     - Finally, after the addition operation, it converts the resultant integer back to a string and then into a list of integers.
#     This repeated conversion process (list to string to int to string to list) involves multiple passes over the data.

# 2. **Memory Overhead**: 
#    Each of the conversions mentioned creates a new data structure in memory. For instance:
#    - The joined string representation of the list.
#    - The integer representation of the number.
#    - The string representation of the incremented number.
#    - The final list of digits.

#    This means more memory allocations and deallocations, which can slow down the operation, especially for long lists of digits.

# 3. **Integer Size Limitation**:
#    In Python, while integers can be of arbitrary size, converting very large numbers (long lists) into integers and then doing string operations on them can be computationally intensive. For extremely long lists, this approach can lead to performance issues.

# 4. **Simple Arithmetic vs. Conversions**:
#    The `plusOneAdv` function performs simple arithmetic and array operations, while the second function deals with repeated type conversions. Basic arithmetic operations and direct list manipulations are generally faster than type conversions.

# While the provided function is a concise and nifty way to achieve the goal (and may work perfectly fine for many common use cases), the earlier `plusOneAdv` approach is more direct and efficient, especially when dealing with long lists of digits.