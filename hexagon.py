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
            choice = input("Введите ход за белых (позиция_вашей_фигуры позиция_куда_ее_передвинуть): ")
            start, end = choice.split(" ")

            #start1 - индедекс строки, start0 - индекс столбца
            start0, start1 = abc.index(start[0].upper()), int(start[1])-1
            #end1 - индекс строки, end0 - индекс столбца
            end0, end1 = abc.index(end[0].upper()), int(end[1])-1

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

    if logic[0].count('♟') == 0 and logic[1].count('♟') == 0 and logic[2].count('♟') == 0: #Если больше нет черных пешек
        print("Белые победили!")
        break
    elif logic[0][0] == '♙' or logic[0][1] == '♙' or logic[0][2] == '♙': #Если черные дошли до конца
        print('Белые победили!')
        break
    flag = 0 # Есть ли ходы для черных пешек
    for i in range(3):
        for j in range(3):
            if logic[i][j] == '♟':
                if j == 0:
                    if logic[i+1][j] == "_" or logic[i+1][j+1] == "♙":
                        flag = 1
                        break
                elif j == 1:
                    if logic[i+1][j] == "_" or logic[i+1][j+1] == "♙" or logic[i+1][j-1]=="♙":
                        flag = 1
                        break
                else:
                    if logic[i+1][j] == "_" or logic[i+1][j-1]=="♙":
                        flag = 1
                        break
    if flag == 0:
        print("Черные победили!")
        break


    else:
        while True:
            choice = input("Введите ход за черных (позиция_вашей_фигуры позиция_куда_ее_передвинуть): ")
            start, end = choice.split(" ")
            
            #start1 - индедекс строки, start0 - индекс столбца
            start0, start1 = abc.index(start[0].upper()), int(start[1])-1
            #end1 - индекс строки, end0 - индекс столбца
            end0, end1 = abc.index(end[0].upper()), int(end[1])-1
            
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

    if logic[0].count('♙') == 0 and logic[1].count('♙') == 0 and logic[2].count('♙') == 0: #Если больше нет белых пешек
        print("Черные победили!")
        break
    elif logic[2][0] == '♟' or logic[2][1] == '♟' or logic[2][2] == '♟': #Если черные дошли до конца
        print('Черные победили!')
        break
    flag = 0 #Есть ли ходы для белых пешек
    for i in range(3):
        for j in range(3):
            if logic[i][j] == '♙':
                if j == 0:
                    if logic[i-1][j] == "_" or logic[i-1][j+1] == "♟":
                        flag = 1
                        break
                elif j == 1:
                    if logic[i-1][j] == "_" or logic[i-1][j+1] == "♟" or logic[i-1][j-1]=="♟":
                        flag = 1
                        break
                else:
                    if logic[i-1][j] == "_" or logic[i-1][j-1]=="♟":
                        flag = 1
                        break
    if flag == 0:
        print("Белые победили!")
        break
