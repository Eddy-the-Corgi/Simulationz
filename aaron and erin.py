'''
It’s been a while and change, but the Robot Games are back once again. This time it’s Capture the Flag!

Two robots, Aaron and Erin, have made it to this year’s final! Initially they are situated at the center of a unit circle. A flag is placed somewhere inside the circle, at a location chosen uniformly at random. Once the flag is placed, Aaron is able to deduce its distance to the flag, and Erin is only able to deduce its direction to the flag. (Equivalently: if (r, θ) are the polar coordinates of the flag’s location, Aaron is told r and Erin is told θ.)

Both robots are allowed to make a single move after the flag is placed, if they wish. Any move they make is without knowledge of what the other robot is doing. (And they may not move outside the circle.)

Whichever robot is closer to the flag after these moves captures the flag and is declared the winner!

During the preliminaries it was discovered that Erin is programmed to play a fixed distance along the detected angle θ. Assuming otherwise optimal play by both robots, can you determine the probability that Aaron will win? (Please express your answer to 10 decimal places.)
'''
import random
import math

def play_game(erin_fixed, aaron_score, erin_score):
    actual_r = math.sqrt(random.random())
    erin_dist_squared = ( actual_r - erin_fixed ) ** 2
    if actual_r < erin_fixed / 2:
        aaron_score += 1
    else:
        aaron_angle = 2 * math.pi * random.random()
        aaron_picked_radius = math.sqrt((actual_r ** 2) - (erin_fixed - actual_r) ** 2)
        aaron_dist_squared = (aaron_picked_radius ** 2) + (actual_r ** 2) - 2 * actual_r * aaron_picked_radius * math.cos(aaron_angle)
        if aaron_dist_squared > erin_dist_squared:
            aaron_score += 1
        else:
            erin_score += 1
    print(erin_fixed, aaron_score, erin_score)
    return (aaron_score, erin_score)

def play_N_times(N, erin_fixed, aaron_score, erin_score):
    for _ in range(N):
        aaron_score, erin_score = play_game(erin_fixed, aaron_score, erin_score)
    print(aaron_score / (aaron_score + erin_score))

play_N_times(10000, 0.00001, 0, 0)