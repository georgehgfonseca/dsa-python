class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # sort the trips by from field
        # monitor the numPassengers throught the drive
        trips.sort(key=lambda x: x[1])
        milePassChange = dict()
        for trip in trips:
            milePassChange[trip[1]] = milePassChange.get(trip[1], 0) + trip[0]
            milePassChange[trip[2]] = milePassChange.get(trip[2], 0) - trip[0]

        
        # sorted_dict = dict(sorted(milePassChange.items()))
        currPassengers = 0
        for mile in sorted(milePassChange):
            currPassengers += milePassChange[mile]
            if currPassengers > capacity:
                return False
        return True

