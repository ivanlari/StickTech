def animate_outputs(solver_outputs, plots_inputs_list, inputs_list):

    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation
    from datetime import datetime
    import logging

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

    t_e     = plots_inputs_list[0]
    tau_e   = plots_inputs_list[1]
    de_deg  = plots_inputs_list[2]
    t_r     = plots_inputs_list[3]
    tau_r   = plots_inputs_list[4]
    dr_deg  = plots_inputs_list[5]
    t_a     = plots_inputs_list[6]
    tau_a   = plots_inputs_list[7]
    da_deg  = plots_inputs_list[8]

    equilibratore   = inputs_list[13]
    alettone        = inputs_list[28]
    timone          = inputs_list[29]

    # Generate points for command inputs
    elevator = []
    for i in range(len(t_span)):
        elevator.append(equilibratore(t_span[i])*de_deg)
    
    aileron = []
    for i in range(len(t_span)):
        aileron.append(alettone(t_span[i])*da_deg)

    rudder = []
    for i in range(len(t_span)):
        rudder.append(timone(t_span[i])*dr_deg)

    t_list = []
    dT = t_span[1]-t_span[0] # delta T



    # Longitudinal
    fig_LO_an = plt.figure(figsize=(12, 7))

    # q
    plt.subplot(3, 2, 1)
    plt.grid(which='major', color='k', linestyle=':', linewidth=0.2)
    plt.suptitle('Longitudinal Dynamics', fontsize=16)
    plt.ylabel('$q$ $(deg/s)$', fontsize=12)
    plt.xlim((0, t_max))
    plt.ylim((min(q)-0.5, max(q)+0.5))
    q_list = []
    ln_q, = plt.plot(t_list, q_list, linewidth=1.2, ls="-", color='b')

    # theta
    plt.subplot(3, 2, 2)
    plt.grid(which='major', color='k', linestyle=':', linewidth=0.2)
    plt.ylabel('$\u03B8$ $(deg)$', fontsize=12)
    plt.xlim((0, t_max))
    plt.ylim((min(theta)-0.5, max(theta)+0.5))
    theta_list = []
    ln_theta, = plt.plot(t_list, theta_list, linewidth=1.2, ls="-", color='b')

    # alpha
    plt.subplot(3, 2, 3)
    plt.grid(which='major', color='k', linestyle=':', linewidth=0.2)
    plt.ylabel('$\u03B1$ $(deg)$', fontsize=12)
    plt.xlim((0, t_max))
    plt.ylim((min(alpha)-0.5, max(alpha)+0.5))
    alpha_list = []
    ln_alpha, = plt.plot(t_list, alpha_list, linewidth=1.2, ls="-", color='b')

    # h
    plt.subplot(3, 2, 4)
    plt.grid(which='major', color='k', linestyle=':', linewidth=0.2)
    plt.ylabel('$h$ $(m)$', fontsize=12)
    plt.xlim((0, t_max))
    plt.ylim((min(h)-10, max(h)+10))
    h_list = []
    ln_h, = plt.plot(t_list, h_list, linewidth=1.2, ls="-", color='b')

        # gamma
    plt.subplot(3, 2, 5)
    plt.grid(which='major', color='k', linestyle=':', linewidth=0.2)
    plt.ylabel('$\u03B3$ $(deg)$', fontsize=12)
    plt.xlim((0, t_max))
    plt.ylim((min(gamma)-0.5, max(gamma)+0.5))
    plt.xlabel('$t$ $(s)$', fontsize=12)
    gamma_list = []
    ln_gamma, = plt.plot(t_list, gamma_list, linewidth=1.2, ls="-", color='b')

    # Elevator
    plt.subplot(3, 2, 6)
    plt.grid(which='major', color='k', linestyle=':', linewidth=0.2)
    plt.ylabel('$\u03B4_e$ $(deg)$', fontsize=12)
    plt.xlim((0, t_max))
    plt.ylim((min(elevator)-1, max(elevator)+1))
    plt.xlabel('$t$ $(s)$', fontsize=12)
    de_list = []
    ln_de, = plt.plot(t_list, de_list, linewidth=1.2, ls="-", color='r')

    def update_lon(i):

        t_list.append(t_span[i])

        # q
        q_list.append(q[i])
        ln_q.set_data(t_list, q_list) 

        # theta
        theta_list.append(theta[i])
        ln_theta.set_data(t_list, theta_list) 

        # alpha
        alpha_list.append(alpha[i])
        ln_alpha.set_data(t_list, alpha_list) 

        # h
        h_list.append(h[i])
        ln_h.set_data(t_list, h_list)

        # gamma
        gamma_list.append(gamma[i])
        ln_gamma.set_data(t_list, gamma_list)

        # de
        de_list.append(elevator[i])
        ln_de.set_data(t_list, de_list)

        return ln_q, ln_theta, ln_alpha, ln_h, ln_gamma, ln_de,

    print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Generating Animation for the Longitudinal Dynamics. Please wait...")
    logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Generating Animation for the Longitudinal Dynamics...")
    animation_lon = FuncAnimation(fig_LO_an, update_lon, frames=len(t_span), interval=dT*1000)
    animation_lon.save('Longitudinal_Dynamics_Animation.mp4', fps=1/dT)
    #plt.show()
    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Animation has been saved.")
    logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Animation has been saved.")
    plt.close('all')

    

    # Lateral-Directional
    fig_LD_an = plt.figure(figsize=(12, 7))
    
    # re-initiate t_list
    t_list = []

    # Beta
    plt.subplot(3, 2, 1)
    plt.grid(which='major', color='k', linestyle=':', linewidth=0.2)
    plt.ylabel('$\u03B2$ $(deg)$', fontsize=12)
    plt.suptitle('Lateral-Directional Dynamics', fontsize=16)
    plt.xlim((0, t_max))
    plt.ylim((min(beta)-0.5, max(beta)+0.5))
    beta_list = []
    ln_beta, = plt.plot(t_list, beta_list, linewidth=1.2, ls="-", color='b')

    # p
    plt.subplot(3, 2, 2)
    plt.grid(which='major', color='k', linestyle=':', linewidth=0.2)
    plt.ylabel('$p$ $(deg/s)$', fontsize=12)
    plt.xlim((0, t_max))
    plt.ylim((min(p)-0.5, max(p)+0.5))
    p_list = []
    ln_p, = plt.plot(t_list, p_list, linewidth=1.2, ls="-", color='b')

    # r
    plt.subplot(3, 2, 3)
    plt.grid(which='major', color='k', linestyle=':', linewidth=0.2)
    plt.ylabel('$r$ $(deg/s)$', fontsize=12)
    plt.xlabel('$t$ $(s)$', fontsize=12)
    plt.xlim((0, t_max))
    plt.ylim((min(r)-0.5, max(r)+0.5))
    r_list = []
    ln_r, = plt.plot(t_list, r_list, linewidth=1.2, ls="-", color='b')

    # phi
    plt.subplot(3, 2, 4)
    plt.grid(which='major', color='k', linestyle=':', linewidth=0.2)
    plt.ylabel('$\u03C6$ $(deg)$', fontsize=12)
    plt.xlabel('$t$ $(s)$', fontsize=12)
    plt.xlim((0, t_max))
    plt.ylim((min(phi)-0.5, max(phi)+0.5))
    phi_list = []
    ln_phi, = plt.plot(t_list, phi_list, linewidth=1.2, ls="-", color='b')

    # Rudder
    plt.subplot(3, 2, 5)
    plt.grid(which='major', color='k', linestyle=':', linewidth=0.2)
    plt.ylabel('$\u03B4_r$ $(deg)$', fontsize=12)
    plt.xlim((0, t_max))
    plt.ylim((min(rudder)-1, max(rudder)+1))
    plt.xlabel('$t$ $(s)$', fontsize=12)
    dr_list = []
    ln_dr, = plt.plot(t_list, dr_list, linewidth=1.2, ls="-", color='r')

    # Aileron
    plt.subplot(3, 2, 6)
    plt.grid(which='major', color='k', linestyle=':', linewidth=0.2)
    plt.ylabel('$\u03B4_a$ $(deg)$', fontsize=12)
    plt.xlim((0, t_max))
    plt.ylim((min(aileron)-1, max(aileron)+1))
    plt.xlabel('$t$ $(s)$', fontsize=12)
    da_list = []
    ln_da, = plt.plot(t_list, da_list, linewidth=1.2, ls="-", color='r')

    def update_lat(i):

        t_list.append(t_span[i])

        # beta
        beta_list.append(beta[i])
        ln_beta.set_data(t_list, beta_list) 

        # p
        p_list.append(p[i])
        ln_p.set_data(t_list, p_list) 

        # r
        r_list.append(r[i])
        ln_r.set_data(t_list, r_list)

        # phi
        phi_list.append(phi[i])
        ln_phi.set_data(t_list, phi_list)

        # rudder
        dr_list.append(rudder[i])
        ln_dr.set_data(t_list, dr_list)

        # rudder
        da_list.append(aileron[i])
        ln_da.set_data(t_list, da_list)

        return ln_beta, ln_p, ln_r, ln_phi, ln_dr, ln_da,

    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Generating Animation for the Lateral-Directional Dynamics. Please wait...")
    logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Generating Animation for the Lateral-Directional Dynamics...")
    animation_lat = FuncAnimation(fig_LD_an, update_lat, frames=len(t_span), interval=dT*1000)
    animation_lat.save('LateralDirectional_Dynamics_Animation.mp4', fps=1/dT)
    #plt.show()
    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Animation has been saved.")
    logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Animation has been saved.")
    plt.close('all')