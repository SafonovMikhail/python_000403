#000403_01_09_vid04_ex01_FTT.py
x1,x2,x3 = False, True, False
print("x1: ", x1)
print("x2: ", x2)
print("x3: ", x3)
print("OR:AND:NOT - в порядке возрастания приоритета")
print("not x1 or x2 and x3: ", not x1 or x2 and x3)
# Приостановил 2019-05-25, причина - медленно! См. 000010
# Возобновляю 2019-06-08, причина - нужндо в разнообразном двигаться вперед!
# Расчет с учетом приоритета логических операций показывает TRUE
# С помощью скобок расставим прямой приоритет
print("(not x1 or x2) and x3: ", (not x1 or x2) and x3)
print("(x1 or x2) and x3: ", ((x1 or x2) and x3))
print("x1 or (x2 and x3): ", (x1 or (x2 and x3)))
print("x1 or (x2 and x3): ", (x1 or (x2 and x3)))
print("not x1 or (x2 and x3): ", (not x1 or (x2 and x3)))
