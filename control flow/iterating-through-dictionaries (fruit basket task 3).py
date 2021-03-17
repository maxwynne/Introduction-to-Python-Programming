# Keep track of both the number of fruits and other items in the basket

# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary

#if the key is in the list of fruits, add to fruit_count.

#if the key is not in the list, then add to the not_fruit_count

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

for object, count in basket_items.items():
   if object in fruits:
       fruit_count += count
   else:
       not_fruit_count += count    
    
print(fruit_count, not_fruit_count)

print(There are {fruit_count} fruits in the basket..format(result), There are {not_fruit_count} fruits in the non-fruit basket.format(result))
