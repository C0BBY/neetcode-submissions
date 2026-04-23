class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        upgrade = []
        fleet_count = len(position)

        for i in range(len(position)):
            upgrade.append((position[i], speed[i]))
        upgrade.sort()

        for i in range(len(upgrade)):
            pos = upgrade[i][0]
            spd = upgrade[i][-1]
            tim_taken = (target - pos) / spd
            for j in range(i + 1, len(upgrade)):
                pos_2 = upgrade[j][0]
                spd_2 = upgrade[j][-1]
                tim_taken_2 = (target - pos_2) / spd_2

                if tim_taken <= tim_taken_2:
                    fleet_count -= 1
                    break
        return fleet_count