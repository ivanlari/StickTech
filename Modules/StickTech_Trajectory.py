def computeTrajectory(solver_outputs, inputs_list):

    from datetime import datetime
    import logging
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    from matplotlib.animation import FuncAnimation
    import os

    t_span  = solver_outputs[0]
    q       = solver_outputs[1]
    t_max   = solver_outputs[2]
    theta   = solver_outputs[3]
    alpha   = solver_outputs[4]
    h       = solver_outputs[5]
    gamma   = solver_outputs[6]
    beta    = solver_outputs[7]
    p       = solver_outputs[8]
    r       = solver_outputs[9]
    phi     = solver_outputs[10]
    u       = solver_outputs[11]
    w       = solver_outputs[12]
    psi     = solver_outputs[13]

    # Velocità complessiva
    U0      = inputs_list[7]
    V0      = 0
    W0      = 0
    v       = beta*U0
    U = U0 + u
    V = V0 + v 
    W = W0 + w

    # Posizioni iniziali
    x0, y0, z0 = 0, 0, 0

    # Passo temporale
    dt = np.mean(np.diff(t_span))  # Supponendo che t_span sia uniforme

    # Integrazione numerica cumulativa delle velocità
    x = x0 + np.cumsum(U * dt)
    y = y0 + np.cumsum(V * dt)
    z = z0 + np.cumsum(W * dt)

    def plotTrajectory(x, y, z):

        # Create a 3D plot
        fig = plt.figure("Aircraft Trajectory")
        ax = fig.add_subplot(111, projection='3d')

        # Plot the trajectory
        ax.plot(x, y, z, label='Aircraft Trajectory', color='red', lw=2)

        # Add labels and title
        ax.set_title('Trajectory of the Aircraft')
        ax.set_xlabel('X (m)')
        ax.set_ylabel('Y (m)')
        ax.set_zlabel('Z (m)')

        # Adjust tick label size
        ax.tick_params(axis='x', labelsize=9)
        ax.tick_params(axis='y', labelsize=9)
        ax.tick_params(axis='z', labelsize=9)

        # Uniform scale for axes
        max_range = np.array([x.max() - x.min(), y.max() - y.min(), z.max() - z.min()]).max() / 2.0
        mid_x = (x.max() + x.min()) * 0.5
        mid_y = (y.max() + y.min()) * 0.5
        mid_z = (z.max() + z.min()) * 0.5
        
        delta_x = abs(x.max()-x.min())
        delta_y = abs(y.max()-y.min())
        delta_z = abs(z.max()-z.min())

        if delta_y < 10**(-3):
            ax.set_ylim(mid_y - max_range, mid_y + max_range)
        
        if delta_z < 10**(-3):
            ax.set_zlim(mid_z - max_range, mid_z + max_range)


        # Add a legend
        #ax.legend()

        plt.savefig("Aircraft_Trajectory.png", dpi=300)
        plt.show()

    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Opening Trajectory plot...")
    logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Opening Trajectory plot...")

    plotTrajectory(x, y, z)

    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Trajectory plot has been saved.")
    logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Trajectory plot has been saved.")