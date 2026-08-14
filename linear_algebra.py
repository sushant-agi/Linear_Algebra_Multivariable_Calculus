import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# --- 1. Define the Target Transformation Matrix (Example: Rotation and Shear) ---
# A rotation by 45 degrees
theta = np.pi / 4
R = np.array([
    [1, 2], [2, 2]
])
# A shear
S = np.array([
    [1, 0.5],
    [0, 1]
])
# Combine them (Rotation then Shear)
A_target = S @ R

# Identity Matrix
I = np.array([[1, 0], [0, 1]])

# --- 2. Grid Generation (same as before) ---
c_range = np.linspace(-4, 4, 10)
num_points = 20
original_lines = []

for c in c_range:
    x_v = np.full(num_points, c)
    y_v = np.linspace(c_range.min(), c_range.max(), num_points)
    original_lines.append(np.vstack([x_v, y_v]))

    x_h = np.linspace(c_range.min(), c_range.max(), num_points)
    y_h = np.full(num_points, c)
    original_lines.append(np.vstack([x_h, y_h]))
# --- 3. Animation Setup ---
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_title('Animated Linear Transformation')
ax.set_xlabel('x-axis')
ax.set_ylabel('y-axis')
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_aspect('equal', adjustable='box')

plot_range = c_range.max() * 1.5
ax.set_xlim(-plot_range, plot_range)
ax.set_ylim(-plot_range, plot_range)

# Create a list of Line2D objects for the transformed grid (initially empty)
# We need one line object for each original line segment
lines_plot = [ax.plot([], [], color='red', linestyle='-', linewidth=1.5, alpha=0.8)[0] for _ in original_lines]

def init():
    """Initializes the animation by plotting the original grid."""
    for line in original_lines:
        # Plot original grid in blue (static background)
        ax.plot(line[0, :], line[1, :], color='blue', linestyle='--', linewidth=0.5, alpha=0.3)
    
    # Return all the mutable line objects
    return lines_plot

def update(frame):
    """Updates the plot for each frame 't'."""
    t = frame / 100  # t goes from 0.0 to 1.0 in 100 steps
    
    # Calculate the intermediate transformation matrix A(t)
    A_interp = (1 - t) * I + t * A_target
    
    # Optional: Update the title to show the current matrix transformation
    ax.set_title(f'Transformation (t={t:.2f})\n $\mathbf{{A}}$ @ Grid')

    # Transform and plot each line segment
    for i, line in enumerate(original_lines):
        transformed_line = A_interp @ line
        
        # Update the data for the corresponding Line2D object
        lines_plot[i].set_data(transformed_line[0, :], transformed_line[1, :])
        
    return lines_plot

# --- 4. Run the Animation ---
# frames=101 to get 0 to 100 inclusive (t=0.00 to t=1.00)
anim = FuncAnimation(fig, update, frames=101, init_func=init, blit=True, interval=50)

# To view the animation (in a Jupyter environment)
plt.show()

# To save the animation as a video file (requires ffmpeg)
# anim.save('linear_transformation_animation.mp4', writer='ffmpeg', fps=20)