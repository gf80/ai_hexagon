print("""
-|_A_|_B_|_C_| 
1|_♟_|_♟_|_♟_| 
2|___|___|___| 
3|_♙_|_♙_|_♙_| 
""")

logic = [['♟','♟','♟'],
        ['_','_','_'],
        ['♙','♙','♙']]

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

            if logic[start1][start0] == '♙': # Проверка пешки
                if start0-end0 == 0: #Ход прямо
                    if logic[end1][end0] == '_' and abs(start1-end1) < 2: #Если клетка свободна и ход правильный
                        logic[start1][start0], logic[end1][end0] = logic[end1][end0], logic[start1][start0]
                        print(f"""
-|_A_|_B_|_C_| 
1|_{logic[0][0]}_|_{logic[0][1]}_|_{logic[0][2]}_| 
2|_{logic[1][0]}_|_{logic[1][1]}_|_{logic[1][2]}_| 
3|_{logic[2][0]}_|_{logic[2][1]}_|_{logic[2][2]}_| 
""")
                        n += 1
                        break
                    else:
                        print("Неверный ход!\n")
                else: #Диагональный ход
                    if abs(start0-end0) < 2 and logic[end1][end0] == '♟':
                        logic[end1][end0], logic[start1][start0] = logic[start1][start0], "_"
                        print(f"""
-|_A_|_B_|_C_| 
1|_{logic[0][0]}_|_{logic[0][1]}_|_{logic[0][2]}_| 
2|_{logic[1][0]}_|_{logic[1][1]}_|_{logic[1][2]}_| 
3|_{logic[2][0]}_|_{logic[2][1]}_|_{logic[2][2]}_| 
""")
                        n+=1
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
            
            if logic[start1][start0] == '♟': # Проверка пешки
                if start0-end0 == 0: #Ход прямо
                    if logic[end1][end0] == '_' and abs(start1-end1) < 2: #Если клетка свободна и ход правильный
                        logic[start1][start0], logic[end1][end0] = logic[end1][end0], logic[start1][start0]
                        print(f"""
-|_A_|_B_|_C_| 
1|_{logic[0][0]}_|_{logic[0][1]}_|_{logic[0][2]}_| 
2|_{logic[1][0]}_|_{logic[1][1]}_|_{logic[1][2]}_| 
3|_{logic[2][0]}_|_{logic[2][1]}_|_{logic[2][2]}_| 
""")
                        n += 1
                        break
                    else:
                        print("Неверный ход!\n")
                else: #Диагональный ход
                    if abs(start0-end0) < 2 and logic[end1][end0] == '♙':
                        logic[end1][end0], logic[start1][start0] = logic[start1][start0], "_"
                        print(f"""
-|_A_|_B_|_C_| 
1|_{logic[0][0]}_|_{logic[0][1]}_|_{logic[0][2]}_| 
2|_{logic[1][0]}_|_{logic[1][1]}_|_{logic[1][2]}_| 
3|_{logic[2][0]}_|_{logic[2][1]}_|_{logic[2][2]}_| 
""")                    
                        n+=1
                        break
                    else:
                        print('Неверный ход!\n')
            else: print("Неверный ход!\n")
