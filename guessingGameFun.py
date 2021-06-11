secret = "monkey"
guess = ""

guess_count = 0
guess_limit = 3
gameOver = False

while guess != secret and not(gameOver):
    if guess_count < guess_limit:
        guess = input("guess what")
        guess_count += 1
    else:
        gameOver = True

if gameOver:
    print("out of guess, sucker!")
else:
    print("yeah!")