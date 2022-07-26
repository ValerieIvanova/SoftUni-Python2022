cards = input().split()
shuffles = int(input())
for shuffle in range(shuffles):
    final_deck = []
    middle_of_the_deck = len(cards) // 2
    first_deck = cards[:middle_of_the_deck]
    second_deck = cards[middle_of_the_deck:]
    for i in range(len(first_deck)):
        final_deck.append(first_deck[i])
        final_deck.append(second_deck[i])
    cards = final_deck
print(cards)