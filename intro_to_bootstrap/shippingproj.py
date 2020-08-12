def ground_shipping_cost(weight):
  if weight <= 2:
    return ((weight * 1.5) + 20)
  elif weight <= 6:
    return ((weight * 3) + 20)
  elif weight <=10:
    return ((weight *4) + 20)
  else:
    return ((weight * 4.75) + 20)
print(ground_shipping_cost(8.4))
premium_ground_shipping = 125

def drone_shipping_cost(weight):
  if weight <= 2:
    return (weight * 4.5)
  elif weight <= 6:
    return (weight * 9)
  elif weight <= 10:
    return(weight * 12)
  else:
    return (weight * 14.25)
print(drone_shipping_cost(1.5))

def best_shipping_option(weight):
  if ground_shipping_cost(weight) and drone_shipping_cost(weight) > premium_ground_shipping:
    return "Premium ground shipping is your best option at $125." 
  elif ground_shipping_cost(weight) <= drone_shipping_cost(weight): 
    return "Standard ground shipping is your best option at $" + str(ground_shipping_cost(weight)) +"."
  elif ground_shipping_cost(weight) > drone_shipping_cost(weight) :
    return "Drone shipping is your best option at $" + str(drone_shipping_) + "."

print(best_shipping_option(4.8))
print(best_shipping_option(41.5))