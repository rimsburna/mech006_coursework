import numpy as np

m = 2  # kg
AC = 2.3  # m (length of the rope)
Fm_min = 20  # N (tension)
Fm_max = 150  # N ( tension)
CD = 2.7  # m (height from A to the ground)
g = 9.81  # m/s² 

def find_breaking_height(Fm, m, AC):
    # height difference h and breaking angle
    arccos_argument = (3 * m * g - Fm) / (2 * m * g)

    # Ensure arccos argument is within [-1,1] to avoid errors
    if not (-1 <= arccos_argument <= 1):
        return None, None  # Invalid case

    theta = np.arccos(arccos_argument)  # Breaking angle (radians)
    h = AC * (1 - np.cos(theta))  # Height difference
    return h, theta 

def find_landing_distance(h, CD, AC, theta):
    H = CD - h  # Height from B to the ground
    if H < 0:
        return None  # Invalid case

    # velocity at B
    vB = np.sqrt(2 * g * h)  # (from potential energy loss)
    
    # Horizontal velocity at B
    vB_x = vB * np.sin(theta)  

    #  time of flight using projectile motion
    time_fall = np.sqrt(2 * H / g)  
    
    d = vB_x * time_fall  # Horizontal distance
    return d

# values of h and d for forces between 20N and 150N
results = []
for Fm in range(Fm_min, Fm_max + 1, 10):
    h, theta = find_breaking_height(Fm, m, AC)
    
    if h is None:
        results.append((Fm, "Invalid", "Invalid"))
        continue

    d = find_landing_distance(h, CD, AC, theta)
    
    if d is None:
        results.append((Fm, h, "Invalid"))
    else:
        results.append((Fm, h, d))

# results in a table
print(f"{'Fm (N)':<10}{'h (m)':<10}{'d (m)':<10}")
print("-" * 30)
for Fm, h, d in results:
    h_str = f"{h:.2f}" if h != "Invalid" else "Invalid"
    d_str = f"{d:.2f}" if d != "Invalid" else "Invalid"
    print(f"{Fm:<10}{h_str:<10}{d_str:<10}")

