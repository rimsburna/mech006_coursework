import numpy as np
import pandas as pd

# Function to calculate velocities after collision and the % energy loss
def velocity_after_collision(mA, mB, v0, theta, e):
   
    theta_rad = np.radians(theta)  # angle in radians
    v0x = v0 * np.sin(theta_rad)  # horizontal component of initial velocity
    
    # conservation of momentum (CoM) in the horizontal direction
    vA_after = ((mA - e * mB) * v0x) / (mA + mB)
    vB_after = ((1 + e) * mA * v0x) / (mA + mB)
    
    # initial and final kinetic energy
    KE_initial = 0.5 * mA * v0x**2
    KE_final = 0.5 * mA * vA_after**2 + 0.5 * mB * vB_after**2
    
    # % energy loss
    energy_loss = ((KE_initial - KE_final) / KE_initial) * 100  
    
    # Rounding small numerical errors to zero
    if abs(energy_loss) < 1e-10:
        energy_loss = 0.0
    
    # results rounded to two decimal places
    return round(vA_after, 2), round(vB_after, 2), round(energy_loss, 2)

mB = 500  #g Mass of B 
mA = 200  #g Mass of A 
v0 = 5  #m/s Initial velocity of A 
theta_min = 10  #degrees Minimum angle of impact 
theta_max = 145  #degrees Maximum angle of impact
e_values = [1, 0.75, 0]  # restitution coefficients

theta_values = np.arange(theta_min, theta_max + 1, 5)  # angles from 10° to 145° in increments of 5°

# Iterate over different restitution coefficients
for e in e_values:
    data = []  # Storing the results for each restitution value
    
    for theta in theta_values:
        vA, vB, energy_loss = velocity_after_collision(mA, mB, v0, theta, e)  # Computing the values
        data.append([theta, vA, vB, energy_loss])  # storing the results
    
    # Dataframe for displaying results
    df = pd.DataFrame(data, columns=["Theta (degrees)", "Velocity of A (m/s)", "Velocity of B (m/s)", "Energy Loss (%)"])
    
    # Results in a table
    print(f"\nTable for e = {e}")
    print(df.to_string(index=False))
