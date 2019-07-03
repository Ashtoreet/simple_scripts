# price = 100
# vat_rate = 18

# vat = price / 100 * vat_rate

# print(vat)

# price_no_vat = price - vat

# print(price_no_vat)

# def get_vat(price, vat_rate):
# 	if vat_rate in range(0, 101) and price > 0:
# 		vat = price / 100 * vat_rate
# 		price_no_vat = price - vat
# 		print(price_no_vat)
# 	else:
# 		print('Ой!')


# price1 = -100
# vat_rate1 = 18

# get_vat(price1, vat_rate1)
def get_summ(one, two, delimeter=' '):
    return (str(one) + str(delimeter) + str(two)).upper()

print(get_summ('Hello', 'world!'))
