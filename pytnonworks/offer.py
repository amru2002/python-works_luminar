item_price=45
offer_perc=5
# selling price?
# discount_price=(actual_price*perce)/100
discount_price=(item_price*offer_perc)/100
actual_price=item_price-discount_price
print(actual_price)


