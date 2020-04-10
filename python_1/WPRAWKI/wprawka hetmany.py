def queens(board_size):
    def queen_cols(k): #queen_cols, której wynikiem jest lista 
        if k == 0: #wszystkich sposobów rozmieszczenia k hetmanów w k pierwszych kolumnach szachownicy.
            return empty_board()
        else:
            return [adjoin_position(new_row, k, rest_of_queens)
                        for rest_of_queens in queen_cols(k - 1)
                        for new_row in range(1, board_size + 1)
                        if  safe_to_add(rest_of_queens, new_row, k)]
    return queen_cols(board_size)

# empty_board reprezentującą pusty zbiór pozycji
def empty_board(board_size):
    możliwości = []
    ustawienie = [] #może zbierać tuple
    rzedy = []
    for i in range(board_size):
        rzedy.append(i)
    wsp = list(zip(range(board_size),rzedy))
    return wsp

print(empty_board(4))



    #wspolrz = zip(rzedy,kolumny)
    #return możliwości.append(ustawienie.append(wspolrz))

#adjoin_position dodającą do zbioru pozycji nową pozycję określoną przez wiersz i kolumnę
def adjoin_position(row, column, position):
    raise NotImplementedError


#określającą dla danego zbioru pozycji czy hetman ustawiony w k-tej kolumnie i wierszu
#new_row szachuje któregoś z pozostałych hetmanów. 
#def safe_to_add(position, new_row, new_column):
   # for i in range(position):
    #    if 
