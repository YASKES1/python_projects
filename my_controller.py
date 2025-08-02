from controller import Robot
import random  

TIMESTEP = 64
MAX_SPEED = 5
FRONT_OBSTACLE_THRESHOLD = 25
SIDE_OBSTACLE_THRESHOLD = 45
SIDE_AS_FRONT_THRESHOLD = 35

WALL_FOLLOW_KP = 0.5
STUCK_TURN_FACTOR = 1.5  
STUCK_TURN_PROBABILITY = 0.7 
def run_robot(robot):
    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')

    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))

    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)

    ps = []
    ps_names = ['ps0', 'ps1', 'ps2', 'ps5', 'ps6', 'ps7']
    for name in ps_names:
        sensor = robot.getDevice(name)
        sensor.enable(TIMESTEP)
        ps.append(sensor)

    stuck_counter = 0  

    while robot.step(TIMESTEP) != -1:
        ps_values = [sensor.getValue() for sensor in ps]

        ps0_val = ps_values[0]
        ps1_val = ps_values[1]
        ps2_val = ps_values[2]
        ps5_val = ps_values[3]
        ps6_val = ps_values[4]
        ps7_val = ps_values[5]

        front_obstacle = (ps0_val > FRONT_OBSTACLE_THRESHOLD or
                            ps7_val > FRONT_OBSTACLE_THRESHOLD or
                            ps1_val > SIDE_AS_FRONT_THRESHOLD or
                            ps6_val > SIDE_AS_FRONT_THRESHOLD)

        right_wall_too_close = ps1_val > SIDE_OBSTACLE_THRESHOLD or ps2_val > SIDE_OBSTACLE_THRESHOLD
        left_wall_too_close = ps5_val > SIDE_OBSTACLE_THRESHOLD or ps6_val > SIDE_OBSTACLE_THRESHOLD

        right_side_value = max(ps1_val, ps2_val)
        left_side_value = max(ps5_val, ps6_val)

        left_speed = MAX_SPEED
        right_speed = MAX_SPEED

        if front_obstacle:
            stuck_counter += 1
            if stuck_counter > 10:  
                if random.random() < STUCK_TURN_PROBABILITY:
                    turn_factor = STUCK_TURN_FACTOR
                    if random.random() < 0.5:
                        left_speed = -turn_factor * MAX_SPEED
                        right_speed = turn_factor * MAX_SPEED
                    else:
                        left_speed = turn_factor * MAX_SPEED
                        right_speed = -turn_factor * MAX_SPEED
                else:
                    left_speed = -0.8 * MAX_SPEED
                    right_speed = 0.8 * MAX_SPEED
            else:
                left_speed = -0.8 * MAX_SPEED
                right_speed = 0.8 * MAX_SPEED
        else:
            stuck_counter = 0  
            if right_wall_too_close:
                left_speed = 0.7 * MAX_SPEED
                right_speed = MAX_SPEED
            elif left_wall_too_close:
                left_speed = MAX_SPEED
                right_speed = 0.7 * MAX_SPEED
            elif right_side_value > 40:
                error = right_side_value - SIDE_WALL_THRESHOLD
                adjustment = WALL_FOLLOW_KP * error
                adjustment = max(-MAX_SPEED * 0.5, min(MAX_SPEED * 0.5, adjustment))
                left_speed = MAX_SPEED - adjustment
                right_speed = MAX_SPEED + adjustment
            elif left_side_value > 40:
                error = left_side_value - SIDE_WALL_THRESHOLD
                adjustment = WALL_FOLLOW_KP * error
                adjustment = max(-MAX_SPEED * 0.5, min(MAX_SPEED * 0.5, adjustment))
                left_speed = MAX_SPEED + adjustment
                right_speed = MAX_SPEED - adjustment
            else:
                left_speed = MAX_SPEED
                right_speed = MAX_SPEED

        left_speed = max(-MAX_SPEED, min(MAX_SPEED, left_speed))
        right_speed = max(-MAX_SPEED, min(MAX_SPEED, right_speed))

        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)

if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)