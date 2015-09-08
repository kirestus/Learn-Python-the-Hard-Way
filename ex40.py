import random

player_cash = 100
deck_of_cards = []
player_hand = []
dealer_hand = []
player_hand_value = 0

def suit_name(suit):
	if suit == 0:
		sname = 'Clubs'
	elif suit == 1:
		sname = 'Spades'
	elif suit == 2:
		sname = 'Hearts'
	elif suit == 3:
		sname = "Diamonds"
		
	return sname
	
def card_name(number):
	if number <= 10 and number > 1:
		return number
	elif number == 11:
		return ('J')
	elif number == 12:
		return ('Q')
	elif number == 13:
		return ('K')
	elif number == 1:
		return ('A')

def makedeck():
	suit = 0
	for i in range(0,4):
		next_card = 0
		for i in range(0,13):
			next_card += 1
			deck_of_cards.append("%s of %s" % (card_name(next_card),suit_name(suit)))
		suit += 1
	
def shuffledeck():
	random.shuffle(deck_of_cards)

def displaydeck():
	for i in deck_of_cards:
		print i;

def drawcard(towhom, numberofcards):
	while(numberofcards > 0):
		nextcard = deck_of_cards.pop(0)
		numberofcards -= 1
		if towhom == 'player':
			player_hand.append(nextcard)
		else:
			dealer_hand.append(nextcard)

def gamerounds():
	endround = 0
	while endround == 0:
		makedeck()
		shuffledeck()
		drawcard('player', 2)
		drawcard('dealer', 2)
		print "the player has %s" %player_hand
		print "the dealer has %s" %dealer_hand
		hitorstay()
		endround = 1;

def hitorstay():
	choice = raw_input("Do you want to hit or stay?")
	if choice == 'hit'or choice == '1' or choice == 'Hit':
		drawcard('player',1)
		print player_hand
		hitorstay()
	else:
		print "You stay with %s" % player_hand
gamerounds()
