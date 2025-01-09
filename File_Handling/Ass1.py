import csv
with open('sales.csv', mode='r') as file:
    csv_read= csv.reader(file)

    total_sales = {}

    for row in csv_read:
        product = row[0]  
        sales = int(row[1])

        if product in total_sales:
            total_sales[product] += sales 
        else:
            total_sales[product] = sales

for product, total in total_sales.items():
    print(f"Total sales for {product}: {total}")