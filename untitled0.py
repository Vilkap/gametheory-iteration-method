def one(l):
    minrow = [min(i) for i in l] 
    k = [i for i in zip(*l)]
    maxcolumn = [max(i) for i in k]
    indrow = minrow.index(max(minrow)) #индекс максмин строки
    indcolumn = maxcolumn.index(min(maxcolumn)) #индекс минмакс столбца 
    minmaxrow = max(minrow)
    maxminrow = min(maxcolumn)
    return (f'минимальные значения строк: {minrow}\n'
            f'максимальные значения столбцов: {maxcolumn} \n'
            f'оптимальная стратегия для А = {indrow}\n'   
            f'оптимальная стратегия для B = {indcolumn}\n' 
            f'{l[indrow][indcolumn] = }') if minmaxrow == maxminrow  else  'нет седловой точки'
    
if __name__ == '__main__':
    print(one([[5, 4, 8, 9, 6, 8, 4, 5, 6],
                   [1, 6, 9, 4, 3, 6, 8, 2, 7]]))
    print(one([[1,2,3,4],[2,3,4,5]]))