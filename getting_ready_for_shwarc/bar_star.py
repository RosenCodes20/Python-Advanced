drink_deliveries = input().split(": ")
start_beers = 200
start_wines = 300
beer_deliveries = 0
beer_orders = 0
wines_deliveries = 0
wines_orders = 0
while drink_deliveries[0] != "END":
    drink = drink_deliveries[0]
    deliveries = int(drink_deliveries[1])

    if drink == "Beers" and deliveries > 0:
        start_beers += deliveries
        beer_deliveries += 1

    elif drink == "Beers" and deliveries < 0:
        start_beers += deliveries
        beer_orders += 1

    elif drink == "Wines" and deliveries > 0:
        start_wines += deliveries
        wines_deliveries += 1

    elif drink == "Wines" and deliveries < 0:
        start_wines += deliveries
        wines_orders += 1

    drink_deliveries = input().split(": ")

print(f"Wines: {start_wines}")
print(f"Deliveries: {wines_orders}")
print(f"Order: {wines_orders}")
print(f"Beers: {start_beers}")
print(f"Deliveries: {beer_deliveries}")
print(f"Orders: {beer_orders}")