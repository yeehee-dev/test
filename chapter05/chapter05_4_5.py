class Bird:
    def fly(self):
        raise NotImplementedError
class eagle(Bird):
    def fly(self):
        print("very fast")

Eagle = eagle()
Eagle.fly()