def picture(board):
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("--"*7)


def input_step(player):
    valid = False
    while not valid:
        answer = input("ТВОЙ ВЫБОР " + player+"? ")
        try:
            answer = int(answer)
        except:
            print("ЧТО-ТО НЕ ТАК!?")
            continue
        if answer >= 1 and answer <= 9:
            if (str(board[answer-1]) not in "XO"):
                board[answer-1] = player
                valid = True
            else:
                print("ОШИБКА, ТОВАРИЩ!")
        else:
            print("ПОПРОБУЙ ЧИСЛА, ТОВАРИЩ, ДО 9.")


def win_or_not(board):
    check = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
             (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in check:
        if str(board[i[0]]) == str(board[i[1]]) == str(board[i[2]]):
            return board[i[0]]
    return False


def start(board):
    counter = 0
    flag = True
    while flag:
        picture(board)
        if counter % 2 == 0:
            input_step("X")
        else:
            input_step("O")
        counter += 1
        if counter > 4:
            tmp = win_or_not(board)
            if tmp:
                print(tmp, "ПОВЕЗЛО!")
                flag = False
                break
        if counter == 9:
            print("НИКТО НЕ ВЫИГРАЛ!")
            break
    picture(board)


board = list(range(1, 10))
start(board)
