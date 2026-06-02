"""
Design an elevator controller
"""

from enum import Enum
from typing import Set
from collections import defaultdict

class Direction(Enum):
    UP = 1
    DOWN = 2
    NONE = 3

class RequestType(Enum):
    PICKUP = 1
    DROPOFF = 2

class Request():
    def __init__(self, floor, direction: Direction, type: RequestType):
        self.floor = floor
        self.direction = direction
        self.type = type

    def __repr__(self):
        return f"floor: {self.floor} - direction: {self.direction} - type: {self.type}\n"

class ElevatorController():
    def __init__(self, elevatorCount: int, maxFloor: int):
        self.elevators = [Elevator(1, Direction.NONE) for _ in range(elevatorCount)]
        self.maxFloor = maxFloor

    def __repr__(self):
        res = ""
        for i, elevator in enumerate(self.elevators):
            res += f"Elevator {i}: {elevator}\n"
        return res

    def step(self):
        """
        Move each elavator one unit of time (either top, down, or stopped - allowing pickup and dropoff)
        """
        for i, elevator in enumerate(self.elevators):
            if len(elevator.floorRequests) > 0:
                # All requests for that floor were resolved
                self.elevators[i].requestCount -= len(elevator.floorRequests)
                self.elevators[i].floorRequests[elevator.floor] = set()
                continue

            if elevator.direction == Direction.UP:
                if elevator.floor < self.maxFloor:
                    self.elevators[i].floor += 1
                else:
                    self.direction = Direction.NONE

            if elevator.direction == Direction.DOWN:
                if elevator.floor > 1:
                    self.elevators[i].floor -= 1
                else:
                    self.direction = Direction.NONE

        
    
    def acceptRequest(self, request: Request) -> int:
        """
        Request assignment criteria
        1. Closest elevator in the same direction
        2. Idle elevator
        3. Elevator with fewer requests 
        """
        if request.floor < 1 or request.floor > self.maxFloor:
            raise ValueError(f"floor request must be between 1 and {self.maxFloor}")

        minDist, elevatorIdx = float("inf"), -1
        for i, elevator in enumerate(self.elevators):
            dist = abs(elevator.floor - request.floor)
            if elevator.direction != request.direction or dist >= minDist:
                continue

            if elevator.direction == Direction.UP and elevator.floor <= request.floor or elevator.direction == Direction.DOWN and elevator.floor >= request.floor:
                minDist, elevatorIdx = dist, i
        
        if elevatorIdx != -1:
            self.assignElevator(request, elevatorIdx)
            return elevatorIdx

        minReqs = float("inf")
        for i, elevator in enumerate(self.elevators):
            if elevator.direction == Direction.NONE:
                self.assignElevator(request, i)
                return i

            if elevator.requestCount > minReqs:
                elevatorIdx = i
                minReqs = elevator.requestCount

        self.assignElevator(request, elevatorIdx)
        return elevatorIdx        
    
    def assignElevator(self, request: Request, index: int):
        self.elevators[index].floorRequests[request.floor].add(request)
        self.elevators[index].requestCount += 1

        if self.elevators[index].direction == Direction.NONE:
            self.elevators[index].direction = request.direction


class Elevator():
    def __init__(self, floor, direction: Direction):
        self.floor = floor
        self.direction = direction
        self.floorRequests = defaultdict(set) # keep track of requests for each floor in this elevator
        self.requestCount = 0

    def __repr__(self):
        return f"floor: {self.floor} - direction: {self.direction}\nrequests: {self.floorRequests}\n"


e = ElevatorController(5, 10)
e.acceptRequest(Request(1, Direction.UP, RequestType.PICKUP))
print(f"{'='*20}\n{e}")
e.step()
print(f"{'='*20}\n{e}")
e.acceptRequest(Request(5, Direction.DOWN, RequestType.PICKUP))
e.step()
print(f"{'='*20}\n{e}")
e.acceptRequest(Request(8, Direction.UP, RequestType.DROPOFF))
e.step()
print(f"{'='*20}\n{e}")
    