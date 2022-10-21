pole = """
  __A______B______C___
1|     ||     ||     |
 |__♟__||__♟__||__♟__|
2|     ||     ||     |
 |_____||_____||_____|
3|     ||     ||     |
 |__♙__||__♙__||__♙__|
"""

a = """
-|_A_|_B_|_C_| 
1|_♟_|_♟_|_♟_| 
2|___|___|___| 
3|_♙_|_♙_|_♙_| 
"""

board = [i for i in a]

logic = [[1,1, 1,],
        ['','',''],
        [0, 0, 0 ]]

n = 1
abc = "ABC"


while True:
    if n % 2 == 1:
        while True:
            choice = input("Введите ход (позиция_вашей_фигуры позиция_куда_ее_передвинуть): ")
            start, end = choice.split(" ")

            #start1 - индедекс строки, start0 - индекс столбца
            start0, start1 = abc.index(start[0]), int(start[1])-1
            #end1 - индекс строки, end0 - индекс столбца
            end0, end1 = abc.index(end[0]), int(end[1])-1

            if logic[start1][start0] == 0: # Проверка пешки
                if start0-end0 == 0: #Ход прямо
                    if logic[end1][end0] == '' and abs(start1-end1) < 2: #Если клетка свободна и ход правильный
                        logic[start1][start0], logic[end1][end0] = logic[end1][end0], logic[start1][start0]
                        print(logic)
                        n += 1
                        break
                    else:
                        print("Неверный ход!\n")
                else: #Диагональный ход
                    if abs(start0-end0) < 2 and logic[end1][end0] == 1:
                        logic[start1][start0], logic[end1][end0] = logic[end1][end0], ""
                        print(logic)
                        break
                    else:
                        print('Неверный ход!\n')
            else: print("Неверный ход!\n")
    else:
        while True:
            choice = input("Введите ход (позиция_вашей_фигуры позиция_куда_ее_передвинуть): ")
            start, end = choice.split(" ")
            
            #start1 - индедекс строки, start0 - индекс столбца
            start0, start1 = abc.index(start[0]), int(start[1])-1
            #end1 - индекс строки, end0 - индекс столбца
            end0, end1 = abc.index(end[0]), int(end[1])-1
            
            if logic[start1][start0] == 1: # Проверка пешки
                if start0-end0 == 0: #Ход прямо
                    if logic[end1][end0] == '' and abs(start1-end1) < 2: #Если клетка свободна и ход правильный
                        logic[start1][start0], logic[end1][end0] = logic[end1][end0], logic[start1][start0]
                        print(logic)
                        n += 1
                        break
                    else:
                        print("Неверный ход!\n")
                else: #Диагональный ход
                    if abs(start0-end0) < 2 and logic[end1][end0] == 0:
                        logic[end1][end0], logic[start1][start0] = logic[start1][start0], ""
                        print(logic)
                        break
                    else:
                        print('Неверный ход!\n')
            else: print("Неверный ход!\n")
