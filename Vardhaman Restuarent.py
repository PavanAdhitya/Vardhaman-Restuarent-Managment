menu={
    'Biriyani':130,
    'Meals':100,
    'Chicken Curry':150,
    'Fish Curry':120,
    'Mutton Curry':180,    
}

print("Welcome to Vardhaman Restaurant")
print("Biriyani: Rs130\nMeals: Rs100\nChicken Curry: Rs150\nFish Curry: Rs120\nMutton Curry: Rs180")

order_total = 0

item_1=input("enter the name of the item you want to order= ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item [item_1] has been added to the order. Current total: Rs{order_total}")
else:
    print(f"ordered item {item_1} is not available in the menu.")

another_item = input("Do you want to order another item? (yes/no): ").strip().lower()
if another_item == 'yes':
    item_2 = input("Enter the name of the item you want to order: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item [{item_2}] has been added to the order. Current total: Rs{order_total}")
    else:
        print(f"Ordered item {item_2} is not available in the menu.")   
    print(f"Your total order amount is Rs{order_total}. Thank you for dining with us!")    