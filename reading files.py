
# open files in different modes r = read , w = write, a = append, r+ = read and write
employee_file = open("employees", "r")
# check to make sure file is readable
#print(employee_file.readable())
# outputs the entire file
#print(employee_file.read())
# output 1st line of file
#print(employee_file.readline())
for employee in employee_file.readlines():
# reads file and puts each line in a list for index position 1, can drop the index to display the entire line
    print(employee)

employee_file.close()


