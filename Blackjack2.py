import random

points = 1000
game_done = False
while not game_done:


    def win():
        global points
        points = (bet * 2) + points

    def lose():
        global points
        points = points

    def tie():
        global points
        points = bet + points

    def blackjack():
        global points
        points = (bet * 2.5) + points



    betinput = input(f"You have {points} chips. How many would you like to bet?:")
    bet = int(betinput)
    if bet > points:
        exit()
    print(f"you bet {bet} chips")
    points = points - bet




    deck = (["2", "2", "2", "2", "3", "3", "3", "3", "4", "4", "4", "4", "5", "5", "5", "5", "6", "6", "6", "6", "7", "7", "7", "7", "8", "8", "8", "8", "9", "9", "9", "9", "10", "10", "10", "10", "Jack", "Jack", "Jack", "Jack", "Queen", "Queen", "Queen", "Queen", "King", "King", "King", "King", "Ace", "Ace", "Ace", "Ace"])

    random.shuffle(deck)

    draw1 = deck.pop(0)
    if draw1 == "Ace" or draw1 == "8":
        print(f"You drew an {draw1}")
    else:
        print(f"You drew a {draw1}")
    draw2 = deck.pop(0)
    draw3 = deck.pop(0)
    if draw3 == "Ace" or draw3 == "8":
        print(f"You drew an {draw3}")
    else:
        print(f"You drew a {draw3}")
    draw4 = deck.pop(0)
    if draw4 == "Ace" or draw4 == "8":
        print(f"Dealer drew an {draw4}")
    else:
        print(f"Dealer drew a {draw4}")


    if draw1 == "Ace" and draw3 == "Ace":
        double_ace = input("Would you like your points to be 2 or 12?:")
        if double_ace == "2":
            player = 2
        elif double_ace == "12":
            player = 12
        else:
            print("Please enter 2,12,or 22")
    elif draw1 == "Ace" and draw3 in ["Jack", "Queen", "King", "10"]:
        print("Blackjack! You Win!")
        player = 21
        blackjack()
        continue
    elif draw3 == "Ace" and draw1 in ["Jack", "Queen", "King", "10"]:
        print("Blackjack! You Win!")
        player = 21
        blackjack()
        continue
    elif draw1 == "Ace":
        ace = input("Would you like your ace to be 1 or 11 points?:")
        if ace == "1":
            player = 1 + int(draw3)
        elif ace == "11":
            player = 11 + int(draw3)
    elif draw3 == "Ace":
        ace = input("Would you like your ace to be 1 or 11 points?:")
        if ace == "1":
            player = 1 + int(draw1)
        elif ace == "11":
            player = 11 + int(draw1)
    elif draw1 in ["Jack", "Queen", "King"] and draw3 in ["Jack", "Queen", "King"]:
        player = 20
    elif draw1 in ["Jack", "Queen", "King"]:
        player = 10 + int(draw3)
    elif draw3 in ["Jack", "Queen", "King"]:
        player = 10 + int(draw1)
    else:
        player = int(draw1) + int(draw3)

    if draw4 == "Ace":
        card = 11
    elif draw4 in ["Jack", "Queen", "King"]:
        card = 10
    else:
        card = int(draw4)

    print(f"You have {player} points")
    print(f"The dealer has {card} points")


    def stand():
        print("You have chosen to Stand")
        if draw2 == "Ace" or draw2 == "8":
            print(f"Dealer revealed an {draw2}")
        else:
            print(f"Dealer revealed a {draw2}")
        if draw2 == "Ace" and draw4 == "Ace":
            dealer = 22
        elif draw2 == "Ace" and draw4 in ["Jack", "Queen", "King", "10"]:
            print("Blackjack! Dealer Wins!")
            lose()
        elif draw4 == "Ace" and draw2 in ["Jack", "Queen", "King", "10"]:
            print("Blackjack! Dealer Wins!")
            lose()
        elif draw2 == "Ace":
            dealer = 11 + int(draw4)
        elif draw4 == "Ace":
            dealer = 11 + int(draw2)
        elif draw2 in ["Jack", "Queen", "King"] and draw4 in ["Jack", "Queen", "King"]:
            dealer = 20
        elif draw2 in ["Jack", "Queen", "King"]:
            dealer = 10 + int(draw4)
        elif draw4 in ["Jack", "Queen", "King"]:
            dealer = 10 + int(draw2)
        else:
            dealer = int(draw2) + int(draw4)

        print(f"The dealer has {dealer} points")
        if any(d > 21 for d in [dealer]):
            print("Dealer busts, you win!")
            win()
        elif any(d >= 17 for d in [dealer]):
            if any(d < player for d in [dealer]):
                print("You Win!")
                win()
            elif any(d > player for d in [dealer]):
                print("You Lose!")
                win()
            else:
                print("It's a tie!")
                tie()

        if dealer < 17:
            draw8 = deck.pop(0)
            if draw8 == "Ace" or draw8 == "8":
                print(f"Dealer drew an {draw8}")
            else:
                print(f"Dealer drew a {draw8}")
            if draw8 == "Ace":
                card2 = 11
            elif draw8 in ["Jack", "Queen", "King"]:
                card2 = 10
            else:
                card2 = int(draw8)
            dealer_total = card2 + dealer
            print(f"The dealer now has {dealer_total} points")
            if any(d > 21 for d in [dealer_total]):
                print("Dealer busts, you win!")
                win()
            elif any(d >= 17 for d in [dealer_total]):
                if any(d < player for d in [dealer_total]):
                    print("You Win!")
                    win()
                elif any(d > player for d in [dealer_total]):
                    print("You Lose!")
                    lose()
                else:
                    print("It's a tie!")
                    tie()
            if dealer_total < 17:
                draw9 = deck.pop(0)
                if draw9 == "Ace" or draw9 == "8":
                    print(f"Dealer drew an {draw9}")
                else:
                    print(f"Dealer drew a {draw9}")
                if draw9 == "Ace":
                    card3 = 11
                elif draw9 in ["Jack", "Queen", "King"]:
                    card3 = 10
                else:
                    card3 = int(draw9)
                dealer_total2 = card3 + dealer_total
                print(f"The dealer now has {dealer_total2} points")
                if any(d > 21 for d in [dealer_total2]):
                    print("Dealer busts, you win!")
                    win()
                elif any(d >= 17 for d in [dealer_total2]):
                    if any(d < player for d in [dealer_total2]):
                        print("You Win!")
                        win()
                    elif any(d > player for d in [dealer_total2]):
                        print("You Lose!")
                        lose()
                    else:
                        print("It's a tie!")
                        tie()
                if dealer_total2 < 17:
                    draw10 = deck.pop(0)
                    if draw10 == "Ace" or draw10 == "8":
                        print(f"Dealer drew an {draw10}")
                    else:
                        print(f"Dealer drew a {draw10}")
                    if draw10 == "Ace":
                        card4 = 11
                    elif draw10 in ["Jack", "Queen", "King"]:
                        card4 = 10
                    else:
                        card4 = int(draw10)
                    dealer_total3 = card4 + dealer_total2
                    print(f"The dealer now has {dealer_total3} points")

                    if any(d > 21 for d in [dealer_total3]):
                        print("Dealer busts, you win!")
                        win()
                    elif any(d >= 17 for d in [dealer_total3]):
                        if any(d < player for d in [dealer_total3]):
                            print("You Win!")
                            win()
                        elif any(d > player for d in [dealer_total3]):
                            print("You Lose!")
                            lose()
                        else:
                            print("It's a tie!")
                            tie()


    def stand1():
        print("You have chosen to Stand")
        if draw2 == "Ace" or draw2 == "8":
            print(f"Dealer revealed an {draw2}")
        else:
            print(f"Dealer revealed a {draw2}")
        if draw2 == "Ace" and draw4 == "Ace":
            dealer = 22
        elif draw2 == "Ace" and draw4 in ["Jack", "Queen", "King", "10"]:
            print("Blackjack! Dealer Wins!")
            lose()
        elif draw4 == "Ace" and draw2 in ["Jack", "Queen", "King", "10"]:
            print("Blackjack! Dealer Wins!")
            lose()
        elif draw2 == "Ace":
            dealer = 11 + int(draw4)
        elif draw4 == "Ace":
            dealer = 11 + int(draw2)
        elif draw2 in ["Jack", "Queen", "King"] and draw4 in ["Jack", "Queen", "King"]:
            dealer = 20
        elif draw2 in ["Jack", "Queen", "King"]:
            dealer = 10 + int(draw4)
        elif draw4 in ["Jack", "Queen", "King"]:
            dealer = 10 + int(draw2)
        else:
            dealer = int(draw2) + int(draw4)

        print(f"The dealer has {dealer} points")
        if any(d > 21 for d in [dealer]):
            print("Dealer busts, you win!")
            win()
        elif any(d >= 17 for d in [dealer]):
            if any(d < new_total for d in [dealer]):
                print("You Win!")
                win()
            elif any(d > new_total for d in [dealer]):
                print("You Lose!")
                lose()
            else:
                print("It's a tie!")
                tie()

        if dealer < 17:
            draw8 = deck.pop(0)
            if draw8 == "Ace" or draw8 == "8":
                print(f"Dealer drew an {draw8}")
            else:
                print(f"Dealer drew a {draw8}")
            if draw8 == "Ace":
                card2 = 11
            elif draw8 in ["Jack", "Queen", "King"]:
                card2 = 10
            else:
                card2 = int(draw8)
            dealer_total = card2 + dealer
            print(f"The dealer now has {dealer_total} points")
            if any(d > 21 for d in [dealer_total]):
                print("Dealer busts, you win!")
                win()
            elif any(d >= 17 for d in [dealer_total]):
                if any(d < new_total for d in [dealer_total]):
                    print("You Win!")
                    win()
                elif any(d > new_total for d in [dealer_total]):
                    print("You Lose!")
                    lose()
                else:
                    print("It's a tie!")
                    tie()
            if dealer_total < 17:
                draw9 = deck.pop(0)
                if draw9 == "Ace" or draw9 == "8":
                    print(f"Dealer drew an {draw9}")
                else:
                    print(f"Dealer drew a {draw9}")
                if draw9 == "Ace":
                    card3 = 11
                elif draw9 in ["Jack", "Queen", "King"]:
                    card3 = 10
                else:
                    card3 = int(draw9)
                dealer_total2 = card3 + dealer_total
                print(f"The dealer now has {dealer_total2} points")
                if any(d > 21 for d in [dealer_total2]):
                    print("Dealer busts, you win!")
                    win()
                elif any(d >= 17 for d in [dealer_total2]):
                    if any(d < new_total for d in [dealer_total2]):
                        print("You Win!")
                        win()
                    elif any(d > new_total for d in [dealer_total2]):
                        print("You Lose!")
                        lose()
                    else:
                        print("It's a tie!")
                        tie()
                if dealer_total2 < 17:
                    draw10 = deck.pop(0)
                    if draw10 == "Ace" or draw10 == "8":
                        print(f"Dealer drew an {draw10}")
                    else:
                        print(f"Dealer drew a {draw10}")
                    if draw10 == "Ace":
                        card4 = 11
                    elif draw10 in ["Jack", "Queen", "King"]:
                        card4 = 10
                    else:
                        card4 = int(draw10)
                    dealer_total3 = card4 + dealer_total2
                    print(f"The dealer now has {dealer_total3} points")

                    if any(d > 21 for d in [dealer_total3]):
                        print("Dealer busts, you win!")
                        win()
                    elif any(d >= 17 for d in [dealer_total3]):
                        if any(d < new_total for d in [dealer_total3]):
                            print("You Win!")
                            win()
                        elif any(d > new_total for d in [dealer_total3]):
                            print("You Lose!")
                            lose()
                        else:
                            print("It's a tie!")
                            tie()

    def stand2():
        print("You have chosen to Stand")
        if draw2 == "Ace" or draw2 == "8":
            print(f"Dealer revealed an {draw2}")
        else:
            print(f"Dealer revealed a {draw2}")
        if draw2 == "Ace" and draw4 == "Ace":
            dealer = 22
        elif draw2 == "Ace" and draw4 in ["Jack", "Queen", "King", "10"]:
            print("Blackjack! Dealer Wins!")
            lose()
        elif draw4 == "Ace" and draw2 in ["Jack", "Queen", "King", "10"]:
            print("Blackjack! Dealer Wins!")
            lose()
        elif draw2 == "Ace":
            dealer = 11 + int(draw4)
        elif draw4 == "Ace":
            dealer = 11 + int(draw2)
        elif draw2 in ["Jack", "Queen", "King"] and draw4 in ["Jack", "Queen", "King"]:
            dealer = 20
        elif draw2 in ["Jack", "Queen", "King"]:
            dealer = 10 + int(draw4)
        elif draw4 in ["Jack", "Queen", "King"]:
            dealer = 10 + int(draw2)
        else:
            dealer = int(draw2) + int(draw4)

        print(f"The dealer has {dealer} points")
        if any(d > 21 for d in [dealer]):
            print("Dealer busts, you win!")
            win()
        elif any(d >= 17 for d in [dealer]):
            if any(d < final_hit for d in [dealer]):
                print("You Win!")
                win()
            elif any(d > final_hit for d in [dealer]):
                print("You Lose!")
                lose()
            else:
                print("It's a tie!")
                tie()

        if dealer < 17:
            draw8 = deck.pop(0)
            if draw8 == "Ace" or draw8 == "8":
                print(f"Dealer drew an {draw8}")
            else:
                print(f"Dealer drew a {draw8}")
            if draw8 == "Ace":
                card2 = 11
            elif draw8 in ["Jack", "Queen", "King"]:
                card2 = 10
            else:
                card2 = int(draw8)
            dealer_total = card2 + dealer
            print(f"The dealer now has {dealer_total} points")
            if any(d > 21 for d in [dealer_total]):
                print("Dealer busts, you win!")
                win()
            elif any(d >= 17 for d in [dealer_total]):
                if any(d < final_hit for d in [dealer_total]):
                    print("You Win!")
                    win()
                elif any(d > final_hit for d in [dealer_total]):
                    print("You Lose!")
                    lose()
                else:
                    print("It's a tie!")
                    tie()
            if dealer_total < 17:
                draw9 = deck.pop(0)
                if draw9 == "Ace" or draw9 == "8":
                    print(f"Dealer drew an {draw9}")
                else:
                    print(f"Dealer drew a {draw9}")
                if draw9 == "Ace":
                    card3 = 11
                elif draw9 in ["Jack", "Queen", "King"]:
                    card3 = 10
                else:
                    card3 = int(draw9)
                dealer_total2 = card3 + dealer_total
                print(f"The dealer now has {dealer_total2} points")
                if any(d > 21 for d in [dealer_total2]):
                    print("Dealer busts, you win!")
                    win()
                elif any(d >= 17 for d in [dealer_total2]):
                    if any(d < final_hit for d in [dealer_total2]):
                        print("You Win!")
                        win()
                    elif any(d > final_hit for d in [dealer_total2]):
                        print("You Lose!")
                        lose()
                    else:
                        print("It's a tie!")
                        tie()
                if dealer_total2 < 17:
                    draw10 = deck.pop(0)
                    if draw10 == "Ace" or draw10 == "8":
                        print(f"Dealer drew an {draw10}")
                    else:
                        print(f"Dealer drew a {draw10}")
                    if draw10 == "Ace":
                        card4 = 11
                    elif draw10 in ["Jack", "Queen", "King"]:
                        card4 = 10
                    else:
                        card4 = int(draw10)
                    dealer_total3 = card4 + dealer_total2
                    print(f"The dealer now has {dealer_total3} points")

                    if any(d > 21 for d in [dealer_total3]):
                        print("Dealer busts, you win!")
                        win()
                    elif any(d >= 17 for d in [dealer_total3]):
                        if any(d < final_hit for d in [dealer_total3]):
                            print("You Win!")
                            win()
                        elif any(d > final_hit for d in [dealer_total3]):
                            print("You Lose!")
                            lose()
                        else:
                            print("It's a tie!")
                            tie()

    def stand3():
        print("You have chosen to Stand")
        if draw2 == "Ace" or draw2 == "8":
            print(f"Dealer revealed an {draw2}")
        else:
            print(f"Dealer revealed a {draw2}")
        if draw2 == "Ace" and draw4 == "Ace":
            dealer = 22
        elif draw2 == "Ace" and draw4 in ["Jack", "Queen", "King", "10"]:
            print("Blackjack! Dealer Wins!")
            lose()
        elif draw4 == "Ace" and draw2 in ["Jack", "Queen", "King", "10"]:
            print("Blackjack! Dealer Wins!")
            lose()
        elif draw2 == "Ace":
            dealer = 11 + int(draw4)
        elif draw4 == "Ace":
            dealer = 11 + int(draw2)
        elif draw2 in ["Jack", "Queen", "King"] and draw4 in ["Jack", "Queen", "King"]:
            dealer = 20
        elif draw2 in ["Jack", "Queen", "King"]:
            dealer = 10 + int(draw4)
        elif draw4 in ["Jack", "Queen", "King"]:
            dealer = 10 + int(draw2)
        else:
            dealer = int(draw2) + int(draw4)

        print(f"The dealer has {dealer} points")
        if any(d > 21 for d in [dealer]):
            print("Dealer busts, you win!")
            win()
        elif any(d >= 17 for d in [dealer]):
            if any(d < final_hit2 for d in [dealer]):
                print("You Win!")
                win()
            elif any(d > final_hit2 for d in [dealer]):
                print("You Lose!")
                lose()
            else:
                print("It's a tie!")
                tie()

        if dealer < 17:
            draw8 = deck.pop(0)
            if draw8 == "Ace" or draw8 == "8":
                print(f"Dealer drew an {draw8}")
            else:
                print(f"Dealer drew a {draw8}")
            if draw8 == "Ace":
                card2 = 11
            elif draw8 in ["Jack", "Queen", "King"]:
                card2 = 10
            else:
                card2 = int(draw8)
            dealer_total = card2 + dealer
            print(f"The dealer now has {dealer_total} points")
            if any(d > 21 for d in [dealer_total]):
                print("Dealer busts, you win!")
                win()
            elif any(d >= 17 for d in [dealer_total]):
                if any(d < final_hit2 for d in [dealer_total]):
                    print("You Win!")
                    win()
                elif any(d > final_hit2 for d in [dealer_total]):
                    print("You Lose!")
                    lose()
                else:
                    print("It's a tie!")
                    tie()
            if dealer_total < 17:
                draw9 = deck.pop(0)
                if draw9 == "Ace" or draw9 == "8":
                    print(f"Dealer drew an {draw9}")
                else:
                    print(f"Dealer drew a {draw9}")
                if draw9 == "Ace":
                    card3 = 11
                elif draw9 in ["Jack", "Queen", "King"]:
                    card3 = 10
                else:
                    card3 = int(draw9)
                dealer_total2 = card3 + dealer_total
                print(f"The dealer now has {dealer_total2} points")
                if any(d > 21 for d in [dealer_total2]):
                    print("Dealer busts, you win!")
                    win()
                elif any(d >= 17 for d in [dealer_total2]):
                    if any(d < final_hit2 for d in [dealer_total2]):
                        print("You Win!")
                        win()
                    elif any(d > final_hit2 for d in [dealer_total2]):
                        print("You Lose!")
                        lose()
                    else:
                        print("It's a tie!")
                        tie()
                if dealer_total2 < 17:
                    draw10 = deck.pop(0)
                    if draw10 == "Ace" or draw10 == "8":
                        print(f"Dealer drew an {draw10}")
                    else:
                        print(f"Dealer drew a {draw10}")
                    if draw10 == "Ace":
                        card4 = 11
                    elif draw10 in ["Jack", "Queen", "King"]:
                        card4 = 10
                    else:
                        card4 = int(draw10)
                    dealer_total3 = card4 + dealer_total2
                    print(f"The dealer now has {dealer_total3} points")

                    if any(d > 21 for d in [dealer_total3]):
                        print("Dealer busts, you win!")
                        win()
                    elif any(d >= 17 for d in [dealer_total3]):
                        if any(d < final_hit2 for d in [dealer_total3]):
                            print("You Win!")
                            win()
                        elif any(d > final_hit2 for d in [dealer_total3]):
                            print("You Lose!")
                            lose()
                        else:
                            print("It's a tie!")
                            tie()

    def hit():
        print("You have chosen to Hit")
        draw5 = deck.pop(0)
        if draw5 == "Ace" or draw5 == "8":
            print(f"You drew an {draw5}")
        else:
            print(f"You drew a {draw5}")
        if draw5 == "Ace":
            ace = input("Would you like your Ace to be 1 or 11 points?")
            if ace == "1":
                hit1 = 1
            elif ace == "11":
                hit1 = 11
        elif draw5 in ["Jack", "Queen", "King"]:
            hit1 = 10
        else:
            hit1 = int(draw5)
        global new_total
        new_total = hit1 + player
        print(f"You now have {new_total} points")
        if new_total > 21:
            print("Bust! You Lose!")
            lose()
        elif new_total <= 21:
            hit2 = input("Would you like to Hit or Stand?:")
            if hit2 == "Hit" or hit2 == "hit":
                print("You have chosen to Hit")
                draw6 = deck.pop(0)
                if draw6 == "Ace" or draw6 == "8":
                    print(f"You drew an {draw6}")
                else:
                    print(f"You drew a {draw6}")
                if draw6 == "Ace":
                    ace2 = input("Would you like your Ace to be 1 or 11 points?:")
                    if ace2 == "1":
                        new_total2 = 1
                    elif ace2 == "11":
                        new_total2 = 2
                elif draw6 in ["Jack", "Queen", "King"]:
                    new_total2 = 10
                else:
                    new_total2 = int(draw6)
                global final_hit
                final_hit = new_total2 + new_total
                print(f"You now have {final_hit} points")
                if final_hit > 21:
                    print("Bust! You Lose!")
                    lose()
                elif final_hit < 21:
                    hit3 = input("Would you like to Hit or Stand?:")
                    if hit3 == "Hit" or hit3 == "hit":
                        print("You have chosen to Hit")
                        draw7 = deck.pop(0)
                        if draw7 == "Ace" or draw7 == "8":
                            print(f"You drew an {draw7}")
                        else:
                            print(f"You drew a {draw7}")
                        if draw7 == "Ace":
                            ace3 = input("Would you like your Ace to be 1 or 11 points?:")
                            if ace3 == "1":
                                new_total3 = 1
                            elif ace3 == "11":
                                new_total3 = 2
                        elif draw7 in ["Jack", "Queen", "King"]:
                            new_total3 = 10
                        else:
                            new_total3 = int(draw7)
                            global final_hit2
                        final_hit2 = new_total3 + final_hit
                        print(f"You now have {final_hit2} points")
                        if final_hit2 > 21:
                            print("Bust! You Lose!")
                            lose()
                        elif final_hit2 <= 21:
                            print("Turn over. Dealer Draws")
                            stand3()
                    elif hit3 == "Stand" or hit3 == "stand":
                        stand2()
            elif hit2 == "Stand" or hit2 == "stand":
                stand1()




    def hit_stand():
        move = input("Would you like to Hit or Stand?:")
        if move == "Hit" or move == "hit":
            hit()
        elif move == "Stand" or move == "stand":
            stand()
        else:
            print("Please enter Hit or Stand")
            hit_stand()
    hit_stand()




