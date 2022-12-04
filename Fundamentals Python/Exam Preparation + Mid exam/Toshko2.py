
def card_actions(cards, lines):
    new_card = []
    for i in range(lines):
        new_card = input()
        if 'Add' in new_card:
            command, add_card = new_card.split(", ")
            if add_card not in cards:
                cards.append(add_card)
                print("Card successfully added")
            else:
                print("Card is already in the deck")
        if "Remove" in new_card:
            command, removed_card = new_card.split(", ")
            if command == 'Remove':
                if removed_card in cards:
                    cards.remove(removed_card)
                    print("Card successfully removed")
                else:
                    print("Card not found")
        if "Remove At" in new_card:
            command, index_removed_card = new_card.split(", ")
            if command == 'Remove At':
                if 0<=int(index_removed_card)<=len(cards):
                    cards.pop(int(index_removed_card))
                    print("Card successfully removed")
                else:
                    print("Index out of range")
        elif "Insert" in new_card:
            command, index, new_add_card = new_card.split(", ")
            if 0<=int(index)<=len(cards):
                if new_add_card in cards:
                    print("Card is already added")
                else:
                    cards.insert(int(index), new_add_card)
                    print("Card successfully added")
            else:
                print("Index out of range")


cards_deck= input().split(", ")
lines = int(input())
card_actions(cards_deck, lines)
print(', '.join(str(card) for card in cards_deck))