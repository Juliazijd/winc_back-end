# Do not modify these lines
__winc_id__ = "62311a1767294e058dc13c953e8690a4"
__human_name__ = "casting"

# Add your code after this line
# Part 1
leek_price = 2
print("Leek price is " + str(leek_price) + " euro per kilo")

# Part 2
string_with_amount = "leek 4"
print(string_with_amount.find("4"))
leek_amount = int(string_with_amount[5:])
print(leek_amount)
sum_total = leek_amount * leek_price
print(sum_total)

# part 3
broccoli_price = 2.34
broccoli_amount = 1.6
broccoli_total = round(broccoli_price * broccoli_amount, 2)
print(f"{broccoli_amount}kg broccoli costs {broccoli_total} euro")
