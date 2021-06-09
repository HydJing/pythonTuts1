monthConversion = {
    "Jan": "January",
    "Feb": "Feburary",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    8: "August"
}

print(monthConversion['Jul'])
print(monthConversion[8])
print(monthConversion.get("Jan"))
print(monthConversion.get("Yoyo", "fake index yo"))