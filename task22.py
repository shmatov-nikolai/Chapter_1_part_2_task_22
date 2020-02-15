
def perevod_Celsius_to_Fahrehreim(celsius):
    num_Fahrehreim = 9/5 * celsius + 32
    print(f"{celsius} градусов Цельсия  - это: {num_Fahrehreim} градусов по шкале Фаренгейта ")


def perevod_Fahrehreim_to_Celsius(fahrehreim):
    num_celsius = 5/9 * (fahrehreim - 32)
    print(f"{fahrehreim} градусов по Фаренгейту  - это: {num_celsius} градусов по шкале Цельсию ")






perevod_Celsius_to_Fahrehreim(32)
perevod_Fahrehreim_to_Celsius(90)

