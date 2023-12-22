from rover_control import mars_rover


class rover_test:
    def __init__(self):
        self.rover = mars_rover()

    def test_rover_position(self, position_x, position_y):
        rover_x, rover_y = self.rover.get_position()
        return rover_x == position_x and rover_y == position_y

    def test_camera_direction(self, direction):
        camera_direction = self.rover.get_camera_direction()
        return camera_direction == direction


test = rover_test()

if test.test_rover_position(0, 0):
    print('Начальная позиция верна')
else:
    print('Начальная позиция НЕ верна')

if test.test_camera_direction('forward'):
    print('Начальное положение камеры верно')
else:
    print('Начальное положение камеры НЕ верно')

test.rover.move_forward()
test.rover.move_left()
test.rover.move_forward()
test.rover.move_right()
test.rover.move_back()
test.rover.move_back()
test.rover.move_left()
print()
if test.test_rover_position(-3, 0):
    print('Конечная позиция верна')
else:
    print('Конечная позиция НЕ верна')

if test.test_camera_direction('left'):
    print('Конечное положение камеры верно')
else:
    print('Конечное положение камеры НЕ верно')
