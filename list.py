# Empty list
empty_list = []
print(empty_list)

# List with numbers
numbers = [1, 2, 3, 4, 5]
print(numbers)


# List with strings
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Mixed data types
mixed = [10, "hello", 3.14, True]
print(mixed)


# 🔹 Accessing Elements
fruits = ["apple", "banana", "cherry", "mango"]

print(fruits[0])   # apple
print(fruits[0:])


#slicing list[start:end:step]

print(fruits[1:3]) # ['banana', 'cherry'] (slicing)

print(numbers[0:5:2])

print(numbers[:3])    # (from beginning to index 2)
print(numbers[3:])    # (from index 3 to end)
print(numbers[:])     # (print all index from starting to end )


# Using Negative Index
print(numbers[-4:-1])   # [2, 3, 4]
print(numbers[-3:])     # [3, 4, 5]



# 🔹 Modifying Lists
fruits = ["apple", "banana", "cherry", "mango"]
fruits[1]="orange"
print(fruits)   # ['apple', 'orange', 'cherry', 'mango']

numbers[4]=40
print(numbers)

# 🔹 Adding Elements
fruits.append("kiwi")        # add at end
fruits.insert(2, "grapes")   # add at index
fruits.extend(["pear", "guava"])  # add multiple from last 
print(fruits)

# 🔹 Removing Elements
fruits.remove("apple")   # remove by value
print(fruits)
fruits.pop(1)            # remove by index 
print(fruits)
fruits.pop()             # remove last
print(fruits)
del fruits[0]            # delete by index
print(fruits)

fruits.clear()         # remove all elements
print(f"All Fruits are removed {fruits}")

# 🔹 Searching in Lists
nums = [10, 20, 30, 40, 20, 50]

print(nums.index(20))   # 1 (find the index of only first element )
print(nums.count(20))   # 2 (total occurrence of any element)

# 🔹 Sorting and Reversing
nums = [5, 2, 9, 1, 7]

nums.sort()
print(nums) # [1, 2, 5, 7, 9]

nums.sort(reverse=True)
print(nums) # [9, 7, 5, 2, 1]

nums.reverse()
print(nums) # [1, 2, 5, 7, 9]

# 🔹 Copying Lists
a = [1, 2, 3]
b=a.copy() #shallow copy
print(b)

#appending in copied list
b.append(4)

print("a:", a)  # [1, 2, 3]
print("b:", b)  # [1, 2, 3, 4]

# 🔹 Useful Functions
nums = [3, 6, 1, 9, 2]

print("printing the length of list", nums)
print(len(nums))   # 5

print("printing the maximum value of list")
print(max(nums))   # 9

print("printing the manimum value of list")
print(min(nums))   # 1
print("printing the sum of  value of list")
print(sum(nums))   # 21


# 🔹 Convert Other Data Types to List

nums="12345"
char=list(nums)

print(char)
print("type of char is ", type (char))


# 🔹  Removing Duplicates
nums = [1, 2, 3,  4, 5]

unique = list(set(nums))
print(unique)   # order may change

# 🔹 print the list element using loop 
print(nums)
for i in nums:
    print(i)

fruits = ["apple", "banana", "cherry", "mango"]
print(fruits)
for fruit in fruits:
    print(fruit)