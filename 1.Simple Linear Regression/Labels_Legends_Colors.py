# We'll use Matplotlib module to draw a series of lines in this lesson
import matplotlib.pyplot as plt
# Coordinates of  Line 1
x1 = ([2.3, 3, 7.8, 8])
y1 = ([0.2, 1.8, 5, 10])

# Coordinates of Line 2
x2 = ([0, 4, 6, 7, 9, 10])
y2 = ([0, 4, 5, 4, 7, 12])

x3 = ([0, 4, 6, 8, 9, 15])
y3 = ([0, 4, 6, 8, 9, 15])

# Plotting, line style, line color and legend
plt.plot(x1, y1, linestyle='--', c='g', label='Line 1')
plt.plot(x2, y2, linestyle='-', c='r', label='Line 2')
plt.plot(x3, y3, linestyle='-', c='y', label='Line 3')

plt.legend()

# Set Legend title
plt.title('My First Multi_line')

# Set Labels
plt.xlabel('X-Values')
plt.ylabel('Y-Values')
# print('Please Wait as python is doing the plotting...')
plt.show()
