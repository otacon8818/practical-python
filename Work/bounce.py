# bounce.py
#
# Exercise 1.5
height = 100  # 100 meters
# bounce = 0
bounce = 1
# times = 1  # initial time
# * not need variable : times
while bounce <= 10:
    height = height * (3 / 5)  # * height is dynamical change
    print(bounce, round(height, 4))
    bounce += 1
    # height = bounce