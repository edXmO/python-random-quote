import random


def primary():

    f = open("python-random-quote/quotes.txt")
    quotes = f.readlines()
    # Added cleanQuotes, which is an array without the \n (newline) character
    cleanQuotes = []
    for elem in range(0, len(quotes) - 1):
        cleanQuotes.append(quotes[elem].rstrip("\n"))
    print(cleanQuotes)
    f.close()
    last = 13
    rnd = random.randint(0, last)
    # Added printing another quote
    print(cleanQuotes[rnd] + " " + cleanQuotes[rnd + 1])


if __name__ == "__main__":
    primary()
