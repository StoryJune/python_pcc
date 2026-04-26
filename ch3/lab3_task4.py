#Jason Li
#Sept 11 2025

#initializing
originalPrice = input("Please enter the total purchase price: ")
discountPrice = float(originalPrice)
#statement
if discountPrice >= 128:
    finalPrice = discountPrice - (discountPrice * 0.16)
else: 
    finalPrice = discountPrice - (discountPrice * 0.08)

print(f"The price after the discount is $ {finalPrice:.2f}")