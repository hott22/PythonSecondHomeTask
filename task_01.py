# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".

my_str = 'Напишите прогабврамму, удаляабвющую из текабвста все слова, содержащие'
my_str = my_str.split(" ")
print(my_str)
res = ''
for word in my_str:
    if word.find('абв') == -1:
        res += word + ' '
        
print(res)