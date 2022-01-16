import random

deck = []

def init():
    global deck
    types = ["Clubs", "Spades", "Hearts", "Diamonds"]
    numbers = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

    for type in types:
        for num in numbers:
            deck.append((num, type))

def orderValue(card):
    if card[0] == "A":
        return 1
    if card[0] == "J":
        return 11
    if card[0] == "Q":
        return 12
    if card[0] == "K":
        return 13
    return card[0]

def orderType(card):
    if card[1] == "Spades":
        return 0
    if card[1] == "Hearts":
        return 1
    if card[1] == "Clubs":
        return 2
    if card[1] == "Diamonds":
        return 3

def sortHand(e):
    return 13 * orderType(e) + orderValue(e)

def sort(hand: list = None):
    if hand != None:
        hand.sort(key=sortHand)
        return hand
    else:
        global deck
        deck.sort(key=sortHand)

def getDeck():
    global deck
    return deck

def checkCard(pos):
    global deck
    if not(0 <= pos < 52):
        return deck[0]
    return deck[pos]

def dealCard(pos):
    global deck
    retVal = ""
    if not(0 <= pos < len(deck)):
        retVal = deck[0]
    else:
        retVal = deck[pos]
    deck.remove(retVal)
    return retVal

def clean():
    init()

def deal(num):
    global deck
    cards = []
    for i in range(num):
        cards.append(deck[0])
        deck.remove(deck[0])
    return cards

def shuffle(num = 1):
    if(num <= 0):
        return
    global deck
    temp = []
    for i in range(num):
        for i in range(52):
            index = random.randrange(0,52-i,1)
            temp.append(deck[index])
            deck.remove(deck[index])
        deck = temp

def value(card):
    if card[0] == "A":
        return 1
    if card[0] == "J":
        return 10
    if card[0] == "Q":
        return 10
    if card[0] == "K":
        return 10
    return card[0]

def main():
    global deck
    init()
    for i in range(7):
        shuffle()
    print(deck)
    cards = deal(5)
    print(cards)
    clean()
    print(deck)

if __name__ == "__main__":
    main()
