suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']

beginning = suitcase[0:4]
print(beginning)
middle = suitcase[2:4]

# this followoing code is menat to demonstrate list slicing
suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
start = suitcase[:3]
end = suitcase[4:]

votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']
jake_votes = votes.count('Jake')
print(jake_votes)
#preceding code shows how to count the number of items  in a list

### Exercise 1 & 2 ###
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']
addresses.sort()
print(addresses)
# Sort addresses here:

### Exercise 3 ###
names = ['Ron', 'Hermione', 'Harry', 'Albus', 'Sirius']
names.sort()
print(names)
### Exercise 4 ###
cities = ['London', 'Paris', 'Rome', 'Los Angeles', 'New York']

sorted_cities = cities.sort()
print(sorted_cities)

#preceding code demonstrates the use of sort, but remember
# sort() does not return anything, it sorts whatever the list is,
#one way around this is to save an original of a list as list()
# But aonther way is sorted()- it creates a new sorted list and leaves the original intact

inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']
inventory_len = len(inventory)
first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 = inventory[0:3]
twin_beds = inventory.count('twin bed')
inventory.sort()
# here are all the functions of this chpter except for sorted

toppings = ['pepperoni', 'pineapple', ' cheese', 'sausage', 'olives',' anchovies', 'mushrooms'] 
prices = [2, 6, 1, 3, 2, 7, 2]
num_pieces = len(toppings)
print('We sell ' + str(num_pieces) + ' different kinds of pizza!')
pizzas = list(zip(prices, toppings))
print(pizzas)
pizzas.sort()
cheapest_pizzas = pizzas[0]
print(cheapest_pizzas)
priciest_pizzas = pizzas[-1]
print(priciest_pizzas)
three_cheapest = pizzas[0:3]  
print(three_cheapest)
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)












