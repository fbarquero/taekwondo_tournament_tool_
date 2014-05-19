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
    matches = []
    count = 0
    print "shuffled players:"
    print shuffled_players
    if len(shuffled_players) % 2 == 1:
        print "impar"
        matches.append(shuffled_players[count])
        count = 1
        while count != (len(shuffled_players)/2) + 1:
                matches.append([shuffled_players[count],shuffled_players[(len(shuffled_players))-count]])
                count += 1
    else:
        print "par"
        while count != len(shuffled_players)/2:
                matches.append([shuffled_players[count],shuffled_players[(len(shuffled_players)-1)-count]])
                count += 1
    print "matches:"
    print matches
    return matches


single_elimination_bracket_generation(["alonso","darian","michael","will", "papi"])


