import time
def check_inventory(x): 
    for i in range(len(inventory)):
        if inventory[i][0] == x:
            return i
inventory = []
adding_necessary = True
print('Do you already have a preexisting inventory?')
answer1 = input()
if answer1 == 'yes':
    print('Please enter it')
    pre = eval(input())
    inventory.extend(pre)
    print('Would you like to restock any of these products?')
    answer2 = input().lower()
    if answer2 == 'yes':
        while True:
            print('Enter "done" when you have finished restocking')
            print(inventory)
            print('What is the name of the product you would like to restock?')
            restock_item = input()
            if restock_item.lower() == 'done':
                break
            pos_restock = check_inventory(restock_item)
            if pos_restock is not None:
                print('How many more of this product do you have?')
                restock_quantity = int(input())
                inventory[pos_restock] = (inventory[pos_restock][0], inventory[pos_restock][1], inventory[pos_restock][2] + restock_quantity)
                print('Inventory updated')
            else:
                print('I am sorry, but this product('+restock_item+') is not in the inventory')
    print('Do you have any products you would like to add?')
    answer3 = input()
    if answer3 == 'no':
        adding_necessary = False
while adding_necessary == True:
    print("Enter 'done' when you have already completed the inventoy")
    print('What is the name of the product you would like to add?')
    name_item = input()
    if name_item.lower() == 'done':
        break
    print('What is the price of this product?')
    price = float(input())
    print('How many of this product do you have?')
    quantity = int(input())
    novo_pro = (name_item, price, quantity)
    inventory.append(novo_pro)
    print('Item cataloged')
    print('Curret inventory:')
    print(inventory)
print('Final inventory:')
print(inventory)
while True:
    print("Enter 'done' when you have ended your sales of the day")
    print(inventory)
    print('What would this customer like?(please enter the name of the product as it is written)')
    item_of_customer = input()
    if item_of_customer.lower() == 'done':
        break
    pos = check_inventory(item_of_customer)
    if pos is not None:
        print(inventory[pos])
        print('How many of this product would the customer like?')
        n_item_of_customer = int(input())
        if inventory[pos][2] < n_item_of_customer:
            print("I am sorry, but there aren't enough of this product for the order")
        else:
            price_customer = n_item_of_customer*(inventory[pos][1])
            print('That will be: '+str(price_customer))
            print('Will the customer be able to pay?')
            answer4 = input()
            if answer4 == 'no':
                print('Purchase canceled')
                time.sleep(2)
            else:
                print('Purchased made')
                inventory[pos] = (inventory[pos][0], inventory[pos][1], inventory[pos][2] - n_item_of_customer)
                if inventory[pos][2] == 0:
                    del inventory[pos]
                time.sleep(2)
    else:
        print('I am sorry, but this product('+item_of_customer+') is not in the inventory')
print('This is the final inventory:')
print(inventory)