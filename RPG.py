"""RPG игра."""

import random
import sys
import time

knight_lives: int = 10
monsters_count: int = 0
knight_strength: int = 10
border_low: int = 5
border_high: int = 30
events_border_low: int = 1
events_border_high: int = 3
current_strength: int = knight_strength
current_lives: int = knight_lives
delay = 2

print('Вы начинаете опасное путешествие')
print('Ваше здоровье и сила атаки равна: %s, %s' % (current_lives, current_strength))
time.sleep(delay)


while monsters_count < 10:
    event: int = random.randint(events_border_low, events_border_high)
    # monster
    if event == 1:
        monster_health: int = random.randint(border_low, border_high)
        monster_strength: int = random.randint(border_low, border_high)
        print('Вы встретили чудовище с %s жизнями и %s силой удара.'
              % (monster_health, monster_strength))
        print('Нажмите 1 чтобы атаковать, нажмите 2 чтобы убежать')
        while True:
            user_input: str = str(input())
            if user_input == '1':
                while monster_strength < current_lives and \
                        current_strength < monster_health:
                    monster_health = monster_health - current_strength
                    current_lives = current_lives - monster_strength
                if monster_strength >= current_lives:
                    print('Монстер убил вас. Игра окончена')
                    time.sleep(delay)
                    sys.exit()
                elif monster_health <= current_strength:
                    current_lives = current_lives - monster_strength
                    print('Чудовище побеждено, у вас осталось %s здоровья'
                          % current_lives)
                    monsters_count += 1
                    time.sleep(delay)
                    break
            elif user_input == '2':
                print('Вы убежали от чудовища')
                time.sleep(delay)
                break
            else:
                print('Вы выбрали неверный вариант.Попробуйте еще раз')

    if event == 2:
        apple_health: int = random.randint(border_low, border_high)
        print('Вы нашли яблочко, которое увеличивает ваше здоровье на %s'
              % apple_health)
        current_lives = current_lives + apple_health
        print('Ваше текущее здоровье равно %s' % current_lives)
        time.sleep(delay)

    if event == 3:
        sword_strength: int = random.randint(border_low, border_high)
        print('Вы нашли меч с силой атаки %s' % sword_strength)
        print('Нажмите 1, чтобы взять его, нажмите 2, чтобы пройти мимо')
        while True:
            user_input = str(input())
            if user_input == '1':
                print('Вы взяли меч')
                current_strength = sword_strength
                print('Ваша сила увеличилась на ' + str(sword_strength))
                time.sleep(delay)
                break
            elif user_input == '2':
                print('Вы прошли мимо меча')
                time.sleep(delay)
                break
            else:
                print('Вы выбрали неверный вариант.Попробуйте еще раз')

print('Вы победили всех чудовищ и спасли ваше королевство. Ура!')
