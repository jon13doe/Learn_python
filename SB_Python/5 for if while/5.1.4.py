s = 0
i = 1
while i < 100:                        # i < 100 штатное завершение цикла
    if i == 0:
        break                         # break не штатное завершение цикла
    s += 1 / i
    i +=1
else:                                 # срабативает если происходит штатное завершение цикла
    print("summa vich korectno")
print(s)


