import random
from enum import Enum
from collections import Counter
from typing import Optional

# Enums for dealing the Board
class Street(Enum):
    FLOP = "flop"
    TURN = "turn"
    RIVER = "river"

# Deck of Cards
deck = ['AS','2S','3S','4S','5S','6S','7S','8S','9S','10S','JS','QS','KS',
        'AC','2C','3S','4C','5C','6C','7C','8C','9C','10C','JC','QC','KC',
        'AH','2H','3H','4H','5H','6H','7H','8H','9H','10H','JH','QH','KH',
        'AD','2D','3D','4D','5D','6D','7D','8D','9D','10D','JD','QD','KD']

# Global Variables
cardsLeft = 52
remainingDeck = deck.copy()
noPlayers = 2
playerHands = [[None] * 2 for _ in range(noPlayers)]
theBoard = ['','','','','']

# Possible Poker Hands

# Four of a Kind
def has_foak(playerHand) -> bool:
    combined_cards = playerHand + theBoard
    ranks = [card[:-1] for card in combined_cards]
    rank_counts = Counter(ranks)
    return any(count >= 4 for count in rank_counts.values())

# Three of a Kind
def has_toak(playerHand) -> bool:
    combined_cards = playerHand + theBoard
    ranks = [card[:-1] for card in combined_cards]
    
    rank_counts = Counter(ranks)
    return any(count >= 3 for count in rank_counts.values())

# Pair
def has_pair(playerHand) -> bool:
    combined_cards = playerHand + theBoard
    ranks = [card[:-1] for card in combined_cards]
    
    rank_counts = Counter(ranks)
    return any(count >= 2 for count in rank_counts.values())

# Check for best hand
def bestHand(playerHand) -> Optional[str]:
    handChecks = [(has_toak, "Three of a Kind"),
                  (has_pair, "Pair")]
    
    for hand_func, hand_name in handChecks:
        if hand_func(playerHand):
            return hand_name
    
    return "High Card"

# Check all hands for best hand
def playerChecks():
    for i in range(len(playerHands)):
        print("Player " + str(i) + " has " + bestHand(playerHands[i]))
    return

# Reset the deck
def deckReset():
    global remainingDeck
    global cardsLeft
    remainingDeck = deck.copy()
    cardsLeft = 52
    return

# Deal all cards
def dealAll():
    while (cardsLeft > 0):
        dealHands()
    return

# Random Card Picker
def randomCard():
    shuffle = random.randrange(0,65535,random.randint(1,9))
    return shuffle % cardsLeft

# Deal a card and remove it from the deck
def dealCard():
    global cardsLeft
    global remainingDeck
    
    if cardsLeft == 0:
        return "No cards left, reset the deck"
    
    card = remainingDeck[randomCard()]
    cardsLeft = cardsLeft - 1
    remainingDeck.remove(card)
    return card

# Deal hands to players
def dealHands():
    global noPlayers
    global playerHands
    for i in range(2): # Deal two cards
        for j in range(noPlayers): # Deal one card to each player at a time
            playerHands[j][i] = dealCard()     
    return playerHands

# Burn Card (Deal without showing players)
def burnCard():
    dealCard()
    print("Card burn")
    return

# Community Cards
def communityCards(street: Street):
    global theBoard
    burnCard()
    
    # Perform different deals
    if street == Street.FLOP:
        for i in range(3):
            theBoard[i] = dealCard()
    if street == Street.RIVER:
        theBoard[3] = dealCard()
    if street == Street.TURN:
        theBoard[4] = dealCard()
    
    return theBoard

# Deal a full community board
def fullBoard():
    communityCards(Street.FLOP)
    communityCards(Street.TURN)
    communityCards(Street.RIVER)
    return theBoard

        
    
    

    

        
    



    
    

