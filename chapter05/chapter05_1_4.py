class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def div(self):
        result =  self.first / self.second
        return result

    def min(self):
        result = self.first - self.second
        return result


class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
    
class safeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else: return self.first / self.second

a = safeFourCal(4,0)
print(a.add())
print(a.mul())
print(a.div())
print(a.min())

