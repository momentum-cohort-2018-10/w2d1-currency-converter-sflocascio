# Create a function called convert that takes a list called rates, a number called value, a string called from, and a string called to. Make sure than when you call convert with from and to being equal, the return value is the same as value.

# The rates list should contain a list of tuples, with each tuple containing a currency code you can convert from, a currency code you can convert to, and a rate.

# [("USD", "EUR", 0.74)]
# This means that each dollar is worth 0.74 euros.

# value is the amount of currency, from is the current currency code, and to is the currency code you wish to convert to.

# Given the above rates, make sure that converting 1 dollar into euros returns the following value: 0.74.

# Next, test that you can convert currency with a value that is not 1.

value = 10 
rates = [("USD", "EUR", 0.74), ("EUR", "JPY", 145.949)]

def convert(rates, value, _from, to):
    if _from == to:
        return value
    for conversion in rates:
        if _from == conversion[0] and to == conversion[1]:
            return value * conversion[2]
        if _from == conversion[1] and to == conversion[0]:
            return value / conversion[2]
        

print(rates[0], value, rates[0][0], rates[0][1])
#convert(rates[1], value, rates[1][0], rates[1][1])
#convert(rates[0], value, rates[0][0], rates[0][1])



