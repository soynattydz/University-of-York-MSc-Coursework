import matplotlib.pyplot as plt
from matplotlib.sankey import Sankey

# Function to add text boxes with arrows
def add_box(ax, text, xy, width=0.2, height=0.1, fontsize=10, color='lightblue'):
    box = plt.Rectangle(xy, width, height, edgecolor='black', facecolor=color)
    ax.add_patch(box)
    ax.text(xy[0] + width/2, xy[1] + height/2, text, horizontalalignment='center', 
            verticalalignment='center', fontsize=fontsize, weight='bold')
    
def add_arrow(ax, xy_from, xy_to, color='black'):
    ax.annotate('', xy=xy_to, xytext=xy_from,
                arrowprops=dict(facecolor=color, shrink=0.05, width=1.5, headwidth=10))

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 8))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Add boxes for each step
add_box(ax, '1. Research Questions and Hypotheses Formulation', (0.4, 0.85), width=0.4, height=0.1)
add_box(ax, '2. Literature Review', (0.4, 0.7), width=0.4, height=0.1)
add_box(ax, '3. Research Design Selection', (0.4, 0.55), width=0.4, height=0.1)
add_box(ax, '4. Data Collection', (0.4, 0.4), width=0.4, height=0.1)
add_box(ax, '5. Data Analysis', (0.4, 0.25), width=0.4, height=0.1)
add_box(ax, '6. Results Interpretation', (0.4, 0.1), width=0.4, height=0.1)
add_box(ax, '7. Conclusions and Recommendations', (0.4, -0.05), width=0.4, height=0.1)
add_box(ax, '8. Reporting and Dissemination', (0.4, -0.2), width=0.4, height=0.1)

# Add arrows
add_arrow(ax, (0.6, 0.85), (0.6, 0.8))
add_arrow(ax, (0.6, 0.7), (0.6, 0.65))
add_arrow(ax, (0.6, 0.55), (0.6, 0.5))
add_arrow(ax, (0.6, 0.4), (0.6, 0.35))
add_arrow(ax, (0.6, 0.25), (0.6, 0.2))
add_arrow(ax, (0.6, 0.1), (0.6, 0.05))
add_arrow(ax, (0.6, -0.05), (0.6, -0.1))

# Remove axes
ax.axis('off')

# Show the diagram
plt.show()
