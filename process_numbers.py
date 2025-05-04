
input_str = input("Введите список чисел через запятую: ")
numbers = [int(num.strip()) for num in input_str.split(',')]
even_numbers = [num for num in numbers if num % 2 == 0]
print("Четные числа:", even_numbers)
max = numbers[0]
min= numbers[0]
for num in numbers[1:]:
    if num > max:
        max = num
    if num < min:
        min = num
print("Максимальное число:", max)
print("Минимальное число:", min)
for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print("Отсортированный список:", numbers)
