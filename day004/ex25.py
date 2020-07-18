"""
**The Minion Game

Both players are given the same string, ```S```. Both players have to make substrings using the letters of this string.
Stuart has to make words starting with consonants. Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.
"""
import re

def minion_game(string):
    player1 = dict()
    player2 = dict()

    for i in range(len(string)):
        pattern1 = "(?=([^AEIOU]+\w{{{0}}}))".format(i)
        for match in re.finditer(pattern1, string):
            sub = match.group(1)
            if player1.get(sub) == None:
                player1[sub] = 1
            else:
                player1[sub] += 1
        
        pattern2 = "(?=([AEIOU]+\w{{{0}}}))".format(i)
        for match in re.finditer(pattern2, string):
            sub = match.group(1)
            if player2.get(sub) == None:
                player2[sub] = 1
            else:
                player2[sub] += 1
    
    res1 = sum(player1.values())
    res2 = sum(player2.values())
    
    if res1 > res2:
        print("Stuart {}".format(res1))
    elif res1 < res2:
        print("Kevin {}".format(res2))
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)

"""
This was my attempt.
Unfortunately this did not work well for all input test cases due to time constraints.
Looking into discussions, there's an elegant and faster solution to this problem statement.
"""
def minion_game_v2(string):
    vowels = "AEIOU"
    stuart_score = 0
    kevin_score = 0
    length = len(string)

    for i in range(length):
        if string[i] in vowels:
            kevin_score += length - i
        else:
            stuart_score += length - i
    
    if stuart_score > kevin_score:
        print("Stuart {}".format(stuart_score))
    elif stuart_score < kevin_score:
        print("Kevin {}".format(kevin_score))
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game_v2(s)