from graphics import *
import time
import random
import os
import sys
import numpy as np

def create_matrix():
    list1 = [0,0,0,0,0,0,0,0,0]
    list2 = [0,0,0,0,0,0,0,0,0]
    list3 = [0,0,0,0,0,0,0,0,0]
    list4 = [0,0,0,0,0,0,0,0,0]
    list5 = [0,0,0,0,0,0,0,0,0]
    list6 = [0,0,0,0,0,0,0,0,0]
    list7 = [0,0,0,0,0,0,0,0,0]
    list8 = [0,0,0,0,0,0,0,0,0]
    list9 = [0,0,0,0,0,0,0,0,0]

    matrix = [list1,list2,list3,list4,list5,list6,list7,list8,list9]
    return matrix

def print_matrix(matrix):
    win = GraphWin(width = 540,height = 540)
    for i in range(0,9):
        line = Line(Point(i*60,0),Point(i*60,540))
        line.draw(win)
        line = Line(Point(0,60*i),Point(540,60*i))
        line.draw(win)
    for i in range(0,4):
        line = Line(Point(i*180-1,0),Point(i*180-1,540))
        line.draw(win)
        line = Line(Point(i*180+1,0),Point(i*180+1,540))
        line.draw(win)
        line = Line(Point(0,180*i-1),Point(540,180*i-1))
        line.draw(win)
        line = Line(Point(0,180*i+1),Point(540,180*i+1))
        line.draw(win)
    for i in range(0,9):
        for j in range(0,9):
            if matrix[i][j]!=0:
                label = Text(Point(30+60*i,30+60*j),str(matrix[i][j]))
                label.setSize(20)
                label.draw(win)

def add_square_initial(matrix,a,b):
    square = [1,2,3,4,5,6,7,8,9]
    for i in range(0,3):
        for j in range(0,3):
            matrix[a+i][b+j] = add_number_initial(matrix,i+a,j+b,square)
            square.remove(matrix[a+i][b+j])
    return matrix 

def add_number_initial(matrix,a,b,square):
    list1 = [1,2,3,4,5,6,7,8,9]
    list2 = [1,2,3,4,5,6,7,8,9]
    for i in range(0,9):
        if matrix[a][i] != 0 and i != b:
            list1.remove(matrix[a][i])
        if matrix[i][b] != 0 and i!= a:
            list2.remove(matrix[i][b])
    temp_list = list(set.intersection(set(list1),set(list2)))
    list3 = list(set.intersection(set(temp_list),set(square)))
    j = random.randint(0,len(list3)-1)
    return list3[j]

def add_square(matrix,a,b,count):
    square = [1,2,3,4,5,6,7,8,9]
    for i in range(0,3):
        for j in range(0,3):
            list1 = [1,2,3,4,5,6,7,8,9]
            list2 = [1,2,3,4,5,6,7,8,9]
            for k in range(0,9):
                if matrix[a+i][k] != 0 and k != b+j:
                    list1.remove(matrix[a+i][k])
                if matrix[k][b+j] != 0 and k!= a+i:
                    list2.remove(matrix[k][b+j])
            temp_list = list(set.intersection(set(list1),set(list2)))
            list3 = list(set.intersection(set(temp_list),set(square)))
            if len(list3) > 0:
                m = random.randint(0,len(list3)-1)
                matrix[a+i][b+j] = list3[m]
                square.remove(matrix[a+i][b+j])
            else:
                if count < 100:
                    return add_square(matrix,a,b,count+1)
                elif count < 200:
                    if a==6 and b==3:
                        add_square(matrix,3,6,count+1)
                        return add_square(matrix,a,b,count+1)
                    elif a==3 and b==6:
                        add_square(matrix,3,0,count+1)
                        return add_square(matrix,a,b,count+1)
                    elif a==3 and b==0:
                        add_square(matrix,0,3,count+1)
                        return add_square(matrix,a,b,count+1)
                    elif a==0 and b==3:
                        add_square(matrix,6,0,count+1)
                        return add_square(matrix,a,b,count+1)
                    elif a==6 and b==0:
                        add_square(matrix,0,6,count+1)
                        return add_square(matrix,a,b,count+1)
                else:
                    matrix = create_matrix()
                    matrix = first_three(matrix)
                    if a==6 and b==3:
                        matrix = add_square(matrix,0,6,count)
                        matrix = add_square(matrix,6,0,count)
                        matrix = add_square(matrix,0,3,count)
                        matrix = add_square(matrix,3,0,count)
                        matrix = add_square(matrix,3,6,count)
                        return add_square(matrix,a,b,count+1)
                    elif a==3 and b==6:
                        matrix = add_square(matrix,0,6,count)
                        matrix = add_square(matrix,6,0,count)
                        matrix = add_square(matrix,0,3,count)
                        matrix = add_square(matrix,3,0,count)
                        return add_square(matrix,a,b,count+1)
                    elif a==3 and b==0:
                        matrix = add_square(matrix,0,6,count)
                        matrix = add_square(matrix,6,0,count)
                        matrix = add_square(matrix,0,3,count)
                        return add_square(matrix,a,b,count+1)
                    elif a==0 and b==3:
                        matrix = add_square(matrix,0,6,count)
                        matrix = add_square(matrix,6,0,count)
                        return add_square(matrix,a,b,count+1)
                    elif a==6 and b==0:
                        matrix = add_square(matrix,0,6,count)
                        return add_square(matrix,a,b,count+1)
                    else:
                        return add_square(matrix,a,b,count+1)                  
                        
    return matrix       

def first_three(matrix):
    matrix = add_square_initial(matrix,0,0)
    matrix = add_square_initial(matrix,3,3)
    matrix = add_square_initial(matrix,6,6)
    return matrix

def generate_board():
    global count
    count = 0
    matrix = create_matrix()
    matrix = first_three(matrix)
    matrix = add_square(matrix,0,6,count)
    matrix = add_square(matrix,6,0,count)
    matrix = add_square(matrix,0,3,count)
    matrix = add_square(matrix,3,0,count)
    matrix = add_square(matrix,3,6,count)
    matrix = add_square(matrix,6,3,count)
    print_matrix(matrix)
    return matrix

def solve_matrix(matrix):
    solution = matrix
    for i in range(0,9):
        for j in range(0,9):
            if solution[i][j] == 0:
                solution[i][j] = [1,2,3,4,5,6,7,8,9]
            else:
                solution[i][j] = [solution[i][j]]
    count = 0
    for i in range(0,9):
        for j in range(0,9):
            count = count + len(solution[i][j])
    while count!=81:
        for i in range(0,9):
            for j in range(0,9):
                if len(solution[i][j])>1:
                    solution[i][j] = solve_one_cell(solution,i,j)
        count = 0
        for i in range(0,9):
            for j in range(0,9):
                count = count + len(solution[i][j])
    for i in range(0,9):
        for j in range(0,9):
            solution[i][j] = int(solution[i][j][0])
    return solution 
                

def solve_one_cell(solution,a,b):
    offset_a = a%3
    offset_b = b%3
    square = [1,2,3,4,5,6,7,8,9]
    for i in range(0,3):
        for j in range(0,3):
            if len(solution[i+a-offset_a][j+b-offset_b])==1:
                square.remove(int(solution[i+a-offset_a][j+b-offset_b][0]))
    row_list = [1,2,3,4,5,6,7,8,9]
    col_list = [1,2,3,4,5,6,7,8,9]  
    for i in range(0,9):
        if len(solution[a][i])==1 and solution[a][i]!=0 and i!=b:
            row_list.remove(int(solution[a][i][0]))
        if len(solution[i][b])==1 and solution[i][b] != 0 and i!=a:
            col_list.remove(int(solution[i][b][0]))
    temp_list = list(set.intersection(set(row_list),set(col_list)))
    sol_list = list(set.intersection(set(temp_list),set(square)))
    return sol_list


    

practice_matrix = [[3,0,4,0,0,2,5,0,1],[6,0,5,0,1,3,0,8,2],[7,1,2,0,8,0,3,0,6],[9,2,8,0,0,7,0,5,3],[4,0,7,0,3,5,0,1,9],[5,3,0,0,2,0,7,4,0],[1,0,0,3,5,0,8,2,4],[2,0,0,4,0,8,1,6,7],[0,0,6,2,0,1,9,0,5]]

print_matrix(practice_matrix)
solution = solve_matrix(practice_matrix)
print_matrix(solution)



    


