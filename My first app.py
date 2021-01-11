#This app calculates the cost of items

#Define the budget
budget = (950.00)

#Define item costs
clothes = (89.99)
watch = (299.99)
tv = (500.00)
coupon = (-50.00)

#Calculate total
total = (budget - clothes - watch - tv + coupon)

#Print totals
print(total)
if total < 0.00:
    print("Insufficent funds.")
if total > 0.01:
    print("Transaction complete.")