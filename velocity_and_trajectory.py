import math
import matplotlib.pyplot as plt
import itertools

try:
    ball_list = []
    loop = input("How many trajectories?")
    for i in range(int(loop)):
        ball_list.append("Ball {}".format(i + 1))
        init_velocity = input("Enter the initial velocity for trajectory {} (m/s) >> ".format(i + 1))
        angle = input("Enter the angle of projection for trajectory {} (degrees) >> ".format(i + 1))

        velocity_x = float(init_velocity) * math.cos(math.radians(float(angle)))
        velocity_y = float(init_velocity) * math.sin(math.radians(float(angle)))

        time = int((2 * velocity_y) / 10)
        s_size = list()
        s_height = list()

        for i in itertools.count():
            sx = velocity_x * (i / 1000)
            sy = velocity_y * (i / 1000) - 0.5 * 10 * (i / 1000) ** 2
            if sy >= 0:
                s_size.append(sx)
                s_height.append(sy)
            else:
                break

        plt.scatter(s_size, s_height, s=50)

    """Label"""
    plt.title("Projectile motion of a ball")
    plt.xlabel("Distance")
    plt.ylabel("Height")
    plt.legend(ball_list)
    plt.show()
except:
    print("[ERROR] alphabet inputted")
