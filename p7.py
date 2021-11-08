#p_7. Create a function that takes two arguments: the original price and the discount percentage as integers and returns the final price after the discount.
#Examples

#dis(1500, 50) ➞ 750
#dis(89, 20) ➞ 71.2
#dis(100, 75) ➞ 25

#original_price=int (input("What is the original price of the item? "))
#discount= int(input("How many percent discount do you give? "))
#discounted_price=int (original_price - discount*original_price/100)
#print(f'Discounted price of the item is ${discounted_price} ')
#print("Enjoy using it, thank you")
#Yukaridaki normal oldu, asagida return de kullandim

original_price=int (input("What is the original price of the item? "))
discount= int(input("How many percent discount do you give? "))

result=int(original_price-original_price*discount/100)

def dis(result):
        return dis(result)

print(f'Discounted price of the item is ${result}')
print("Thank you for choosing us")
