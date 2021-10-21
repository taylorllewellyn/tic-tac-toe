from graphics import *
def draw_x_or_o(i, h, v):  #player 1 is X. Player -1 is O. h and v are the horizontal and vertical position of 0, 1, or 2
    if i == 1:
        draw_x = Line(Point(10 + (h * 66), 10 + (v * 66)), Point(56 + (h * 66), 56 + (v * 66)))
        draw_x.setWidth(4)
        draw_x.draw(win)
        draw_x = Line(Point(10 + (h * 66), 56 + (v * 66)), Point(56 + (h * 66), 10 + (v * 66)))
        draw_x.setWidth(4)
        draw_x.draw(win)
    if i == -1:
        circle_center = Point(33 + (h * 66), 33 + (v * 66))
        draw_o = Circle(circle_center, 23)
        draw_o.setWidth(4)
        draw_o.draw(win)

def check_for_winner():
    for item in totals_dict.items():  #If any row, column, diag up, or diag down equals 3 or -3 then we have a winner
        if item[1] == 3:
            draw_winning_line(item[0])
            return('X')
        if item[1] == -3:
            return('O')
    return

def draw_winning_line(key):
    i = 0
    if key == 'diag_down':
        while i < 190:
            draw_line = Line(Point(5 + i, 5 + i), Point(5 + i + 2, 5 + i + 2))
            draw_line.setWidth(3)
            draw_line.setOutline('red')
            draw_line.draw(win)
            i = i + 2
            time.sleep(.01)
    if key == 'diag_up':
        while i < 190:
            draw_line = Line(Point(5 + i, 195 - i), Point(5 + i + 2, 195 - i - 2))
            draw_line.setWidth(3)
            draw_line.setOutline('red')
            draw_line.draw(win)
            i = i + 2
            time.sleep(.01)
    if key[0] == 'r':
        row_line = int(key[1])  #row 0, 1, or 2
        while i < 190:
            draw_line = Line(Point(5 + i, row_line * 66 + 33), Point(5 + i + 2, row_line * 66 + 33))  #Each row is 66 wide. 33 is half way. The 5 is so the line starts near the edge.
            draw_line.setWidth(3)
            draw_line.setOutline('red')
            draw_line.draw(win)
            i = i + 2
            time.sleep(.01)
    if key[0] == 'c':
        column_line = int(key[1])    #column 0, 1, or 2
        while i < 190:
            draw_line = Line(Point(column_line * 66 + 33, 5 + i), Point(column_line * 66 + 33, 5 + i + 2))  #Each column is 66 high. 33 is half way. The 5 is so the line starts near the edge.
            draw_line.setWidth(3)
            draw_line.setOutline('red')
            draw_line.draw(win)
            i = i + 2
            time.sleep(.01)
    if key == 'Cats':
        x = 25
        while x < 150:
            y = (((75 ** 2) - (x-100) ** 2) ** .5) + 100
            cir = Circle(Point(x, y), 4)
            cir.setFill('red')
            cir.setOutline('red')
            cir.draw(win)
            x = x + .1
            time.sleep(.0001)
            y = -(((75 ** 2) - (x-100) ** 2) ** .5) + 100
            cir = Circle(Point(x, y), 4)
            cir.setFill('red')
            cir.setOutline('red')
            cir.draw(win)
            x = x + .1
            time.sleep(.0001)

def play_game(starting_player):
    turn_count = 1
    if starting_player == 'x':
        i = 1
    else: i = -1
    while turn_count <= 9: #After 9 turns, it is a cats game. (No winner.)
        click_point = win.getMouse()
        h = int((click_point.getX() // 66)) #Returns 0, 1, or 2 to indicate the column clicked
        v = int((click_point.getY() // 66)) #Returns 0, 1, or 2 to indicate the row clicked

        hv_string = '{}{}'.format(h, v)
        if game_dict[hv_string] == 0:   #Check to see if cell has a value
            game_dict[hv_string] = i   #Assign cell a value of 1 for X and -1 for O player
            draw_x_or_o(i, h, v)
            if h == v:   #diag down the h and v values are equal. Record 1 or -1 if in diag down
                totals_dict['diag_down'] += i
            if h + v == 2:   #diag up the h and v sum to 2. Record 1 or -1if in diag up
                totals_dict['diag_up'] += i
            row_string = 'r{}'.format(v)  #record a 1 or -1 value for the row
            totals_dict[row_string] += i
            column_string = 'c{}'.format(h)  #record a 1 or -1 value for the column
            totals_dict[column_string] += i
            if check_for_winner() == 'X' or check_for_winner() == 'O':
                return(check_for_winner()) #Ends turn after winner
            i = i * -1  #switches player
            turn_count += 1
    draw_winning_line('Cats')
    return('cats')

game_running = True
# game loop
while game_running == True:
    game_dict = {'00':0, '10':0, '20':0, '01':0, '11':0, '21':0, '02':0, '12':0, '22':0}
    totals_dict = {'r0':0, 'r1':0, 'r2':0, 'c0':0, 'c1':0, 'c2':0, 'diag_down':0, 'diag_up':0}

    h = 0
    v = 0
    print("Would you like X or O to go first?")
    starting_player = input().lower()  #x or o

    win = GraphWin() #opens window
    # Game board setup. 2 horizontal and 2 vertical lines
    h_line1 = Line(Point(0, 66), Point(200, 66))
    h_line1.setWidth(3)
    h_line1.draw(win)
    h_line2 = Line(Point(0, 132), Point(200, 132))
    h_line2.setWidth(3)
    h_line2.draw(win)
    v_line1 = Line(Point(66, 0), Point(66, 200))
    v_line1.setWidth(3)
    v_line1.draw(win)
    v_line2 = Line(Point(132, 0), Point(132, 200))
    v_line2.setWidth(3)
    v_line2.draw(win)

    winner = play_game(starting_player)
    if winner == 'cats':
        print('Cats game. There is no winner')
    else: print('Player ' + winner + ' is the winner!')

    win.getMouse()
    win.close()
    print("Would you like to play again?")
    playagain = input().lower() #okay values start in an n or N for no. Anything else for yes.
    if playagain[0] == 'n':
        game_running = False
    
    
    


  