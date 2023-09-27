import keyboard

class GyroSim:
    def __init__(self, desired_heading, initial_heading, heading_increment=0.1):
        self.desired_heading=desired_heading
        self.heading=initial_heading
        self.heading_increment=heading_increment
    
    def update(self):
        if keyboard.is_pressed("left"):
            self.heading+=self.heading_increment
        elif keyboard.is_pressed('right'):
            self.heading-=self.heading_increment
    
    def get_heading(self):
        return self.heading
    
    def get_desired_heading(self):
        return self.desired_heading
    
    def get_delta_heading(self):
        delta_heading = self.desired_heading - self.heading
        delta_heading = (delta_heading + 180) % 360 - 180  # Wrap within -180 to 180 range

        return delta_heading
