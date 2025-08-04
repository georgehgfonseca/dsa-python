class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if len(triplets) == 1 and triplets[0] == target:
            return True

        # compute triplets that form the target[pos]
        candTriplets = set([i for i in range(len(triplets))])
        for pos in range(len(target)):
            toRemove = set()
            for idx in candTriplets:
                if triplets[idx][pos] > target[pos]:
                    toRemove.add(idx)
                
            for idx in toRemove:
                candTriplets.remove(idx)
        
        for pos in range(len(target)):
            foundPos = False
            for idx in candTriplets:
                if triplets[idx][pos] == target[pos]:
                    foundPos = True
            if not foundPos:
                return False
        return True
            
    def mergeTriplets2(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i, v in enumerate(t):
                if v == target[i]:
                    good.add(i)
        return len(good) == 3
        
    def mergeTriplets3(self, triplets: List[List[int]], target: List[int]) -> bool:
        if len(triplets) == 1 and triplets[0] == target:
            return True

        # compute pairs that form the target[pos]
        candTriplets = set([i for i in range(len(triplets))])
        tripletsWithTargetPos = set()
        for pos in range(len(target)):
            if pos != 0 and len(tripletsWithTargetPos) == 0:
                return False
            tripletsWithTargetPos = set()
            toRemove = set()
            for idx in candTriplets:
                if triplets[idx][pos] > target[pos]:
                    toRemove.add(idx)
                elif triplets[idx][pos] == target[pos]:
                    tripletsWithTargetPos.add(idx)
            for idx in toRemove:
                candTriplets.remove(idx)

            #print(candTriplets, tripletsWithTargetPos)

        if len(candTriplets) >= 2 and len(tripletsWithTargetPos) >= 1:
            return True
        return False