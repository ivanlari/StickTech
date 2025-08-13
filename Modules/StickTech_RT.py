def runRT(inputs_list, GUI_outputs_2, code_build):  
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.widgets import Slider, Button
    from mpl_toolkits.mplot3d.art3d import Poly3DCollection
    import math
    from datetime import datetime
    import logging
    import matplotlib.cm as cm
    import matplotlib.colors as mcolors

    print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Opening RT...")
    logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Opening RT...")

    # Parametri
    Xu = inputs_list[0]
    Xw = inputs_list[1]
    g = inputs_list[2]
    Zu = inputs_list[3]
    Zw = inputs_list[4]
    Zde = inputs_list[5]
    de = 0
    U0 = inputs_list[7]
    Mu = inputs_list[8]
    Mw = inputs_list[9]
    Mw_dot = inputs_list[10]
    Mq = inputs_list[11]
    Mde = inputs_list[12]
    equilibratore = inputs_list[13]
    Yv = inputs_list[14]
    Ydr_star = inputs_list[15]
    dr = 0
    Lb_apice = inputs_list[17]
    Lp_apice = inputs_list[18]
    Lr_apice = inputs_list[19]
    Lda_apice = inputs_list[20]
    da = 0
    Ldr_apice = inputs_list[22]
    Nb_apice = inputs_list[23]
    Np_apice = inputs_list[24]
    Nr_apice = inputs_list[25]
    Nda_apice = inputs_list[26]
    Ndr_apice = inputs_list[27]
    alettone = inputs_list[28]
    timone = inputs_list[29]
    t_e = inputs_list[30]
    tau_e = inputs_list[31]
    de_deg = inputs_list[32]
    t_r = inputs_list[33]
    tau_r = inputs_list[34]
    dr_deg = inputs_list[35]
    t_a = inputs_list[36]
    tau_a = inputs_list[37]
    da_deg = inputs_list[38]
    Xdt = inputs_list[39]
    Zdt = inputs_list[40]
    Mdt = inputs_list[41]
    t_t = inputs_list[42]
    tau_t = inputs_list[43]
    dt = inputs_list[44]
    thrust = inputs_list[45]

    # Condizioni iniziali
    e43 = GUI_outputs_2[0]
    e44 = GUI_outputs_2[1]
    e45 = GUI_outputs_2[2]
    e46 = GUI_outputs_2[3]
    e47 = GUI_outputs_2[4]
    e48 = GUI_outputs_2[5]
    e49 = GUI_outputs_2[6]
    e50 = GUI_outputs_2[7]
    e51 = GUI_outputs_2[8]
    e52 = GUI_outputs_2[9]

    delta_X0 = 0
    u0 = float(e43.get()) + delta_X0
    w0 = float(e44.get()) + delta_X0
    q0 = float(e45.get()) + delta_X0
    theta0 = float(e46.get()) + delta_X0
    h0 = float(e47.get()) + delta_X0
    beta0 = float(e48.get()) + delta_X0
    p0 = float(e49.get()) + delta_X0
    r0 = float(e50.get()) + delta_X0
    phi0 = float(e51.get()) + delta_X0
    psi0 = float(e52.get()) + delta_X0

    throttle_eq = max(0, -(Xu * U0) / Xdt)

    state_lon = np.array([u0, w0, q0, theta0, h0])
    state_lat = np.array([beta0, p0, r0, phi0, psi0])

    state_lon[2] = math.radians(state_lon[2])
    state_lon[3] = math.radians(state_lon[3])
    for j in range(len(state_lat)):
        state_lat[j] = math.radians(state_lat[j])

    def model_LON(X_lon, de, throttle):
        u, w, q, theta, h = X_lon
        du_dt = Xu*u + Xw*w - g*theta + Xdt*throttle
        dw_dt = Zu*u + Zw*w + Zde*de + U0*q + Zdt*throttle
        dq_dt = Mu*u + Mw*w + Mw_dot*dw_dt + Mq*q + Mde*de + Mdt*throttle
        dtheta_dt = q
        dh_dt = U0*theta - w
        return np.array([du_dt, dw_dt, dq_dt, dtheta_dt, dh_dt])

    def model_LAT(X_lat, da, dr):
        beta, p, r, phi, psi = X_lat
        dbeta_dt = Yv*beta + g/U0*phi + Ydr_star*dr - r
        dp_dt = Lb_apice*beta + Lp_apice*p + Lr_apice*r + Lda_apice*da + Ldr_apice*dr
        dr_dt = Nb_apice*beta + Np_apice*p + Nr_apice*r + Nda_apice*da + Ndr_apice*dr
        dphi_dt = p
        dpsi_dt = r
        return np.array([dbeta_dt, dp_dt, dr_dt, dphi_dt, dpsi_dt])
    
    def rk4_step(func, state, dt, *args):
        k1 = func(state, *args)
        k2 = func(state + 0.5 * dt * k1, *args)
        k3 = func(state + 0.5 * dt * k2, *args)
        k4 = func(state + dt * k3, *args)
        return state + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
        

    # --- Punti originali per superfici ---
    scale = 3

    # 1. Ala centrale (senza alettoni)
    wing_half_span = 2.8 * scale / 2
    chord = 0.3 * scale

    center_span = wing_half_span / 2       # metà centrale con corda intera
    outer_span = wing_half_span * 2 / 3    # metà estremità per fixed + alettrone

    # 1. Parte centrale con corda completa
    wing_center = np.array([
        [-chord / 2,     -center_span, 0],
        [ chord / 2,     -center_span, 0],
        [ chord / 2,      center_span, 0],
        [-chord / 2,      center_span, 0]
    ])

    # 2. Estremità sinistra - fixed (corda metà destra)
    left_fixed = np.array([
        [-chord / 4,              -wing_half_span, 0],
        [ chord / 2,     -wing_half_span, 0],
        [ chord / 2,     -center_span, 0],
        [-chord / 4,              -center_span, 0]
    ])

    # 3. Estremità sinistra - alettrone (corda metà sinistra)
    left_aileron = np.array([
        [-chord / 2,     -wing_half_span, 0],
        [-chord / 4,              -wing_half_span, 0],
        [-chord / 4,              -center_span, 0],
        [-chord / 2,     -center_span, 0]
    ])

    # 4. Estremità destra - fixed (corda metà destra)
    right_fixed = np.array([
        [-chord / 4,              center_span, 0],
        [ chord / 2,     center_span, 0],
        [ chord / 2,     wing_half_span, 0],
        [-chord / 4,              wing_half_span, 0]
    ])

    # 5. Estremità destra - alettrone (corda metà sinistra)
    right_aileron = np.array([
        [-chord / 2,     center_span, 0],
        [-chord / 4,              center_span, 0],
        [-chord / 4,              wing_half_span, 0],
        [-chord / 2,     wing_half_span, 0]
    ])




    offset_elevator = 0.125 * scale / 2
    x_min = -2.0 * scale / 2 - 0.2 * scale / 2
    x_max = -2.0 * scale / 2 + 0.2 * scale / 2
    y_min = -0.8 * scale / 2
    y_max = 0.8 * scale / 2

    # Piano orizzontale senza alettone
    tail_horizontal_points = np.array([
        [x_min + offset_elevator, y_min, 0],
        [x_max,         y_min, 0],
        [x_max,         y_max, 0],
        [x_min + offset_elevator, y_max, 0]
    ])

    # Equilibratore
    tail_horizontal_aileron = np.array([
        [x_min,          y_min, 0],
        [x_min + offset_elevator, y_min, 0],
        [x_min + offset_elevator, y_max, 0],
        [x_min,          y_max, 0]
    ])

    offset_rudder = 0.125 * scale / 2

    # Coda verticale senza timone (fisso)
    tail_vertical_points = np.array([
        [-2.0 * scale / 2, 0, 0],
        [-2.0 * scale / 2, 0, 0.3 * scale],
        [-2.0 * scale / 2 - 0.2 * scale + offset_rudder, 0, 0.3 * scale],  # taglio timone in alto
        [-2.0 * scale / 2 - 0.2 * scale + offset_rudder, 0, 0]             # taglio timone in basso
    ])

    # Timone (mobile)
    tail_vertical_rudder = np.array([
        [-2.0 * scale / 2 - 0.2 * scale + offset_rudder, 0, 0],            # punto davanti timone (taglio)
        [-2.0 * scale / 2 - 0.2 * scale + offset_rudder, 0, 0.3 * scale],  # punto davanti timone in alto
        [-2.0 * scale / 2 - 0.2 * scale, 0, 0.3 * scale],                  # punta posteriore timone in alto
        [-2.0 * scale / 2 - 0.2 * scale, 0, 0]                             # punta posteriore timone in basso
    ])

    transparence = 0.65
    color_general = "grey"
    color_aileron = "blue"
    color_elevator = "blue"
    color_rudder = "blue"

    def draw_airplane(ax, R):
        fuselage_points = np.array([[-2.0 * scale / 2, 0, 0],
                                    [ 2.0 * scale / 2, 0, 0]])
        fuselage_rotated = (R @ fuselage_points.T).T
        ax.plot(fuselage_rotated[:, 0], fuselage_rotated[:, 1], fuselage_rotated[:, 2],
                color="grey", lw=4)

        wing_center_rotated = (R @ wing_center.T).T
        left_fixed_rotated = (R @ left_fixed.T).T
        right_fixed_rotated = (R @ right_fixed.T).T
        tail_h_rotated = (R @ tail_horizontal_points.T).T
        tail_v_rotated = (R @ tail_vertical_points.T).T
        left_aileron_rotated = (R @ left_aileron.T).T
        right_aileron_rotated = (R @ right_aileron.T).T
        elevator_rotated = (R @ tail_horizontal_aileron.T).T
        rudder_rotated = (R @ tail_vertical_rudder.T).T

        wing_center_poly = Poly3DCollection([wing_center_rotated], color=color_general, alpha=transparence)
        left_fixed_poly = Poly3DCollection([left_fixed_rotated], color=color_general, alpha=transparence)
        right_fixed_poly = Poly3DCollection([right_fixed_rotated], color=color_general, alpha=transparence)
        tail_h_poly = Poly3DCollection([tail_h_rotated], color=color_general, alpha=transparence)
        tail_v_poly = Poly3DCollection([tail_v_rotated], color=color_general, alpha=transparence)
        left_aileron_poly = Poly3DCollection([left_aileron_rotated], color=color_aileron, alpha=transparence)
        right_aileron_poly = Poly3DCollection([right_aileron_rotated], color=color_aileron, alpha=transparence)
        elevator_poly = Poly3DCollection([elevator_rotated], color=color_elevator, alpha=transparence)
        rudder_poly = Poly3DCollection([rudder_rotated], color=color_rudder, alpha=transparence)

        ax.add_collection3d(wing_center_poly)
        ax.add_collection3d(left_fixed_poly)
        ax.add_collection3d(right_fixed_poly)
        ax.add_collection3d(tail_h_poly)
        ax.add_collection3d(tail_v_poly)
        ax.add_collection3d(left_aileron_poly)
        ax.add_collection3d(right_aileron_poly)
        ax.add_collection3d(elevator_poly)
        ax.add_collection3d(rudder_poly)

        return wing_center_poly, left_fixed_poly, right_fixed_poly, tail_h_poly, tail_v_poly, left_aileron_poly, right_aileron_poly, elevator_poly, rudder_poly


    fig = plt.figure("StickTech " + code_build + " - RealTime", figsize=(14, 7))
    import matplotlib.gridspec as gridspec
    gs = gridspec.GridSpec(3, 2, figure=fig)
    ax_graphics = [fig.add_subplot(3, 1, i+1) for i in range(3)]
    for i, ax in enumerate(ax_graphics):
        ax.set_position(gs[i, 0].get_position(fig))
        ax.set_subplotspec(gs[i, 0])
    ax_3d = fig.add_subplot(gs[:, 1], projection='3d')
    ax_3d.set_title("StickTech $RealTime$ Animator", fontsize=14)
    plt.subplots_adjust(left=0.1, bottom=0.3, right=0.9, top=0.95, wspace=0.3, hspace=0.4)

    titles = ["$\u03B8$ $(deg)$", "$\u03C6$ $(deg)$", "$\u03C8$ $(deg)$"]
    y_labels = ["$\u03B8$ $(deg)$", "$\u03C6$ $(deg)$", "$\u03C8$ $(deg)$"]
    for i, (ax, title) in enumerate(zip(ax_graphics, titles)):
        ax.set_xlim(0, 10)
        ax.set_ylim(-20, 20)
        ax.grid(True, color='gray', linestyle='--', linewidth=0.7, alpha=0.6)
        ax.set_ylabel(y_labels[i], fontsize=12)
    ax_graphics[-1].set_xlabel("$t$ $(s)$", fontsize=12)
    lines = []
    for ax in ax_graphics:
        line, = ax.plot([], [], lw=1.6, color='r')
        lines.append(line)

    ax_de = plt.axes([0.45, 0.19, 0.25, 0.015])
    ax_da = plt.axes([0.45, 0.14, 0.25, 0.015])
    ax_dr = plt.axes([0.45, 0.09, 0.25, 0.015])

    slider_de = Slider(ax_de, '$\u03B4_e$ $(deg)$', -20, 20, valinit=0, valstep=0.1, color=color_elevator)
    slider_da = Slider(ax_da, '$\u03B4_a$ $(deg)$', -20, 20, valinit=0, valstep=0.1, color=color_aileron)
    slider_dr = Slider(ax_dr, '$\u03B4_r$ $(deg)$', -20, 20, valinit=0, valstep=0.1, color=color_rudder)  

    def reset_sliders_de(event):
        slider_de.set_val(0)

    def reset_sliders_da(event):
        slider_da.set_val(0)
    
    def reset_sliders_dr(event):
        slider_dr.set_val(0)

    # Reset slider de
    axreset_de = plt.axes([0.33, 0.185, 0.05, 0.03])
    button_reset_de = Button(axreset_de, 'Reset $\u03B4_e$')
    button_reset_de.on_clicked(reset_sliders_de)

    # Reset slider da
    axreset_da = plt.axes([0.33, 0.135, 0.05, 0.03])
    button_reset_da = Button(axreset_da, 'Reset $\u03B4_a$')
    button_reset_da.on_clicked(reset_sliders_da)

    # Reset slider dr
    axreset_dr = plt.axes([0.33, 0.085, 0.05, 0.03])
    button_reset_dr = Button(axreset_dr, 'Reset $\u03B4_r$')
    button_reset_dr.on_clicked(reset_sliders_dr)

    stop_flag = False
    paused = False
    ax_btn_stop = plt.axes([0.78, 0.195, 0.10, 0.05])
    btn_stop = Button(ax_btn_stop, 'PAUSE', color='orange', hovercolor='red')
    ax_btn_resume = plt.axes([0.78, 0.125, 0.10, 0.05])
    btn_resume = Button(ax_btn_resume, 'RESUME', color='lightgreen', hovercolor='green')
    ax_btn_exit = plt.axes([0.78, 0.055, 0.10, 0.05])
    btn_exit = Button(ax_btn_exit, 'EXIT', color='lightcoral', hovercolor='darkred')

    def stop_callback(event):
        nonlocal paused
        paused = True
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Simulation paused.")
        logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Simulation paused.")

    def resume_callback(event):
        nonlocal paused
        paused = False
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Simulation resumed.")
        logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Simulation resumed.")

    def exit_callback(event):
        nonlocal stop_flag
        stop_flag = True
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Exit command received. Closing simulation.")
        logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Exit command received. Closing simulation.")

    btn_stop.on_clicked(stop_callback)
    btn_resume.on_clicked(resume_callback)
    btn_exit.on_clicked(exit_callback)

    sim_dt = 0.05
    t = 0
    t_vals = []
    theta_vals, phi_vals, psi_vals = [], [], []

    def rotation_matrix(phi, theta, psi):
        Rz = np.array([[np.cos(psi), np.sin(psi), 0],
                       [-np.sin(psi), np.cos(psi), 0],
                       [0, 0, 1]])
        Ry = np.array([[np.cos(theta), 0, -np.sin(theta)],
                       [0, 1, 0],
                       [np.sin(theta), 0, np.cos(theta)]])
        Rx = np.array([[1, 0, 0],
                       [0, np.cos(phi), np.sin(phi)],
                       [0, -np.sin(phi), np.cos(phi)]])
        return Rx @ Ry @ Rz

    # Inizializzazione disegno
    R = rotation_matrix(state_lat[3], state_lon[3], state_lat[4])
    wing_center_poly, left_fixed_poly, right_fixed_poly, tail_h_poly, tail_v_poly, left_aileron_poly, right_aileron_poly, elevator_poly, rudder_poly = draw_airplane(ax_3d, R)

    while plt.fignum_exists(fig.number) and not stop_flag:
        if not paused:
            de = math.radians(slider_de.val)
            da = math.radians(slider_da.val)
            dr = math.radians(slider_dr.val)
            throttle = 0
            state_lon = rk4_step(model_LON, state_lon, sim_dt, de, throttle)
            state_lat = rk4_step(model_LAT, state_lat, sim_dt, da, dr)
            t += sim_dt
            t_vals.append(t)
            theta_vals.append(math.degrees(state_lon[3]))
            phi_vals.append(math.degrees(state_lat[3]))
            psi_vals.append(math.degrees(state_lat[4]))

        for line, vals, ax in zip(lines, [theta_vals, phi_vals, psi_vals], ax_graphics):
            line.set_data(t_vals, vals)
            ax.set_xlim(0, max(20, t))
            ax.relim()
            ax.autoscale_view(True, True, True)

        ax_3d.cla()
        ax_3d.set_title("StickTech $RealTime$ Animator", fontsize=14)
        ax_3d.set_xlim(-3, 3)
        ax_3d.set_ylim(-3, 3)
        ax_3d.set_zlim(-1, 2)
        ax_3d.set_xticks([])
        ax_3d.set_yticks([])
        ax_3d.set_zticks([])
        ax_3d.grid(True)

        R = rotation_matrix(state_lat[3], state_lon[3], state_lat[4])
        wing_center_poly, left_fixed_poly, right_fixed_poly, tail_h_poly, tail_v_poly, left_aileron_poly, right_aileron_poly, elevator_poly, rudder_poly = draw_airplane(ax_3d, R)

        # **Modifica colori superfici in base agli slider**
        left_aileron_poly.set_color("red" if slider_da.val != 0 else color_aileron)       # alettone sinistro
        right_aileron_poly.set_color("red" if slider_da.val != 0 else color_aileron)       # alettone destro
        elevator_poly.set_color("red" if slider_de.val != 0 else color_elevator)     # equilibratore
        rudder_poly.set_color("red" if slider_dr.val != 0 else color_rudder)     # timone

        plt.pause(sim_dt)

    if stop_flag:
        plt.close(fig)

    if not stop_flag:
        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Simulation stopped. Waiting for window to close.")
        logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Simulation stopped. Waiting for window to close.")
        plt.show()

    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    RT is closed.")
    logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    RT is closed.")