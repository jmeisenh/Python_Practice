

# to append to a file
#employee_file = open("employees", "a")
# w will write over file
# employee_file = open("employees", "w")
# employee_file.write("\nKelly - Custumer Service")
# w can also be used to create a new file

employee_file = open("employees1", "w")
employee_file.write("\nKelly - Customer Service")
employee_file.close()