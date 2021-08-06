monthConversions = { #the keys are unique
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "Octuber",
    "Nov": "November",
    "Dec": "December",

}
#print(monthConversions["1"])
print(monthConversions["Dec"])
print(monthConversions.get("No", "Not a valid key"))