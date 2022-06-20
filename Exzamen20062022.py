# 1. Напишите функцию, которая будет принимать номер кредитной карты и
# показывать только последние 4 цифры. Остальные цифры должны заменяться
# звездочками
def card():
    number_card = input('Введите номре карты: ')
    while len(number_card) != 16:
        print('Данной карты не существует')
        number_card = input('Введите номре карты: ')
    else:
        return '*' * (len(number_card) - 4) + number_card[-4:]

print(card())

print()

# 2. Напишите функцию, которая проверяет: является ли слово палиндромом
def palindrom():
    palindrom_vvod = str(input('Введите что-нибудь: '))
    palindrom_dovv = palindrom_vvod[::-1]
    if palindrom_vvod == palindrom_dovv:
        return 'YES'
    else:
        return 'NO'

print(palindrom())

print()

# 3. Задача про томаты
class Tomato:
    states = {1: 'пусто', 2: 'цветок', 3: 'зеленый', 4: 'желтый', 5: 'красный'}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 5:
            self._state += 1
        print(f'Томат {self._index + 1} - {Tomato.states[self._state]}')

    def is_ripe(self):
        if self._state == 5:
            return True
        else:
            return False

class TomatoBush:

    def __init__(self, numbers):
        self.tomatoes = [Tomato(i) for i in range(0, numbers)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []

class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print(f'Садовник {self.name} решил поработать')
        self._plant.grow_all()
        print(f'Садовник {self.name} закончил работать')

    def harvest(self):
        print(f'Садовник {self.name} решил собрать урожай')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print(f'Садовник {self.name} убрал все томаты')
        else:
            print('Еще все томаты не созрели')

    @staticmethod
    def knowledge_base():
        print('Помидоры можно собирать с мая по октябрь, '
              'если выращивать тепличные сорта. Даже в том регионе, '
              'где в августе уже сыро и холодно. При этом выращивать '
              'томаты в теплице сможет даже новичок.')

Gardener.knowledge_base()
Tomato_Bush = TomatoBush(10)
gardener = Gardener('Sergey', Tomato_Bush)
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()