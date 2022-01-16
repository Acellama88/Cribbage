from ftplib import parse150
import Cards

def count15(hand: list):
    total = 0
    size = len(hand)
    #count 2 cards
    for i in range(size):
        for j in range(i + 1, size):
            if (Cards.value(hand[i]) + Cards.value(hand[j])) == 15:
                total += 2
    #count 3 cards
    for i in range(size):
        for j in range(i + 1, size):
            for k in range(j + 1, size):
                if (Cards.value(hand[i]) + Cards.value(hand[j]) + Cards.value(hand[k])) == 15:
                    total += 2
    #count 4 cards
    for i in range(size):
        for j in range(i + 1, size):
            for k in range(j + 1, size):
                for l in range(k + 1, size):
                    if (Cards.value(hand[i]) + Cards.value(hand[j]) + Cards.value(hand[k]) + Cards.value(hand[l])) == 15:
                        total += 2
    #count 5 cards
    if (Cards.value(hand[0]) + Cards.value(hand[1]) + Cards.value(hand[2]) + Cards.value(hand[3]) + Cards.value(hand[4])) == 15:
        total += 2
    return total

def countPairs(hand: list):
    total = 0
    size = len(hand)
    #count pairs of cards
    for i in range(size):
        for j in range(i + 1, size):
            if (hand[i][0] == hand[j][0]):
                total += 2
    return total

def countFlush(hand, common):
    size = len(hand)
    base = hand[0][1]
    #count flush
    for i in range(1, size):
        if hand[i][1] != base:
            return 0
    if common[1] == base:
        return 5
    return 4

def countKnobs(hand, common):
    if common[0] == "J":
        return 2
    for i in range(len(hand)):
        if hand[i][0] == "J" and hand[i][1] == common[1]:
            return 1
    return 0

def countRuns(hand: list):
    hand.sort(key=Cards.orderValue)
    size = len(hand)
    total = 0
    prev1 = Cards.orderValue(hand[1]) - 1
    prev2 = Cards.orderValue(hand[2]) - 1
    prev3 = Cards.orderValue(hand[3]) - 1
    prev4 = Cards.orderValue(hand[4]) - 1
    #check 5 card run
    if (Cards.orderValue(hand[0]) == Cards.orderValue(hand[1]) - 1) and (Cards.orderValue(hand[1]) == Cards.orderValue(hand[2]) - 1) and (Cards.orderValue(hand[2]) == Cards.orderValue(hand[3]) - 1) and (Cards.orderValue(hand[3]) == Cards.orderValue(hand[4]) - 1):
        return 5
    #check 4 card run
    for i in range(size):
        for j in range(i + 1, size):
            for k in range(j + 1, size):
                for l in range(k + 1, size):
                    if (Cards.orderValue(hand[i]) == Cards.orderValue(hand[j]) - 1) and (Cards.orderValue(hand[j]) == Cards.orderValue(hand[k]) - 1) and (Cards.orderValue(hand[k]) == Cards.orderValue(hand[l]) - 1):
                        total += 4
    if(total > 0):
        return total
    #check 3 card run
    for i in range(size):
        for j in range(i + 1, size):
            for k in range(j + 1, size):
                    if (Cards.orderValue(hand[i]) == Cards.orderValue(hand[j]) - 1) and (Cards.orderValue(hand[j]) == Cards.orderValue(hand[k]) - 1):
                        total += 3
    return total

def strToCard(s):
    keeps = ["A", "J", "Q", "K"]
    types = ["C", "H", "S", "D"]
    fullTypes = ["Clubs", "Hearts", "Spades", "Diamonds"]
    num = s[0]
    type = s[1]
    if(num == "1" and type == "0"):
        num = 10
        type = s[2]
    if not(num in keeps):
        num = int(num)
    loc = types.index(type)
    type = fullTypes[loc]
    return (num, type)

def getScore(hand: list, common):
    temp = hand.copy()
    total = countKnobs(temp,common)
    total += countFlush(temp,common)
    temp.append(common)
    total += count15(temp)
    total += countPairs(temp)
    total += countRuns(temp)
    return total

def main():
    Cards.init()
    strHand = input("What cards do you have (comma seperated, 5 total, '4H,2D,JS,...')?\r\n")
    print("\r\nScore: Removed Card\r\n")
    hand = []
    tokens = strHand.split(",")
    for i in range(len(tokens)):
        card = strToCard(tokens[i])
        loc = Cards.deck.index(card)
        hand.append(Cards.dealCard(loc))
    
    scores = []
    #calculate
    for i in range(len(hand)):
        #remove card from hand
        tempRemove = hand[i]
        hand.remove(tempRemove)
        total = 0
        for j in range(len(Cards.deck)):
            common = Cards.checkCard(j)
            total += getScore(hand, common)
        scores.append(total)
        hand.insert(i,tempRemove)
    high = 0
    highloc = 0
    for i in range(len(scores)):
        if(scores[i] > high):
            high = scores[i]
            highloc = i
        print(f"{scores[i]}: {hand[i][0]}-{hand[i][1]}")
    print(f"\r\nToss {hand[highloc]}!")

def main2():
    Cards.init()
    strHand = input("What cards do you have (comma seperated, 6 total, '4H,2D,JS,...')?\r\n")
    print("\r\nScore: Removed Cards\r\n")
    hand = []
    tokens = strHand.split(",")
    for i in range(len(tokens)):
        card = strToCard(tokens[i])
        loc = Cards.deck.index(card)
        hand.append(Cards.dealCard(loc))
    
    scores = []
    #calculate
    for i in range(len(hand)):
        for j in range(i +1, len(hand)):
            #remove card from hand
            tempRemove2 = hand[j]
            tempRemove1 = hand[i]
            hand.remove(tempRemove2)
            hand.remove(tempRemove1)
            total = 0
            for k in range(len(Cards.deck)):
                common = Cards.checkCard(k)
                total += getScore(hand, common)
            scores.append((total, tempRemove1, tempRemove2))
            hand.insert(i,tempRemove1)
            hand.insert(j,tempRemove2)
    high = 0
    highloc = 0
    for i in range(len(scores)):
        if(scores[i][0] > high):
            high = scores[i][0]
            highloc = i
        print(f"{scores[i]}")
    print(f"\r\nToss {scores[highloc][1]} and {scores[highloc][2]}")
    cmnCard = input("What is the Common Card?\r\n")
    cmnCard = strToCard(cmnCard)
    hand.remove(scores[highloc][1])
    hand.remove(scores[highloc][2])
    print(f"\r\nTotal Score: {getScore(hand,cmnCard)}")

if __name__ == "__main__":
    main2()