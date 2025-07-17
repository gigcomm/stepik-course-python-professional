import csv


with open('prices.csv', 'r', encoding='utf-8', newline='') as file:
    reader = csv.DictReader(file, delimiter=';')
    products = reader.fieldnames[1:]

    min_price = float('inf')
    min_product = None
    min_store = None

    for row in reader:
        store = row['Магазин']
        for product in products:
            price = int(row[product])
            if price < min_price:
                min_price = price
                min_product = product
                min_store = store
            elif price == min_price:
                if product < min_product:
                    min_product = product
                    min_store = store
                elif product == min_product and store < min_store:
                    min_store = store

    print(f"{min_product}: {min_store}")


