#цена товара
#количевтво денег
#хватит ли на товар

print('PSSSSS: default launguage is russian      |      ПСССС стандарт язык русский')
print('   ')
print('   ')
lang_opt = input('Что бы сменить язык введите англискую l    |          Switch launguage press english l:      ')
lang = ['RUS']
while lang_opt == 'l':
    if lang[0] == 'RUS':
        lang[0] = 'ENG'
        lang_opt = input('Вы сменили язык на Ангийский:       ')
    else:
        lang[0] = 'RUS'
        lang_opt = input('Вы сменили язык на Русский:      ')
        
if lang[0] == 'ENG':
    mensh = 'You dont have enough for the product'
    rav = 'You only have enough without a building!'
    bolsh = 'Do you have enough for the product'
    
if lang[0] == 'RUS':
    mensh = 'У вас не хватает на товар'
    rav = 'У вас хватает только без сдачи!'
    bolsh = 'У вас хватает на товар'

tovar1 = int(input ('Сколько стоит товар: '))
bal = int(input ('Сколько у вас денег: '))

if bal < tovar1:
    print(mensh)
elif bal > tovar1:
    print(bolsh)
if bal == tovar1:
    print(rav)

#version 0.1