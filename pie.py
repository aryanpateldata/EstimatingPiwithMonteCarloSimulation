import random
import matplotlib.pyplot as plt
circle_points = 0
dots = 1500
fig, ax = plt.subplots(figsize=(5,5))
ax.set_aspect('equal')

# Create two lists, one for x coordinates and one for y coordinates

# Create a circle centered at (0.5, 0.5) with radius 0.5
my_circle = plt.Circle((0.5,0.5), radius=0.5, fill=False)


ax.add_patch(my_circle)

xcoords = [random.random() for _ in range(dots)]
ycoords = [random.random() for _ in range(dots)]
ax.scatter(xcoords, ycoords)
# Using the pythagorean theorem to determine whether the point is inside circle or not. 
def inside_circle(x, y, cx, cy, radius):
    return True if ((x-cx)**2) + ((y-cy)**2) <= radius**2 else False

#iterate through x,y coordinate list
for i in range(dots):
    if inside_circle(xcoords[i], ycoords[i], 0.5, 0.5, 0.5):
        circle_points += 1


pi = (circle_points/dots)*4

print(f"Estimation of Pi is = ",pi)
print("Total Dots = 1500")
print(f"Dots in Circle = ",circle_points)
plt.show()