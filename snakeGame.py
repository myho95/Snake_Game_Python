import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN, KEY_EXIT

curses.initscr()

window = curses.newwin(20, 60, 0, 0)

window.keypad(1)

curses.noecho()

curses.curs_set(0)

window.border(0)

window.nodelay(1)

snake = [(4, 10), (4, 9), (4, 8)]

food = (10, 30)

window.addch(food[0], food[1], "$")

key = KEY_RIGHT

while key != KEY_EXIT:
    event = window.getch()

    # Update window after 15 milliseconds
    window.timeout(150)

    prevKey = key

    key = event if event != -1 else prevKey

    head = snake[0]

    currentHeadY = head[0]

    currentHeadX = head[1]

    if(key == KEY_UP):
        currentHeadY = currentHeadY - 1

    if(key == KEY_DOWN):
        currentHeadY = currentHeadY + 1

    if(key == KEY_LEFT):
        currentHeadX = currentHeadX - 1

    if(key == KEY_RIGHT):
        currentHeadX = currentHeadX + 1

    if key in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]:
        snake.insert(0, (currentHeadY, currentHeadX))

        tail = snake.pop()

        window.addch(tail[0], tail[1], " ")

    # Rule: when snake touchs boundary or touch itself
    if(currentHeadY == 0 or currentHeadY == 19 or currentHeadX == 0 or currentHeadX == 59 or snake[0] in snake[1:]):
        exit()

    for s in snake:
        window.addch(s[0], s[1], "*")


curses.endwin()
