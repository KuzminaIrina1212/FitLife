# Проект FitLife - MVP версия 1.0


# 1. Знакомство

user_name = input('Как тебя зовут? ')
user_age = int(input('Сколько тебе лет? '))

# 2. Сбор данных

user_weight = float(input('Сколько ты весишь (кг)? '))
user_height = float(input('Какой у тебя рост (м)? '))

# Формула ИМТ: вес разделить на (рост в квадрате)
# TODO: Рассчитай bmi (Индекс массы тела)
bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)
# Подсчет воды: вес * 30 мл
# TODO: Рассчитай water_needed
water_needed = user_weight * 30
water_l = water_needed / 1000
# 4. Вывод красивого результата
print(f'Привет, {user_name}!')

print(f'Тебе {user_age} лет.')
print(f'Твой индекс массы тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_l:.2f} л. в день.')
print("Расчет окончен. Будьте здоровы!")
