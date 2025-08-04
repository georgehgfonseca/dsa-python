from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = Counter(hand)
        hand.sort()
        for num in hand:
            if count[num]:
                for i in range(num, num + groupSize):
                    if not count[i]:
                        return False
                    count[i] -= 1
        return True
        
    def isNStraightHand2(self, hand: List[int], groupSize: int) -> bool:
        numGroups = int(len(hand) / groupSize)
        if len(hand) % groupSize != 0:
            return False

        # hash map of num and count
        cardCount = dict()
        for card in hand:
            cardCount[card] = cardCount.get(card, 0) + 1
        
        for _ in range(numGroups):
            curr = min(cardCount)
            countCards = 0
            while curr in cardCount and countCards < groupSize:
                cardCount[curr] -= 1
                if cardCount[curr] == 0:
                    cardCount.pop(curr)
                curr += 1
                countCards += 1
            if countCards != groupSize:
                return False
        return True



