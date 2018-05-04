from math import sqrt
import matplotlib.pyplot as plt

plot1 = [1,3]
plot2 = [2,5]

euclid_distance = sqrt((plot1[0] - plot2[0])**2 + (plot1[1] - plot2[1])**2)

print(euclid_distance)

plt.plot(plot1)
plt.plot(plot2)
plt.plot([0, euclid_distance])

plt.show()