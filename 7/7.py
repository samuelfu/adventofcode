from collections import Counter, defaultdict

ll = [x for x in open('input.txt').read().strip().split('\n')]
grid = [[c for c in s] for s in ll]

order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def categorize(c):
    l = len(c.keys())
    # print(l, c.keys(), c.values())
    if l == 1:
        return 0
    elif l == 2 and 4 in c.values():
        return 1
    elif l == 2 and 3 in c.values() and 2 in c.values():
        return 2
    elif l == 3 and 3 in c.values():
        return 3
    elif l == 3 and 2 in c.values() and 1 in c.values():
        return 4
    elif l == 4 and 2 in c.values() and 1 in c.values():
        return 5
    else:
        return 6

def compare_hands(hand):
    return tuple(order.index(card) for card in hand)


hands = []
bids = []
hand_bid = {}
types = []
total_cards = len(ll)
m = defaultdict(list)
for l in ll:
    s = l.split()
    hands.append(s[0])
    bids.append(s[1])
    hand_bid[s[0]] = s[1]

for i in range(len(hands)):
    c = Counter(hands[i])
    most_frequent = sorted(c, key=c.get, reverse=True)
    if most_frequent[0] == 'J' and len(most_frequent) >= 2:
            c = Counter(hands[i].replace('J', most_frequent[1]))
    else:
        c = Counter(hands[i].replace('J', most_frequent[0]))
    type = categorize(c)
    types.append(type)

for i in range(len(types)):
    m[types[i]].append((hands[i], bids[i]))

final_ranks = []
for key in sorted(m.keys()):
    cards = [x[0] for x in m[key]]
    b = [x[1] for x in m[key]]
    sorted_cards = sorted(cards, key=compare_hands)
    final_ranks.extend(sorted_cards)

print(hands)
print(bids)
print(final_ranks)
print([int(hand_bid[r]) for r in final_ranks])
print(sum(int(hand_bid[final_ranks[i]]) * (total_cards - i) for i in range(len(final_ranks))))