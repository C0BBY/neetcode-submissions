class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        fleets = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort(reverse=True)

        print(cars)
        for car in cars:
            pos,spd = car
            time = (target-pos)/spd
            if fleets:
                pos_2,spd_2 = fleets[-1]
                time_2 = (target-pos_2)/spd_2
                if time <= time_2:
                    continue
            fleets.append(car)
        return len(fleets)            

             