class mars_rover:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 'forward'

    def move_forward(self):
        if self.direction == 'forward':
            self.y += 1
        elif self.direction == 'left':
            self.x -= 1
        elif self.direction == 'right':
            self.x += 1
        elif self.direction == 'back':
            self.y -= 1

    def move_left(self):
        if self.direction == 'forward':
            self.direction = 'left'
            self.x -= 1
        elif self.direction == 'left':
            self.direction = 'back'
            self.y -= 1
        elif self.direction == 'back':
            self.direction = 'right'
            self.x += 1
        elif self.direction == 'right':
            self.direction = 'forward'
            self.y += 1

    def move_right(self):
        if self.direction == 'forward':
            self.direction = 'right'
            self.x += 1
        elif self.direction == 'right':
            self.direction = 'back'
            self.y -= 1
        elif self.direction == 'back':
            self.direction = 'left'
            self.x -= 1
        elif self.direction == 'left':
            self.direction = 'forward'
            self.y += 1

    def move_back(self):
        if self.direction == 'forward':
            self.y -= 1
        elif self.direction == 'left':
            self.x += 1
        elif self.direction == 'back':
            self.y += 1
        elif self.direction == 'right':
            self.x -= 1

    def get_position(self):
        print(f'Координаты: x={self.x}, y={self.y}')
        return self.x, self.y

    def get_camera_direction(self):
        print(f'Направление камеры: {self.direction}')
        return self.direction


rover = mars_rover()


def start():
    move = input()
    if move == 'f':
        rover.move_forward()
        rover.get_position()
        rover.get_camera_direction()
        return start()
    elif move == 'l':
        rover.move_left()
        rover.get_position()
        rover.get_camera_direction()
        return start()
    elif move == 'b':
        rover.move_back()
        rover.get_position()
        rover.get_camera_direction()
        return start()
    elif move == 'r':
        rover.move_right()
        rover.get_position()
        rover.get_camera_direction()
        return start()
    elif move == 'exit':
        return rover.get_position(), rover.get_camera_direction()
    else:
        print('Ошибка ввода.')
        return start()
