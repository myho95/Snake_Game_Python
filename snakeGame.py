import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN, KEY_EXIT
import random
curses.initscr()

window = curses.newwin(15, 30, 0, 0)

window.keypad(1)

curses.noecho()

curses.curs_set(0)

window.border(0)


window.nodelay(1)
# Make a starter snake:
snake = [(1, 3), (1, 2), (1, 1)]


# Make food
foodY = random.randint(1, 13)
foodX = random.randint(1, 28)
window.addch(foodY, foodX, "o")


key = KEY_RIGHT

while key != KEY_EXIT:

    event = window.getch()

# Update window after 15 milliseconds
    window.timeout(200)

    prevKey = key
    key = event if event != -1 else prevKey

    head = snake[0]
    currentHeadY = head[0]
    currentHeadX = head[1]

# When move the snake:
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
# When the snake eats food:
    if foodY == currentHeadY and foodX == currentHeadX:
        snake_length = len(snake)
        if snake_length > 30:
            break
        foodY = random.randint(1, 13)
        foodX = random.randint(1, 28)
        window.addch(foodY, foodX, "o")

    else:
        tail = snake.pop()
        window.addch(tail[0], tail[1], " ")

    # Rule: when snake touchs boundary or touch itself
    if currentHeadY == 0 or currentHeadY == 14 or currentHeadX == 0 or currentHeadX == 29 or snake[0] in snake[1:]:
        break

    for s in snake:
        window.addch(s[0], s[1], "*")


curses.endwin()
