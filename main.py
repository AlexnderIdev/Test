print ("Для подсчёта отпускной цены введите начальную стоимость товара через ENTER:")

def condition(x):
    if x % 10 > 5:
        x = x + 10 - x % 10
        return x
    else:
        x = x + 5 - x % 10
        return x
    

apple = int (input("Введите стоимость яблок = "))
banana = int (input("Введите стоимость бананов = "))
milk = int (input("Введите стоимость молока = "))

print ()
print ("Теперь введите желаемый процент прибыли, не менее 15%:")
profitPercentage = int (input("Желаемый процент прибыли = "))
while profitPercentage < 15:
    print ()
    print('Вы ввели процент меньше минимума! Желаемый процент не должен быть меньше 15.')
    profitPercentage = int (input("Повторно введите желаемый процент прибыли = "))

newPriceApple = (apple/100*profitPercentage) + apple
newPriceBanana = (banana/100*profitPercentage) + banana
newPriceMilk = (milk/100*profitPercentage) + milk

newPriceAppleRound = round(newPriceApple)
newPriceBananaRound = round(newPriceBanana)
newPriceMilkRound = round(newPriceMilk)

sellingPriceApple = condition(newPriceAppleRound)
sellingPriceBanana = condition(newPriceBananaRound)
sellingPriceMilk = condition(newPriceMilkRound)

print ()
print ("Отпускная цена яблок =", sellingPriceApple)
print ("Отпускная цена бананов =", sellingPriceBanana)
print ("Отпускная цена молока =", sellingPriceMilk)