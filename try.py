import pyo3_101 as p1

sum = p1.sum_as_string(1,2)
print(f"{sum} as type {type(sum)}")

john = p1.say_hello("John" , "Pycon")
print(john)

# test check_reg
print(p1.check_reg("reg_list.txt", "john"))
print(p1.check_reg("reg_list.txt", "jane"))
print(p1.check_reg("reg_list.txt", "adam"))
print(p1.check_reg("reg_list.txt", "mary"))

# test check_reg with a non-existent file
print(p1.check_reg("reg_list2.txt", "john"))