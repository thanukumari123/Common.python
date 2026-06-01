numbers = [10, 20, 30, 40, 50]
numbers.remove(20)
print("After remove:", numbers)
removed = numbers.pop(1)
print("Popped value:", removed)
print("After pop:", numbers)
del numbers[0]
print("After del:", numbers)