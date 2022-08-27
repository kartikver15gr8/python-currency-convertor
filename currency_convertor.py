# So basically this is a currency convertor using python



with open('currency_data.txt') as f:
    lines = f.readlines()

# print(lines)
currencyDict = {}

for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]
    # print(parsed)
    # break
# print(currencyDict)
amount = int(input("Enter the amount:\n"))
print("Enter the name of the currency you want to convert this amount to?\n")
[print(item) for item in currencyDict.keys()]
currency = input("please enter one of these values:\n")
print(f"{amount} INR is equal to {amount*float(currencyDict[currency])} {currency} ")
