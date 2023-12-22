from rover_control import start

rule = '''

Начальные координаты: x=0, y=0
Начальное направление: forward

Выберите направление движения:
    Вперёд - f
    Направо - r
    Налево - l
    Назад - b
Для завершения введите - exit
'''
print(rule)

start()
