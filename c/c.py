# -*- encoding:utf-8 -*-
from math import floor
'''

'''


def filer(fname):
    with file(fname, 'r') as f:
        contents = f.read().strip().split('\n')
        count, contents = int(contents[0]), contents[1:]
    return count, contents


def play_game(count, contents):
    all_user_scores = []
    for i in xrange(count):
        user, cards = contents[i * 2], contents[i * 2 + 1]
        print user, cards
        user = int(user)
        order = 0
        length = len(cards)
        user_scores = [0] * user
        j = 0
        for i in xrange(length):
            if j > 0:
                j -= 1
                continue
            card = cards[i]
            if card.isdigit():
                user_scores[order] += int(card)
            elif card == 'X':
                while not card.isdigit():
                    j += 1
                    try:
                        card = cards[i + j]
                    except:
                        card = '1'
                else:
                    user_scores[order] *= int(card)
            elif card == 'D':
                while not card.isdigit():
                    j += 1
                    try:
                        card = cards[i + j]
                    except:
                        card = '1'
                else:
                    user_scores[order] = \
                        user_scores[order] / float(card)
                    if user_scores[order] >= 0:
                        user_scores[order] = int(floor(user_scores[order]))
                    else:
                        user_scores[order] = int(floor(user_scores[order])) + 1
            elif card == 'S':
                while not card.isdigit():
                    j += 1
                    try:
                        card = cards[i + j]
                    except:
                        card = '0'
                else:
                    user_scores[order] -= int(card)
            order = order + 1 if order + 1 < user else 0
        all_user_scores.append(max(user_scores))
    return all_user_scores


def main():
    fname = 'input.txt'
    count, contents = filer(fname)
    results = play_game(count, contents)
    text = ''
    for result in results:
        text += str(result) + '\n'
    with file('output.txt', 'w') as f:
        f.write(text)

if __name__ == '__main__':
    main()
