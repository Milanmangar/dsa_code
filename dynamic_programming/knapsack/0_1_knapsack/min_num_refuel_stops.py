# http://leetcode.com/problems/minimum-number-of-refueling-stops/description/


import heapq


class Solution:
    # def minRefuelStops(
    #     self, target: int, startFuel: int, stations: list[list[int]]
    # ) -> int:
    #     if startFuel >= target:
    #         return 0

    #     heap = []
    #     stations.append([target, float("inf")])
    #     refuels = 0
    #     prev = 0
    #     for location, capacity in stations:
    #         startFuel = startFuel - (location - prev)
    #         while heap and startFuel < 0:
    #             startFuel = startFuel + -heapq.heappop(heap)
    #             refuels += 1
    #         if startFuel < 0:
    #             return -1
    #         heapq.heappush(heap, -capacity)
    #         prev = location
    #     return refuels

    def minRefuelStops(
        self, target: int, startFuel: int, stations: list[list[int]]
    ) -> int:
        """
        Time: O(n log n)
            because at most n elements go into the heap, and each heap operation (push/pop) is O(log n)
        Space: O(n)
            The heap stores at most n fuel capacities
        """
        if startFuel >= target:
            return 0

        heap = []
        stations.append([target, 0])
        current_fuel = startFuel
        number_of_stations_used = 0
        for next_station_distance, next_fuel_capacity in stations:
            while current_fuel < next_station_distance:
                if len(heap) == 0:
                    return -1
                current_fuel = current_fuel + -heapq.heappop(heap)
                number_of_stations_used += 1
            heapq.heappush(heap, -next_fuel_capacity)

        # while current_fuel < target:
        #     if len(heap) == 0:
        #         return -1
        #     current_fuel = current_fuel + -heapq.heappop(heap)
        #     number_of_stations_used += 1
        return number_of_stations_used


s = Solution()

print(s.minRefuelStops(100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]]))  # 2
# print(s.minRefuelStops(100, 25, [[25, 25], [50, 25], [75, 25]]))  # 3
# print(s.minRefuelStops(100, 50, [[50, 50]]))  # 1
# print(s.minRefuelStops(1, 1, []))  # 0
# print(s.minRefuelStops(100, 1, [[10, 100]])) # -1
