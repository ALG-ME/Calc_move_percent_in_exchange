price_open = 122234
price_close = 123445

pleco = 20

movement_percentage = ((price_close - price_open) / price_open) * 100
movement_percentage_place = movement_percentage * pleco
formatted_percentage = "{:.2f}%".format(movement_percentage)
print(f'''Процент движения:, {formatted_percentage}
Процент общий {movement_percentage_place}''')
