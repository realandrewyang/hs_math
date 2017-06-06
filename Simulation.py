import math
import random
import statistics

Cards=[]

#Each card is defined as a linked list and assigned two values, the first for the suit and the second for the number
#Cards is the linked list that contains each individual card
for i in range(1,5):
    for j in range(1,14):
        #This generates a new card to add to the end of the list until all 52 cards have been added to the deck
        Cards.append([i,j])

#This function draws three unique cards
def DrawThree():
    Card1=Cards[random.randrange(0,52)]

    Card2=Cards[random.randrange(0,52)]

    while Card2==Card1:
        Card2=Cards[random.randrange(0,52)]

    Card3=Cards[random.randrange(0,52)]

    while Card3==Card2 or Card3==Card1:
        Card3=Cards[random.randrange(0,52)]

    return [Card1,Card2,Card3]

#This is the core process of the simulation
def Simulate():

    #Give the player three lives    
    Lives=3
    Money=0

    #Ensure after every iteration that they player still has lives left
    while Lives>0:

        #Draw three cards
        #Created a linked list with the shown cards
        ThreeCards=DrawThree()
        ShownCards=[]

        #After the second card is revealed, there is only one last guess before the cards are redrawn
        while Lives>0 and len(ShownCards)<=2:
            #Random guess
            Guess=[random.randrange(1,5),random.randrange(1,14)]

            #Ensure that the random guess is not the same as a card that has already been revealed
            if len(ShownCards)==1:
                while Guess==ShownCards[0]:
                    Guess=[random.randrange(1,5),random.randrange(1,14)]
            elif len(ShownCards)==2:
                while Guess==ShownCards[0] or Guess==ShownCards[1]:
                    Guess=[random.randrange(1,5),random.randrange(1,14)]

            #The conditions for guessing an ace and guessing a non-ace are different. This block of code checks to see if lives are lost and/or how much money is won
            if Guess[1]==1:
                if ThreeCards[len(ShownCards)][1]==1:
                    Money=Money+3
                else:
                    Lives=Lives-1
            else:            
                if Guess[0]==ThreeCards[len(ShownCards)][0] and Guess[1]!=ThreeCards[len(ShownCards)][1]:
                    Money=Money+1
                elif Guess[1]==ThreeCards[len(ShownCards)][1] and Guess[0]!=ThreeCards[len(ShownCards)][0]:
                    Money=Money+1
                elif Guess[0]==ThreeCards[len(ShownCards)][0] and Guess[1]==ThreeCards[len(ShownCards)][1]:
                    Money=Money+10
                elif ThreeCards[len(ShownCards)][1]!=1:
                    Lives=Lives-1
                else:
                    Lives=0
            #Add the most recently picked card to the list of revealed cards
            ShownCards.append(ThreeCards[len(ShownCards)])
    #Output the winnings
    return Money

Collector=[]

for i in range(0,10000):
    Collector.append(Simulate())

print ("Average Winnings",statistics.mean(Collector))
