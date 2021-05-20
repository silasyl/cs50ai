from nim import train, play
import sys

def main():

    # Number of training times
    if len(sys.argv) == 2:
        games = int(sys.argv[1])
        ai = train(games)
    else:
        ai = train()

    # Play
    play(ai)


if __name__ == "__main__":
    main()
