#win rate vs sum of first two cards
#output to console commented out for faster simulation times
#1-win% = (ties+losses)/simulations
import random 
from matplotlib import pyplot as plt

def draw_card():
    while(len(drawn_cards) != 52):
            card = random.randint(0,51)
            if not card in drawn_cards:
                drawn_cards.append(card)
                return card

def value(card):
    val = 0
    if "King" in card:
        val = 10
    elif "Queen" in card:
        val = 10
    elif "Jack" in card:
        val = 10
    elif "Ace" in card:
        val = 11
    else:
        val = int(card.split(" ", 1)[0])
    return val

def card_sum(card_tuple):
    value_tuple = ()
    for card in card_tuple:
        value_tuple = value_tuple + (value(card),)
    for x in range(len(card_tuple)):
        if "Ace" in card_tuple[x] and sum(value_tuple)>21:
            return sum(value_tuple)-10
    return sum(value_tuple)
        
card_order = []

for i in range(1,5):
    suit = ''
    if i == 1:
        suit = " of Clubs"
    elif i == 2:
        suit = " of Diamonds"
    elif i == 3:
        suit = " of Hearts"
    elif i ==4:
        suit = " of Spades"
        
    for j in range(1,14):
        if j == 1:
            j = "Ace"
        elif j == 11:
            j = "Jack"
        elif j == 12:
            j = "Queen"
        elif j ==13:
            j = "King"
        j = str(j) + suit
        card_order.append(j)

simulations = int(input("How many simulations do you want to do? "))
first_two_list = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
for x in range(simulations):
    win = 0
    drawn_cards = []
    user_cards = ()
    house_cards = ()
    
    hit_or_stand = ""
    draw_card()
    #print("You were dealt a", card_order[drawn_cards[0]])
    user_cards = user_cards + (card_order[drawn_cards[0]],)
    draw_card()
    house_cards = house_cards + (card_order[drawn_cards[1]],)
    draw_card()
    #print("You were dealt a", card_order[drawn_cards[2]])
    user_cards = user_cards + (card_order[drawn_cards[2]],)
    draw_card()
    house_cards = house_cards + (card_order[drawn_cards[3]],)
    #print("The dealer has a", card_order[drawn_cards[3]], "(", value(card_order[drawn_cards[3]]),")")  
    #print("You have a", card_order[drawn_cards[0]], "(", value(card_order[drawn_cards[0]]), ")"
          #"and a" , card_order[drawn_cards[2]], "(", value(card_order[drawn_cards[2]]), ")")
    first_two_sum = card_sum(user_cards)
    
    
    
    cards = 3



    
    while(True):
        if((card_sum(user_cards) >= 17 and card_sum(user_cards) <= 21) and card_sum(user_cards) == card_sum(house_cards)):
            #print("You have the same sum as the dealer. You are tied")
            break
        if(card_sum(user_cards) == 21):
            if(card_sum(house_cards)<17):
                while(card_sum(house_cards)<17):
                    draw_card()
                    cards+=1
                    house_cards = house_cards + (card_order[drawn_cards[cards]],)
                    #print("The dealer drew a", card_order[drawn_cards[cards]], "and has a total of", card_sum(house_cards))
                    if(card_sum(house_cards)>21):
                        #print("The dealer busted. You won")
                        win = 1
                        break
                    elif(card_sum(house_cards)==21):
                        #print("Dealer also has 21. It is a tie")
                        break
                    elif(card_sum(house_cards)>=17 and card_sum(house_cards)<21):
                        #print("You won")
                        win = 1
                        break
                break
        if card_sum(user_cards)<17:
            draw_card()
            cards+=1
            user_cards = user_cards + (card_order[drawn_cards[cards]],)
            #print("You were drawn a", card_order[drawn_cards[cards]], "You now have a total of" , card_sum(user_cards))
            if(card_sum(user_cards)>21):
                card_sum(user_cards)
                if(card_sum(user_cards)<21):
                    continue
                #print("You busted. The house wins")
                break
        else:
            #print("The dealer has a", card_order[drawn_cards[1]], "(", value(card_order[drawn_cards[1]]), ") "
              #"and a" , card_order[drawn_cards[3]], "(", value(card_order[drawn_cards[3]]), ") for a total of ", card_sum(house_cards))
            if card_sum(house_cards)>=17 and card_sum(house_cards)<=21:
                if card_sum(house_cards) > card_sum(user_cards):
                    #print("The dealer won.")
                    break
                elif card_sum(house_cards) < card_sum(user_cards):
                    #print("You won.")
                    win = 1
                    break
                else:
                    #print("You tied")
                    break
            if card_sum(house_cards) == 21 and card_sum(user_cards)<21:
                #print("The dealer has 21. The house wins")
                break            
            while(card_sum(house_cards)<17):
                draw_card()
                cards+=1
                house_cards = house_cards + (card_order[drawn_cards[cards]],)
                #print("The dealer drew a", card_order[drawn_cards[cards]], "for a total of", card_sum(house_cards))
                if(card_sum(house_cards)>21):
                    #print("The dealer busted. You won")
                    win = 1
                    break
                elif(card_sum(house_cards)<=21 and card_sum(house_cards)>=17):
                    if(card_sum(house_cards)>card_sum(user_cards)):
                        #print("The dealer won.")
                        break
                    elif(card_sum(house_cards)<card_sum(user_cards)):
                        #print("You won")
                        win = 1
                        break
                
            break
    first_two_list[first_two_sum-4].append(win)
    #print()

win_per_first2 = []
overall = 0
for x in range(len(first_two_list)):
    total = 0
    for y in range(len(first_two_list[x])):
        total += first_two_list[x][y]
        overall += first_two_list[x][y]
    win_per_first2.append((total/len(first_two_list[x])))

first_two = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
win_per = [0,.1,.2,.3,.4,.5,.6,.7,.8,.9,1]
plt.scatter(first_two,win_per_first2)
plt.xlabel("Sum of First Two Cards")
plt.ylabel("Win Percentage (Wins/Total)")
ax = plt.gca()
plt.xticks(first_two)
plt.yticks(win_per)

print("Overall win percentage" , round((overall/simulations), 4))