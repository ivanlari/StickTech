def plots(solver_outputs, plots_inputs_list, dynamics_outputs):

    import matplotlib.pyplot as plt
    from matplotlib.pyplot import legend
    import math
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

    t_e     = plots_inputs_list[0]
    tau_e   = plots_inputs_list[1]
    de_deg  = plots_inputs_list[2]
    t_r     = plots_inputs_list[3]
    tau_r   = plots_inputs_list[4]
    dr_deg  = plots_inputs_list[5]
    t_a     = plots_inputs_list[6]
    tau_a   = plots_inputs_list[7]
    da_deg  = plots_inputs_list[8]

    w_SP        = dynamics_outputs[0]
    z_SP        = dynamics_outputs[1]
    w_LP        = dynamics_outputs[2]
    z_LP        = dynamics_outputs[3]
    p_roll      = dynamics_outputs[4]
    p_spiral    = dynamics_outputs[5]
    w_DR        = dynamics_outputs[6]
    z_DR        = dynamics_outputs[7]
    
    # Longitudinale
    fig_LO = plt.figure(figsize=(12, 7), dpi=300)

    # q
    plt.subplot(3, 2, 1)
    plt.grid(b=True, which='major', color='k', linestyle=':', linewidth=0.2)
    plt.suptitle('Longitudinal Dynamics', fontsize=16)
    plt.plot(t_span,q, linewidth=1.2, ls="-", color='b')
    plt.xlim((0, t_max))
    plt.ylabel('$q$ $(deg/s)$', fontsize=12)

    # theta
    plt.subplot(3, 2, 2)
    plt.grid(b=True, which='major', color='k', linestyle=':', linewidth=0.2)
    plt.plot(t_span,theta, linewidth=1.2, ls="-", color='b')
    plt.xlim((0, t_max))
    plt.ylabel('$\u03B8$ $(deg)$', fontsize=12)

    # alpha
    plt.subplot(3, 2, 3)
    plt.grid(b=True, which='major', color='k', linestyle=':', linewidth=0.2)
    plt.plot(t_span,alpha, linewidth=1.2, ls="-", color='b')
    plt.xlim((0, t_max))
    plt.ylabel('$\u03B1$ $(deg)$', fontsize=12)

    # h
    plt.subplot(3, 2, 4)
    plt.grid(b=True, which='major', color='k', linestyle=':', linewidth=0.2)
    plt.plot(t_span,h, linewidth=1.2, ls="-", color='b')
    plt.xlim((0, t_max))
    #plt.ylim((-0.5, 0.5))
    plt.ylabel('$h$ $(m)$', fontsize=12)

    # gamma
    plt.subplot(3, 2, 5)
    plt.grid(b=True, which='major', color='k', linestyle=':', linewidth=0.2)
    plt.plot(t_span,gamma, linewidth=1.2, ls="-", color='b')
    plt.xlim((0, t_max))
    plt.ylabel('$\u03B3$ $(deg)$', fontsize=12)
    plt.xlabel('$t$ $(s)$', fontsize=12)

    # Comando di equilibratore
    plt.subplot(3, 2, 6)
    plt.grid(b=True, which='major', color='k', linestyle=':', linewidth=0.2)
    plt.plot([0, t_e], [0, 0], linewidth=1.2, ls="-", color='r')
    plt.plot([t_e, t_e+tau_e], [de_deg, de_deg], linewidth=1.2, ls="-", color='r')
    plt.plot([t_e+tau_e, t_max], [0, 0], linewidth=1.2, ls="-", color='r')
    plt.plot([t_e, t_e], [0, de_deg], linewidth=1.2, ls="-", color='r')
    plt.plot([t_e+tau_e, t_e+tau_e], [0, de_deg], linewidth=1.2, ls="-", color='r')
    plt.xlim((0, t_max))
    plt.ylabel('$\u03B4_e$ $(deg)$', fontsize=12)
    plt.xlabel('$t$ $(s)$', fontsize=12)

    figname_LO = "Longitudinal_Dynamics.png"
    plt.savefig(figname_LO)
    #os.system(figname_LO)

    # Latero-Direzionale
    fig_LD = plt.figure(figsize=(12, 7), dpi=300)

    # Beta
    plt.subplot(3, 2, 1)
    plt.grid(b=True, which='major', color='k', linestyle=':', linewidth=0.2)
    plt.suptitle('Lateral-Directional Dynamics', fontsize=16)
    plt.plot(t_span,beta, linewidth=1.2, ls="-", color='b')
    #plt.title('Velocità')
    #plt.xlabel('$ $ $(s)$', fontsize=12)
    plt.xlim((0, t_max))
    plt.ylabel('$\u03B2$ $(deg)$', fontsize=12)

    # p
    plt.subplot(3, 2, 2)
    plt.grid(b=True, which='major', color='k', linestyle=':', linewidth=0.2)
    plt.plot(t_span,p, linewidth=1.2, ls="-", color='b')
    #plt.title('Velocità')
    #plt.xlabel('$Tempo$ $(s)$', fontsize=12)
    plt.xlim((0, t_max))
    plt.ylabel('$p$ $(deg/s)$', fontsize=12)
    bbox = dict(boxstyle="round", fc="1")

    # r
    plt.subplot(3, 2, 3)
    plt.grid(b=True, which='major', color='k', linestyle=':', linewidth=0.2)
    plt.plot(t_span,r, linewidth=1.2, ls="-", color='b')
    #plt.title('Velocità')
    plt.xlabel('$t$ $(s)$', fontsize=12)
    plt.xlim((0, t_max))
    plt.ylabel('$r$ $(deg/s)$', fontsize=12)
    bbox = dict(boxstyle="round", fc="1")

    # phi
    plt.subplot(3, 2, 4)
    plt.grid(b=True, which='major', color='k', linestyle=':', linewidth=0.2)
    plt.plot(t_span,phi, linewidth=1.2, ls="-", color='b')
    #plt.title('Velocità')
    plt.xlabel('$t$ $(s)$', fontsize=12)
    plt.xlim((0, t_max))
    plt.ylabel('$\u03C6$ $(deg)$', fontsize=12)
    bbox = dict(boxstyle="round", fc="1")

    # Comando di timone
    plt.subplot(3, 2, 5)
    plt.grid(b=True, which='major', color='k', linestyle=':', linewidth=0.2)
    plt.plot([0, t_r], [0, 0], linewidth=1.2, ls="-", color='r')
    plt.plot([t_r, t_r+tau_r], [dr_deg, dr_deg], linewidth=1.2, ls="-", color='r')
    plt.plot([t_r+tau_r, t_max], [0, 0], linewidth=1.2, ls="-", color='r')
    plt.plot([t_r, t_r], [0, dr_deg], linewidth=1.2, ls="-", color='r')
    plt.plot([t_r+tau_r, t_r+tau_r], [0, dr_deg], linewidth=1.2, ls="-", color='r')
    plt.xlim((0, t_max))
    plt.ylabel('$\u03B4_r$ $(deg)$', fontsize=12)
    plt.xlabel('$t$ $(s)$', fontsize=12)

    # Comando di alettone
    plt.subplot(3, 2, 6)
    plt.grid(b=True, which='major', color='k', linestyle=':', linewidth=0.2)
    plt.plot([0, t_a], [0, 0], linewidth=1.2, ls="-", color='r')
    plt.plot([t_a, t_a+tau_a], [da_deg, da_deg], linewidth=1.2, ls="-", color='r')
    plt.plot([t_a+tau_a, t_max], [0, 0], linewidth=1.2, ls="-", color='r')
    plt.plot([t_a, t_a], [0, da_deg], linewidth=1.2, ls="-", color='r')
    plt.plot([t_a+tau_a, t_a+tau_a], [0, da_deg], linewidth=1.2, ls="-", color='r')
    plt.xlim((0, t_max))
    plt.ylabel('$\u03B4_a$ $(deg)$', fontsize=12)
    plt.xlabel('$t$ $(s)$', fontsize=12)

    figname_LD = "LateralDirectional_Dynamics.png"
    plt.savefig(figname_LD)
    #os.system(figname_LD)

    # Poles
    fig_poles = plt.figure(figsize=(12, 7), dpi=300)

    # Longitudinal
    plt.subplot(1, 2, 1)
    plt.grid(b=True, which='major', color='k', linestyle=':', linewidth=0.2)
    plt.suptitle('Poles Placement', fontsize=16)
    plt.plot([-z_SP*w_SP, -z_SP*w_SP], [w_SP*math.sqrt(1-z_SP**2), -w_SP*math.sqrt(1-z_SP**2)], 'x', 
             markersize=12, markeredgewidth=2, color='blue', label="Short Period")
    plt.plot([-z_LP*w_LP, -z_LP*w_LP], [w_LP*math.sqrt(1-z_LP**2), -w_LP*math.sqrt(1-z_LP**2)], 'x', 
             markersize=12, markeredgewidth=2, color='green', label="Phugoid")
    plt.xlabel('$Re$', fontsize=14)
    plt.ylabel('$Im$', fontsize=14)
    plt.title("Longitudinal", fontsize=14)
    plt.legend(loc="upper right", fontsize=12)

    # Lateral
    plt.subplot(1, 2, 2)
    plt.grid(b=True, which='major', color='k', linestyle=':', linewidth=0.2)
    plt.plot([-p_roll], [0], 'x', markersize=12, markeredgewidth=2, color='m', label="Roll")
    plt.plot([-p_spiral], [0], 'x', markersize=12, markeredgewidth=2, color='darkcyan', label="Spiral")
    plt.plot([-z_DR*w_DR, -z_DR*w_DR], [w_DR*math.sqrt(1-z_DR**2), -w_DR*math.sqrt(1-z_DR**2)], 'x', 
             markersize=12, markeredgewidth=2, color='red', label="Dutch Roll")
    plt.xlabel('$Re$', fontsize=14)
    #plt.ylabel('$Im$', fontsize=12)
    plt.title("Lateral-Directional", fontsize=14)
    plt.legend(loc="upper left", fontsize=12)

    figname_poles = "Poles_Placement.png"
    plt.savefig(figname_poles)
    #os.system(figname_poles)

    plt.close('all')

    print("\nAnalysis completed.")
    print("Output images and text files have been created. \nClick 'View Results' to open the solution outputs.")