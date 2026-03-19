class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        self.current_floor += 1

    def floor_down(self):
        self.current_floor -= 1

    def go_to_floor(self, floor):
        while self.current_floor != floor:
            if self.current_floor < floor:
                self.floor_up()
            elif self.current_floor > floor:
                self.floor_down()

class Building:
    def __init__(self, bottom_floor, top_floor, elevatorsCount):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevatorsCount = elevatorsCount
        self.elevators = []
        while len(self.elevators) < self.elevatorsCount:
            self.elevators.append(Elevator(self.bottom_floor, self.top_floor))

    def run_elevator(self, elevatorIndex, target_floor):
        self.elevators[elevatorIndex].go_to_floor(target_floor)

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom_floor)