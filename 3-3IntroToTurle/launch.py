def discount(orig_price, discount):	
	discounted_price = orig_price * (1-discount)
	return discounted_price

# $100 with a 20% discount
myOriginalPrice = 50
myDiscount = .2
print("Originally $" + str(myOriginalPrice))
print("Now, with discount $" + str(discount(myOriginalPrice, myDiscount)))
