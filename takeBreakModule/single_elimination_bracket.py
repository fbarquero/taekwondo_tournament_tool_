__author__ = 'Mordigan'
import random


def single_elimination_bracket_generation(players):
   match_maker(shuffle_players(players))


def shuffle_players(players):
    print "players :"
    print players
    amount_of_players = len(players)-1
    while amount_of_players != 0:
        random_generated = random.randint(0,3)
        aux_player = players[random_generated]
        players[random_generated] = players[amount_of_players]
        players[amount_of_players] = aux_player
        amount_of_players -= 1
    print "Shuffled list"
    print players
    return players

def match_maker(shuffled_players):
    # Object that will represents the bracket
    bracket = []
    # Represents the round matches
    matches = []
    # Number of matches in the first round
    byes = 0
    # Number of rounds in the bracket
    rounds = 0

    count = 0
    print "shuffled players:"
    print shuffled_players
    if is_power_of_two(len(shuffled_players)):
       while count != len(shuffled_players)/2:
                matches.append([shuffled_players[count],shuffled_players[(len(shuffled_players)-1)-count]])
                count += 1
    else:
        print "needs to calculate byes"
    print "matches:"
    print matches
    return matches

def is_power_of_two(number):
    return (number & (number-1) == 0) and (number != 0)

def get_exponent_base_two(number):
    exponent = 0
    while number > 1:
        number /= 2
        exponent += 1
    return exponent

#single_elimination_bracket_generation(["alonso", "darian", "michael", "lunita"])
print get_exponent_base_two(64)


