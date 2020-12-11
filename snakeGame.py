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


def food(number):
    food_error = False
    while True:
        foodY = random.randint(1, 13)
        foodX = random.randint(1, 28)
        window.addch(foodY, foodX, "o")
        for s in snake:
            if (foodY, foodX) == s:
                food_error = True
                break
        if food_error != False:
            continue
        else:
            break
    return (foodY, foodX)


(foodY, foodX) = food(1)


key = KEY_RIGHT

while key != KEY_EXIT:

    event = window.getch()

# Update window after 15 milliseconds
    window.timeout(200)

# The direction the snake moves
    prevKey = key
    key = event if event in [KEY_DOWN, KEY_LEFT,
                             KEY_UP, KEY_RIGHT] else prevKey

    head = snake[0]
    currentHeadY = head[0]
    currentHeadX = head[1]

# When the snake turns its head
    if {key, prevKey} == {KEY_UP, KEY_DOWN} or {key, prevKey} == {KEY_LEFT, KEY_RIGHT}:
        key = prevKey

# When move the snake:
    if key == KEY_UP:
        currentHeadY = currentHeadY - 1

    if key == KEY_DOWN:
        currentHeadY = currentHeadY + 1

    if key == KEY_LEFT:
        currentHeadX = currentHeadX - 1

    if key == KEY_RIGHT:
        currentHeadX = currentHeadX + 1

    if key in [KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT]:
        snake.insert(0, (currentHeadY, currentHeadX))
# When the snake eats food:
    if foodY == currentHeadY and foodX == currentHeadX:
        snake_length = len(snake)
        if snake_length > 30:
            break
        (foodY, foodX) = food(2)

    else:
        tail = snake.pop()
        window.addch(tail[0], tail[1], " ")

# Rule: when snake touchs boundary or touch itself
    snake_body = snake[1:]
    if currentHeadY in {0, 14} or currentHeadX in {0, 29}:
        break
    if snake[0] in snake_body:
        break
# Draw the snake:
    for s in snake:
        window.addch(s[0], s[1], "*")


curses.endwin()
