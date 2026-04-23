class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []
        for i,_ in enumerate(position):
            spd = speed[i]
            dst = target - position[i]
            time.append((position[i], dst/spd))
        
        time.sort(reverse=True)
        fleets = 0
        to_beat = 0
        
        for pos, rem in time:
            if not to_beat:
                to_beat = rem
                fleets+=1
            else:
                if rem > to_beat:
                    fleets+=1
                    to_beat = rem

        return fleets           