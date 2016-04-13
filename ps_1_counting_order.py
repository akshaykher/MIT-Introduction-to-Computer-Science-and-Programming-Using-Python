"""
A catering company has hired you to help with organizing and preparing customer's orders. 
You are given a list of each customer's desired items, and must write a program that will count the number of each items 
needed for the chefs to prepare. The items that a customer can order are: salad, hamburger, and water.
Write a function called item_order that takes as input a string named order. 
The string contains only words for the items the customer can order separated by one space. 
The function returns a string that counts the number of each item and consolidates them in the following order: 
salad:[# salad] hamburger:[# hambruger] water:[# water]
If an order does not contain an item, then the count for that item is 0. 
Notice that each item is formatted as [name of the item][a colon symbol][count of the item] and all item groups are separated by a space.

For example:

If order = "salad water hamburger salad hamburger" then the function returns "salad:2 hamburger:2 water:1"
If order = "hamburger water hamburger" then the function returns "salad:0 hamburger:2 water:1"
"""
#order = "hamburger water hamburger"

def item_order(order):
    order = order.replace('salad','s')
    order = order.replace('hamburger','h')
    order = order.replace('water','w')
    
    count_s = 0
    count_h = 0
    count_w = 0
    
    for i in range(len(order)):
        if order[i] == "s":
            count_s = count_s + 1
        elif order[i] == 'h':
            count_h = count_h + 1
        elif order[i] == 'w':
            count_w = count_w + 1
    
    return("salad:" + str(count_s) + " hamburger:" + str(count_h) + " water:" + str(count_w))