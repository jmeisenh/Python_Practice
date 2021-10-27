
# dictionaries allow you to store info in "key value pairs"
# dictionaries are created in open and closed curly brackets
# dictionary keys must be unique
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Nov"])

print(monthConversions.get("DLuv", "Not a Valid key"))
# get function can output a defualt value that is not in the deictionaru