import numpy as np
import sys

def one(l):
    minrow = [min(i) for i in l]#минимальные значения строки
    k = [i for i in zip(*l)]#транспонированная матрица(чтобы столбцы стали строками)
    maxcolumn = [max(i) for i in k]#максимальные значения столбцов
    indrow = minrow.index(max(minrow)) #индекс максмин строки
    indcolumn = maxcolumn.index(min(maxcolumn)) #индекс минмакс столбца 
    #ниже переменные нужны только для вывода
    minmaxrow = max(minrow)
    maxminrow = min(maxcolumn)
    return (f'минимальные значения строк: {minrow}\n\
максимальные значения столбцов: {maxcolumn}\n\
оптимальная стратегия для А = {indrow = }\n\
оптимальная стратегия для B = {indcolumn = }\n\
цена игры = {l[indrow][indcolumn] = }') if minmaxrow == maxminrow  else  'нет седловой точки'
    

def itermethod(l):
    lt = np.copy(l.T)#транспонированная матрица
    
    itr = int(input('введите количество итераций: '))
    start = int(input('начальная стратегия игрока А: '))
    start = start - 1#тк отсчет идет с 1, а не с 0
    if start > len(l): sys.exit('выбранной стратегии не существует')
    gamma1 = []#минимумы строк/номер партии
    gamma2 = []#максимумы столбцов/номер партии
    lstart = np.copy(l[start])
    Δk = []#видал какой символ 
    k = 1 #номер партии
    while(itr != 0):
        
        if k == 1:
            b = l[start].argmin()#начальный индекс для B
            start = lt[l[start].argmin()].argmax()#вычисляем следущий индекс
            blist = lt[b]#строка для b
            gamma1.append(lstart.min())
            gamma2.append(lt[b].max())
            Δk.append(abs(lstart.min() - lt[b].max()))#было лень менять местами, поэтому abs
        else:
            lstart += l[start]
            b = lstart.argmin()#следующий индекс для B
            blist += lt[b]
            lt = np.copy(l.T)
            start = blist.argmax()
            gamma1.append(np.round((lstart.min()/k),3))
            gamma2.append(np.round((blist.max()/k),3))
            Δk.append(abs(np.round((lstart.min()/k) - blist.max()/k,3)))#аналогично abs
        k += 1
        itr -=1
        #print(lstart)
    print(f'{max(gamma1) = }')
    print(f'{min(gamma2) = }')
    print(f'{Δk[-1] = }')


def main():
    l = np.array([[3,6,8,9,1,0,2,4,5],
              [6,8,4,7,6,9,9,7,5],
              [6,3,2,3,6,9,4,5,7],
              [8,9,5,9,6,8,4,7,5],
              [2,1,3,2,4,5,7,9,8],
              [6,3,2,5,4,7,8,9,6],
              [7,8,4,5,6,9,6,5,2],
              [0,2,7,8,4,5,9,6,3],
              [7,8,5,2,7,4,7,5,2]])

    print(one(l))
    if one(l) == 'нет седловой точки':
        print(itermethod(l))  

if __name__ == '__main__':
    main()