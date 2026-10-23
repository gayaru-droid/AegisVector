import time
import numpy as np
import matplotlib.pyplot as plt

dt=0.1
g=9.80665

rng=np.random.default_rng()

st_pos=np.r_[rng.uniform(-25,25,size=2),rng.uniform(10,15)]
st_velocity=np.array(rng.uniform(-4,4,size=3))
print(st_pos)
print(st_velocity)

try:
    cur_pos=st_pos.copy()
    cur_z_velocity=st_velocity[2]
    x_positions=[cur_pos[0]]
    y_positions=[cur_pos[1]]
    z_positions=[cur_pos[2]]
    while True:
        print(f'Current position : X={cur_pos[0]:.2f} Y={cur_pos[1]:.2f} Z={cur_pos[2]:.2f}')

        #change x position
        cur_pos[0]=cur_pos[0]-st_velocity[0]*dt
        
        #change y position
        cur_pos[1]=cur_pos[1]-st_velocity[1]*dt

        #change z position and velocity
        cur_pos[2]=(cur_pos[2]+(cur_z_velocity*dt-0.5*g*(dt**2)))
        cur_z_velocity=cur_z_velocity-g*dt
        x_positions.append(cur_pos[0])
        y_positions.append(cur_pos[1])
        z_positions.append(cur_pos[2])
        if (cur_pos[2]<=0):
            print("Missile Hit")
            break
        time.sleep(dt)

    x_positions=(np.array(x_positions))
    y_positions=(np.array(y_positions))
    z_positions=(np.array(z_positions))
    print(z_positions)

    fig,axs=plt.subplots(2)

    axs[0].plot(z_positions)
    axs[0].set_title("Zposition")
    plt.ylabel('Height')
    plt.xlabel('Time')

    axs[1].plot(x_positions,y_positions)
    axs[1].set_title("Horizontal Position")
    plt.ylabel('Yposition')
    plt.xlabel('Xposition')
    
    plt.show()

except KeyboardInterrupt:
    print("Simulation stopped by user")
