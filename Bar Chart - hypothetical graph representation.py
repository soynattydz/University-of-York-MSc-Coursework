import matplotlib.pyplot as plt
import numpy as np

# Defining the data points for the graph
categories = ['STEM Before AI', 'STEM After AI', 'Non-STEM Before AI', 'Non-STEM After AI']
performance = [70, 85, 65, 75]  # Hypothetical performance scores
engagement = [60, 80, 55, 70]   # Hypothetical engagement scores

x = np.arange(len(categories))  # Label locations
width = 0.35  # Width of the bars

# Creating the plot
fig, ax = plt.subplots()

bar1 = ax.bar(x - width/2, performance, width, label='Performance')
bar2 = ax.bar(x + width/2, engagement, width, label='Engagement')

# Adding labels and titles
ax.set_xlabel('Course Type and AI Implementation')
ax.set_ylabel('Scores')
ax.set_title('Hypothetical Impact of AI on Student Performance and Engagement')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()

# Adding data labels
for bar in bar1:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), va='bottom')  # Adding text label above the bars

for bar in bar2:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), va='bottom')  # Adding text label above the bars

# Display the plot
plt.show()
