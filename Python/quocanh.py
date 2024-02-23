from datetime import date

# Prompt the user for the start date
start_date_str = input("Enter the start date (in YYYY-MM-DD format): ")

# Convert the start date string to a datetime object
start_date = date.fromisoformat(start_date_str)

# Prompt the user for the end date
end_date_str = input("Enter the end date (in YYYY-MM-DD format): ")

# Convert the end date string to a datetime object
end_date = date.fromisoformat(end_date_str)

# Calculate the number of days between the two dates
num_days = (end_date - start_date).days

# Print the result
print("The number of days between", start_date.strftime("%d %B %Y"), "and", end_date.strftime("%d %B %Y"), "is", num_days, "days.")
