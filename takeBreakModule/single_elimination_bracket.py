__author__ = 'Mordigan'
import random
import math


def single_elimination_bracket_generation(players):
    match_maker(shuffle_players(players))


def shuffle_players(players):
    amount_of_players = len(players) - 1
    while amount_of_players != 0:
        random_generated = random.randint(0, amount_of_players)
        aux_player = players[random_generated]
        players[random_generated] = players[amount_of_players]
        players[amount_of_players] = aux_player
        amount_of_players -= 1
    return players


def match_maker(shuffled_players):
    # Object that will represents the bracket
    bracket = []
    # Represents the round matches
    matches = []
    # Number of matches in the first round
    byes = 0
    count = 0
    print "shuffled players:"
    print shuffled_players
    byed_players = []

    if is_power_of_two(len(shuffled_players)):
        while count != len(shuffled_players) / 2:
            matches.append([shuffled_players[count], shuffled_players[(len(shuffled_players) - 1) - count]])
            count += 1
        bracket.append(matches)
    else:
        byes = get_byes(len(shuffled_players))
        random_used = []
        count = 0
        while count < byes:
            while True:
                rand_num = random.randint(0, len(shuffled_players)-1)
                if not rand_num in random_used:
                    random_used.append(rand_num)
                    break
            byed_players.append(shuffled_players[random_used[count]])
            shuffled_players.remove(byed_players[count])
            count += 1
        count = 0
        while count != len(shuffled_players) / 2:
            matches.append([shuffled_players[count], shuffled_players[(len(shuffled_players) - 1) - count]])
            count += 1
        bracket.append(matches)
        print "Byed Players:"
        print byed_players
        print "shufled players after bye process:"
        print shuffled_players
    bracket = generate_next_rounds(len(shuffled_players), bracket, byed_players)
    bracket.append([None])
    print "bracket:"
    print bracket
    return bracket

def generate_next_rounds(number_of_players, bracket, byed_players):
    count = 0
    matches = []
    if len(byed_players) == 0:
        rounds = get_exponent_base_two(number_of_players)
        matches_next_round = number_of_players/4
        while rounds > 1:
            while matches_next_round > count:
                matches.append([None]*2)
                count += 1
            matches_next_round /= 2
            bracket.append(matches)
            matches = []
            rounds -= 1
            count = 0
    else:
        #TODO work on generate next rounds for byes
        rounds = get_exponent_base_two((number_of_players / 2)+len(byed_players))
        matches_next_round = ((number_of_players / 2)+len(byed_players))/2
        while rounds > 0:
            while matches_next_round > count:
                if not is_power_of_two(len(byed_players)) and len(byed_players) != 0:
                    matches.append([byed_players[count],None])
                    byed_players.remove(byed_players[count])
                    count += 1
                    continue
                elif len(byed_players) > 0:
                    count2 = 0
                    while not len(byed_players) / 2 == 0:
                        matches.append([byed_players[count2], byed_players[(len(byed_players) - 1) - count2]])
                        byed_players.remove(byed_players[count2])
                        byed_players.remove(byed_players[(len(byed_players) - 1) - count2])
                        count2 += 1
                    count += 1
                    continue
                else:
                    matches.append([None]*2)
                    count += 1
                    continue
            matches_next_round /= 2
            bracket.append(matches)
            matches = []
            rounds -= 1
            count = 0
    return bracket

def is_power_of_two(number):
    if number == 0:
        return False
    else:
        return (number & (number - 1) == 0) and (number != 0)

def get_byes(number_of_players):
    next_higher_power_of_two = 0
    count = 1
    number_of_byes = 0
    while next_higher_power_of_two < number_of_players:
        next_higher_power_of_two = int(math.pow(2,count))
        count += 1
    number_of_byes = next_higher_power_of_two - number_of_players
    return number_of_byes

def get_exponent_base_two(number):
    exponent = 0
    while number > 1:
        number /= 2
        exponent += 1
    return exponent

#single_elimination_bracket_generation(["alonso", "darian", "michael", "lunita", "5", "6", "7", "8", "alonso2", "darian2", "michael2", "lunita2", "5_2", "6_2", "7_2", "8_2"])
single_elimination_bracket_generation(["alonso", "darian", "michael", "jack", "aaron cook"])
#single_elimination_bracket_generation(["alonso", "darian", "michael", "aaron cook"])



