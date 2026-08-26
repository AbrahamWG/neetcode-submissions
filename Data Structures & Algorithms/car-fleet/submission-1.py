class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = 1
        # sorted by position from closest to target
        cars = sorted(zip(position, speed))
        top = (target - cars[-1][0]) / float(cars[-1][1])
        cars.pop()
        while cars:
            curr = (target - cars[-1][0]) / float(cars[-1][1])
            # if curr takes more time to reach target, its a different fleet
            if curr > top:
                top = curr
                fleet += 1
            else:
                cars.pop()
        
        return fleet