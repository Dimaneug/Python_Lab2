import csv
import itertools

excursions = []
with open("ex_dop/input_4.csv", "r", newline="") as file:
    reader = csv.DictReader(file, delimiter=';')
    dates = list(reader.fieldnames)
    dates.pop(0)
    i = 0
    for row in reader:
        excursions.append(row)

del reader

prices = []
for i in range(len(excursions)):
    prices.append(list(excursions[i].values()))
    prices[i].pop(0)
    for j in range(len(prices[i])):
        prices[i][j] = int(prices[i][j])

prices_amount = []
for i in range(len(prices)):
    prices_amount.append(i)
    i += 1

all_permutations = tuple(itertools.permutations(prices_amount))
del prices_amount

final_price = sum(list(max(price) for price in prices))  # Считаем максимальную сумму потраченную на экскурсии
# Можно просто взять final_price очень большим, но тогда не будет универсальности

for i in range(len(all_permutations)):
    final_price_temp = 0
    for j in range(len(prices)):
        final_price_temp += prices[j][int(all_permutations[i][j])]
    if final_price_temp <= final_price:
        final_price = final_price_temp
        final_permutation_temp = list(all_permutations[i])
    del all_permutations[i]
    print(all_permutations[i])

final_permutation = [None] * len(dates)
final_prices = [None] * len(dates)

for index, value in enumerate(final_permutation_temp):
    final_permutation[value] = index + 1
    final_prices[value] = (prices[index][value])

with open("ex_dop/output_4.csv", "w") as file:
    columns = ["date", "excursion", "sum"]
    writer = csv.DictWriter(file, fieldnames=columns)
    writer.writeheader()
    for i in range(len(dates)):
        writer.writerow(dict(date=dates[i], excursion="#" + str(final_permutation[i]), sum=str(final_prices[i])))
    writer.writerow(dict(sum=final_price))
