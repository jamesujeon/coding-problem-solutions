# 문제 링크: https://leetcode.com/problems/design-parking-system/

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.max_slots = [big, medium, small]
        self.slots = [0] * 3 

    def addCar(self, carType: int) -> bool:
        i = carType - 1
        if self.slots[i] == self.max_slots[i]:
            return False

        self.slots[i] += 1
        return True


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)