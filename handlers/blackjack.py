import random
import time

from create_bot import bot
from base import check_score, update_score, check_bet, update_bet

card_value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] * 4
card_face = {11: "J", 12: "Q", 13: "K", 14: "A"}
fc_vals = {"J": 10, "Q": 10, "K": 10, "A": (1, 11)}
suits=["♠️","♣️","♥️","♦️"]

def generate_cards():
    cards=[]
    for value in card_value:
        for suit in suits:
            if value in card_face:
                _card=(card_face[value],suit)
            else:
                _card=(value,suit)
            cards.append(_card)
    return cards

def deal_card(cards):
    i = random.randint(0, len(cards)-1)
    card = cards[i]
    cards.pop(i)
    return card, cards
 
def deal2(cards):
    card1, cards = deal_card(cards)
    card2, cards = deal_card(cards)
    you = [card1, card2]
    return you, cards

def get_hand_val(hand):
    val = 0
    for card in hand:  
        if card[0] in fc_vals:
            if card[0] != 'A':
                val += fc_vals[card[0]]
            else:
                if val + fc_vals[card[0]][1] > 21:
                    val += fc_vals[card[0]][0]
                else:
                    val += fc_vals[card[0]][1]
        else:
            val += int(card[0])
    return val

# TODO нужно обновить способ добора карт, можно реализовать это через inlinekeyboard
def hit_me(hand, cards):
    hit, cards = deal_card(cards)
    hand.append(hit)
    new_hand_val = get_hand_val(hand)
    return hand, new_hand_val, cards

def dealer_turn(dealer_hand, cards):
    while get_hand_val(dealer_hand) < 17:
        dealer_hand, _, cards = hit_me(dealer_hand, cards)
    if get_hand_val(dealer_hand) > 21:
        return True, dealer_hand, cards

    else:
        return False, dealer_hand, cards

def check_winer(dealer_hand, you_hand, message, cards, score,bet):
    if get_hand_val(you_hand) == 21 and get_hand_val(dealer_hand) == 21:
        bot.send_message(message.chat.id,"<b>Tie!</b>", parse_mode = 'html')
    elif get_hand_val(you_hand) == 21 and any(card[0] == 'A' for card in you_hand):
        bot.send_message(message.chat.id,"<b>You</b> has <b>blackjack</b>. You wins!", parse_mode = 'html')
        score += bet*3
        update_score(message, score)
        bot.send_message(message.chat.id,"💰")
    elif get_hand_val(dealer_hand) == 21 and any(card[0] == 'A' for card in dealer_hand): 
        score -= bet*3
        update_score(message, score)
        bot.send_message(message.chat.id,"<b>Dealer</b> has <b>blackjack</b>. Dealer wins.", parse_mode = 'html')
    else:
        if get_hand_val(dealer_hand) > get_hand_val(you_hand):
            score -= bet
            update_score(message, score)
            bot.send_message(message.chat.id,"<b>Dealer wins.</b>", parse_mode = 'html')
        elif get_hand_val(dealer_hand) < get_hand_val(you_hand):
            score += bet
            update_score(message, score)
            bot.send_message(message.chat.id,"<b>You wins!</b>", parse_mode = 'html')
        else:
            bot.send_message(message.chat.id,"<b>Tie!</b>", parse_mode = 'html')

def format_cards(cards):
    return ' '.join([f"{card_face.get(card[0], card[0])}{card[1]} " for card in cards])

def check_player_score(message):
    score = check_score(message)
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id,f"You have <b>{score} $</b>", parse_mode='html')

# TODO переписать алгоритм изменения ставки на универсальный
def update_bet_amount(message, amount):
    bet = check_bet(message) + amount
    bot.delete_message(message.chat.id, message.message_id)
    update_bet(message, bet)
    bot.send_message(message.chat.id, f"You bet = <b>{check_bet(message)} 🫥</b>", parse_mode='html')

def plus_50_bet(message):
    update_bet_amount(message, +50)

def plus_100_bet(message):
    update_bet_amount(message, +100)

def minus_50_bet(message):
    update_bet_amount(message, -50)

def minus_100_bet(message):
    update_bet_amount(message, -100)

def play_blackjack(message):
    bot.delete_message(message.chat.id, message.message_id)
    score = check_score(message)
    bet = check_bet(message)
    if bet < 0 or bet > score and score > 0:
        bot.send_message(message.chat.id,'Please, change you bet to start')
    else:
        if score >0:
            cards = generate_cards()
            you_hand, cards = deal2(cards)
            dealer_hand, cards = deal2(cards)
            bot.send_message(message.chat.id,f"""
<b>Dealer</b> hand - {format_cards(dealer_hand)} = <b>{get_hand_val(dealer_hand)}</b>
<b>You</b>    hand - {format_cards(you_hand)} = <b>{get_hand_val(you_hand)}</b>

starting score - <b>{score} $</b>
Bet - <b>{bet} 🫥</b>
            """, parse_mode = 'html')
            check_winer(dealer_hand,you_hand,message, cards, score, bet)
            time.sleep(3)

        elif score <=0:
            bot.send_message(message.chat.id,"You no hawe chips for playing \n Please wait")
            time.sleep(10)
            score = 100
            update_score(message, score)
            bot.send_message(message.chat.id,'💸')
            bot.send_message(message.chat.id,"+100 You agan can play!")

def register_handlers_blackjack(bot):
    bot.register_message_handler(play_blackjack, commands = ['PlayBJ'])
    bot.register_message_handler(check_player_score, commands = ['score'])
    bot.register_message_handler(plus_50_bet, commands = ['+50'])
    bot.register_message_handler(plus_100_bet, commands = ['+100'])
    bot.register_message_handler(minus_50_bet, commands = ['-50'])
    bot.register_message_handler(minus_100_bet, commands = ['-100']) 
    #bot.register_message_handler(play_blackjack, commands = ['Play_BJ'])