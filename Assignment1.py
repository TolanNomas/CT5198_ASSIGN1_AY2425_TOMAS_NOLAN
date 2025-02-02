# Tomás Nolan 15105006 02/02/2025
# Q2a. Creates a list to store the number of customers that a business had each day

# Initialising empty customer list
cust_num = []

# Q2b. Use a for loop to ask the user to input the number of customers each day over a
# 7-day period.

# For loop that iterates over 7 days and adds the quantity of customers to earlier list
for i in range(1,8):
    # Int wrapper used below to avoid type error
    count = int(input(f"Enter number of customers for day {i}: "))
    cust_num.append(count)

# Q2c. Determine the maximum, minimum and average number of customers for the week.

# Calculating max,min and avg customer for week using built-in functions
max_cust = max(cust_num)
min_cust = min(cust_num)
average_cust = sum(cust_num)/len(cust_num)

# Printing results for the above using f-strings to avoid rounding errors
print(f"The maximum number of customers for the week is {max_cust}")
print(f"The minimum number of customers for the week is {min_cust}")
print(f"The average number of customers for the week is: {average_cust:.2f}")


