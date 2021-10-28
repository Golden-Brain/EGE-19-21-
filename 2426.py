
def move(x): # Фукция хода

    variants = [] # Все возможные варианты

    if (x * 3) % 2 != 0: # Проверяем каждый вариант на делимость двойкой
        variants.append(x * 3)
    if (x + 1) % 2 != 0:
        variants.append(x + 1)
    if (x + 3) % 2 != 0:
        variants.append(x + 3)

    return variants


def win(x): # Если в куче бедьше 51, то игрок выйграл
    return x >= 51

pos = [0] * 100

for s in range(1, 50 + 1):  # Выйгрыш в один ход (Петя)
    if any(win(h) for h in move(s)):
        pos[s] = 1

for s in range(1, 50 + 1): # Выйгрыш в один ход (Ваня)
    if pos[s] == 0 and all(pos[h] == 1 for h in move(s)):
        pos[s] = -1

for s in range(1, 50 + 1): # Выйгрыш в два хода (Петя)
    if pos[s] == 0 and any(pos[h] == -1 for h in move(s)):
        pos[s] = 2

for s in range(1, 50 + 1): # Выйгрыш в два хода (Ваня)
    if pos[s] == 0 and all(pos[h] == 2 for h in move(s)):
        pos[s] = -2

for index,value in enumerate(pos[:51]):

    if value == -1:
        print("При",index,'будет выйгрыш Вани за 1 ход')
    if value == 2:
        print("При",index,'будет выйгрыш Пети за 2 хода')
    if value == -2:
        print("При",index,'будет выйгрыш Вани за 2 хода')
       
       
#-----Answers-------
# 7
# 12 14
# 2
