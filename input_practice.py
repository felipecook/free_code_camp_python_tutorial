
# reads the file
#employee_file = open("employees.txt", "r")

# print(employee_file.readable())
# print(employee_file.read())
# print(employee_file.readline())
# for employee in employee_file.readlines():
#     print(employee)

# print(employee_file.readlines()[1])


# writes the file (overwrites the file)
# open("employees.txt", "w")


# appends the file
employee_file = open("employees.txt", "a")
employee_file.write("\nR - A")
employee_file.close()

# reads and writes file
# open("employees.txt", "r+")
