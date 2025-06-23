# variable

# greeting = "Hi"
# name = "Alice"

# print(greeting+", "+name)

# list = ["sam","alice","cherry"]
# print(list[0])
# list.append("deny")
# print(list)

# person = {
#     "name":"sama",
#     "job":"developer"
# }

# print(person["name"])

# person["city"] = "matara"
# print(person)

# question 1
def add_item(item,shop_list=None):# == also we can use is
    if shop_list == None:
        shop_list=[]
    shop_list.append(item)
    return shop_list

cart1_fixed = add_item("milk")
print(f"Fixed Cart 1: {cart1_fixed}")

cart2_fixed = add_item("yu")
print(f"Fixed Cart 1: {cart2_fixed}")
