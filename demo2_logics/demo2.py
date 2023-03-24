customer_name = "Mary Smith"
item_desc = "shirt"

message = customer_name + " wants to purchase a " + item_desc
print(message)

# 1. Declare and initialize numeric fields. Include price and tax ,
#      quantity .
# 2. Change the message variable to include quantity
#       (example: "Mary Smith wants to purchase 1 Shirt.")
# 3. Declare total. Calculate total by multiplying price * quantity * tax.
# 4. Print a message showing the total cost.
#       (example:  "Total cost with tax is: 25.78.")

price = 1000
tax = 28
quantity = 5

message = message.replace("a " + item_desc, str(quantity) + " " + item_desc)
print(message)

total = price * quantity * tax

print("Total cost with tax is:", total)

print("Total cost with tax is: " + str(total))
print(f"Total cost with tax is: {total}")

total_message=f"Total cost with tax is: {total}"

out_of_stock=False

if quantity>1:
    message=message+'s'

if out_of_stock:
    print("Item not available")
else:
    print(message)
    print(total_message)

#will start at 4 PM IST
