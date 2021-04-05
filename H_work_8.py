#1
school = {"1б": 12, "2a": 15, "2в": 13, "5в": 17, "5б": 20, "7а": 11, "7б": 10, "9в": 14}
print(school)
# а) в одном из классов изменилось количество учащихся
school["5в"] = 21
print(school)
# б) в школе появился новый класс
school["9б"] = 15
print("new_school:", school)
# с) в школе был расформирован (удален) другой класс
del school["1б"]
print(school)
# Вычислите общее количество учащихся в школе
summa = sum(school.values())
print("Сумма:", summa)

#2
print("="*100)
# Создайте функционал которий вернет новый словарь, "обратный" исходному,
# т.е ключами являются строки, а значениями – числа.
number = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five"}
print("number:", number)
new_number = {}
for key, value in number.items():
    new_number[value] = key
print("new_number:", new_number)