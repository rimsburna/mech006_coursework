import numpy as np

# Function to calculate the projectile range 
def projectile_range(v0, alpha, AB, DE, g=9.81):
  
    alpha_rad = np.radians(alpha)  # launch angle in radians
    v0x = v0 * np.cos(alpha_rad)   # Horizontal velocity 
    v0y = v0 * np.sin(alpha_rad)   # Vertical velocity 
    
    # Time to reach the horizontal position AB
    t_B = AB / v0x
    
    # Height of the projectile at position B
    h_B = (v0y * t_B) - (0.5 * g * t_B**2)  
    
    # Total time to hit the ground
    t_total = (2 * v0y) / g
    
    # Total horizontal distance traveled
    d = v0x * t_total
    
    # Horizontal distance based on height conditions
    if h_B == DE:
        return AB  # The projectile just reaches the max allowed height at B ( so it hits the top of the structure)
    elif h_B > DE:
        return d - 3.9  # The projectile exceeds the height of the structure and goes over it, so subtract 3.9m (BE)
    else:
        return d  # The trajectory of the projectile is beneath the height of the structure

# Given values
v0 = 11  #m/s Initial velocity 
AB = 1.2  #m Distance from sprinkler to obstruction
BE = 3.9  #m horizontal distance of structure
DE = 1.5  #m Maximum allowed height 
alpha_min = 25  #degrees Minimum launch angle 
alpha_max = 70  #degrees  Maximum launch angle 

#  distances for different angles
d_values = []
alpha_values = np.arange(alpha_min, alpha_max + 1, 5)  # Angles from 25° to 70° in increments of 5°

# Iterate over different launch angles
for alpha in alpha_values:
    d = projectile_range(v0, alpha, AB, DE)  # The range for each angle
    d_values.append(d)

# Maximum distance and corresponding angle
max_d = max(d_values)
max_angle = alpha_values[np.argmax(d_values)]

# Results for each angle
for angle, distance in zip(alpha_values, d_values):
    print(f"Angle: {angle:.1f} degrees, Distance: {distance:.2f} m")

# The angle that gives the maximum distance
print(f"\nMaximum Distance: {max_d:.2f} m at {max_angle:.1f} degrees")