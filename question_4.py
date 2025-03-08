import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Function to calculate the angle at which the box leaves the surface
def find_theta(mu_k, m, r, v0, g=9.81):
  
    def equation(theta):
        theta_rad = np.radians(theta)  # angle in radians
        
        # Calculating velocity using conservation of energy
        v = np.sqrt(v0**2 + 2 * g * r * (1 - np.cos(theta_rad)) - 2 * mu_k * g * r * theta_rad)
        
        # Calculating the normal force (centripetal force )
        normal_force = m * (v**2 / r) - m * g * np.cos(theta_rad)
        
        return normal_force  # The angle where normal force becomes zero is the solution
    
    theta_initial_guess = 45  # Provide an initial guess for solving
    theta_solution = fsolve(equation, theta_initial_guess)[0]  # Solve for theta
    
    return theta_solution  # Return the calculated angle

# Given values
m = 0.3  #kg Mass of the block 
r = 2.2  #m Radius of the curved surface 
v0 = 2.5  #m/s Initial velocity 
mu_k_values = np.linspace(0, 0.4, 20)  # Crearing 20 friction values  between and including 0 and 0.4
theta_values = []  # List to store angle results

# angle for each friction value
for mu_k in mu_k_values:
    theta = find_theta(mu_k, m, r, v0)
    theta_values.append(theta)  # Store the  calculated angle

# Plot results
plt.figure(figsize=(8, 6))  # Set plot size
plt.plot(mu_k_values, theta_values, marker='o', linestyle='-')  # Plot mu_k vs theta
plt.xlabel('Coefficient of Friction μ_k')  # Label x-axis
plt.ylabel('Angle θ (degrees)')  # Label y-axis
plt.title('Angle at which Block Leaves Surface vs. Friction')  # Set title
plt.grid()  # Display grid
plt.show()  # Show the plot