def StepTech(tf_outputs, selected_tf, code_build):
    
    from datetime import datetime
    import numpy as np
    import control
    from scipy.signal import lti
    import matplotlib.pyplot as plt
    from matplotlib.widgets import Slider
    import warnings
    import logging
    warnings.filterwarnings("ignore")

    theta_de    = tf_outputs[0]
    q_de        = tf_outputs[1]
    w_de        = tf_outputs[2]
    alpha_de    = tf_outputs[3]
    gamma_de    = tf_outputs[4]
    u_de        = tf_outputs[5]
    phi_da      = tf_outputs[6]
    beta_da     = tf_outputs[7]
    beta_dr     = tf_outputs[8]
    r_dr        = tf_outputs[9]
    p_da        = tf_outputs[10]
    psi_dr      = tf_outputs[11]

    if selected_tf == "Select a TF":
        print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Select a Transfer Function to be put in Closed Loop.")
        tf_marker = False # a transfer function is not selected
    elif selected_tf == "theta/de":
        print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        G = theta_de
        tf_name = "$\\theta / \delta_e$"
        ref_label = "$\\theta_c$"
        y_label = "$\\theta$"
        tf_marker = True # a transfer function is present and loaded
    elif selected_tf == "q/de":
        print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        G = q_de
        tf_name = "$q / \delta_e$"
        ref_label = "$q_c$"
        y_label = "$q$"
        tf_marker = True
    elif selected_tf == "w/de":
        print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        G = w_de
        tf_name = "$w / \delta_e$"
        ref_label = "$w_c$"
        y_label = "$w$"
        tf_marker = True
    elif selected_tf == "alpha/de":
        print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        G = alpha_de
        tf_name = "$\\alpha / \delta_e$"
        ref_label = "$\\alpha_c$"
        y_label = "$\\alpha$"
        tf_marker = True
    elif selected_tf == "gamma/de":
        print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        G = gamma_de
        tf_name = "$\gamma / \delta_e$"
        ref_label = "$\gamma_c$"
        y_label = "$\gamma$"
        tf_marker = True
    elif selected_tf == "u/de":
        print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        G = u_de
        tf_name = "$u / \delta_e$"
        ref_label = "$u_c$"
        y_label = "$u$"
        tf_marker = True
    elif selected_tf == "phi/da":
        print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        G = phi_da
        tf_name = "$\\varphi / \delta_a$"
        ref_label = "$\\varphi_c$"
        y_label = "$\\varphi$"
        tf_marker = True
    elif selected_tf == "beta/da":
        print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        G = beta_da
        tf_name = "$\\beta / \delta_a$"
        ref_label = "$\\beta_c$"
        y_label = "$\\beta$"
        tf_marker = True
    elif selected_tf == "beta/dr":
        print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        G = beta_dr
        tf_name = "$\\beta / \delta_r$"
        ref_label = "$\\beta_c$"
        y_label = "$\\beta$"
        tf_marker = True
    elif selected_tf == "r/dr":
        print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        G = r_dr
        tf_name = "$r / \delta_r$"
        ref_label = "$r_c$"
        y_label = "$r$"
        tf_marker = True
    elif selected_tf == "p/da":
        print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        G = p_da
        tf_name = "$p / \delta_a$"
        ref_label = "$p_c$"
        y_label = "$p$"
        tf_marker = True
    elif selected_tf == "psi/dr":
        print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        G = psi_dr
        tf_name = "$\psi / \delta_r$"
        ref_label = "$\psi_c$"
        y_label = "$\psi$"
        tf_marker = True
    else:
        tf_marker = False

    # Multiplication between TFs
    def mult(sys1, sys2):
        num = np.polymul(sys1.num, sys2.num)
        den = np.polymul(sys1.den, sys2.den)
        return lti(num, den)

    # Closed-Loop function
    def feedback(sysL): # sys sarebbe L
        num = sysL.num
        den = np.polyadd(sysL.den, sysL.num)
        return lti(num, den)

    # PID initial gains
    kp = 1
    ki = 1
    kd = 1

    # Filter
    N = 1

    # Controller transfer function
    Kpid = lti([kp*kd/N+kp*kd, kp**2+ki*kd/N, kp*ki], [kd/N, kp, 0])

    if tf_marker == True: # Start Tuner
        
        [G_num, G_den] = control.tfdata(G)

        # Operations on list and arrays (to pass from 'control' to 'lti')
        G_num_array_1 = G_num[0]
        G_num_array = G_num_array_1[0]
        G_num_list = G_num_array.tolist()
        G_den_array_1 = G_den[0]
        G_den_array = G_den_array_1[0]
        G_den_list = G_den_array.tolist()

        # convert TF from control package to lti package
        G_lti = lti(G_num_list, G_den_list)

        L = mult(Kpid, G_lti) # Open-Loop function
        T = feedback(L) # Closed-Loop function

        t_in = 0
        t_fin = 10
        t_span = np.linspace(t_in , t_fin, 1000)
        t, y = G_lti.step(T=t_span) # step response in open-loop
        t, y2 = T.step(T=t_span) # step response in closed-loop
        cl_zeros = control.zeros(control.tf(T.num, T.den)) # zeros in closed-loop
        cl_poles = control.poles(control.tf(T.num, T.den)) # poles in closed-loop
        cl_dcgain = control.dcgain(control.tf(T.num, T.den)) # dc gain in closed loop
        (gm, pm, wgc, wpc) = control.margin(control.tf(L.num, L.den)) # stability margins
        gm_dB = 20*np.log10(gm)

        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Starting StepTech Tuner...")
        logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Starting StepTech Tuner...")

        # Plots
        fig = plt.figure("StepTech " + code_build, figsize=(12, 7))
        plt.subplots_adjust(bottom=0.4)
        ax = fig.subplots()
        plt.suptitle("StepTech PID Tuner - Transfer Function: " + tf_name, fontsize=13)
        ax.plot([t_in, t_fin], [1, 1], color='k', ls='--', label="Reference (" + ref_label + ")")
        ax.plot([t_in, t_in], [0, 1], color='k', ls='--')
        ax.plot([t_in-1, t_in], [0, 0], color='k', ls='--')
        ax.plot(t, y, color='b', label="Open Loop")
        cl_plot = ax.plot(t, y2, color='r', label="Closed Loop")[0]
        ax.grid(ls=':', lw=0.8)
        ax.legend(loc="best", fontsize=10)
        plt.xlabel('$t$', fontsize=12)
        plt.ylabel(y_label, fontsize=13, rotation=0)
        plt.title("Step Response", fontsize=12, style='italic')

        for i in range(len(cl_poles)):
            cl_poles[i] = f'{cl_poles[i]:.1f}'
        text_poles = fig.text(0.15, 0.04, 'Closed Loop poles: ' + str(cl_poles), 
                              fontsize = 11, color = "black")

        for i in range(len(cl_zeros)):
            cl_zeros[i] = f'{cl_zeros[i]:.1f}'
        text_zeros = fig.text(0.15, 0.08, 'Closed Loop zeros: ' + str(cl_zeros), 
                              fontsize = 11, color = "black")
        
        text_gm = fig.text(0.65, 0.25, 'Gain Margin (abs): ' + f'{gm:.1f}', fontsize = 11, color = "black")

        text_pm = fig.text(0.65, 0.21, 'Phase Margin (deg): ' + f'{pm:.1f}', fontsize = 11, color = "black")

        text_wpc = fig.text(0.65, 0.17, 'Phase Crossover freq. (rad/s): ' + f'{wpc:.1f}', fontsize = 11, color = "black")

        text_wgc = fig.text(0.65, 0.13, 'Gain Crossover freq. (rad/s): ' + f'{wgc:.1f}', fontsize = 11, color = "black")
        
        plt.xlim((t_in-1, t_fin))
        plt.ylim((0-0.25, 1+0.5))

        fig.text(0.32, 0.30, 'Gains:', style = 'italic', fontsize = 12, color = "black")
        
        fig.text(0.7, 0.30, 'Stability Margins:', style = 'italic', fontsize = 12, color = "black")

        # Sliders
        kp_slider_pos = plt.axes([0.15, 0.27, 0.4, 0.02])
        slider_kp = Slider(kp_slider_pos, '$K_P$', 0.0000000001, 50, valinit=1, valstep=0.00001, color='red')
        slider_kp.label.set_size(14)

        ki_slider_pos = plt.axes([0.15, 0.23, 0.4, 0.02])
        slider_ki = Slider(ki_slider_pos, '$K_I$', 0.0000000001, 50, valinit=1, valstep=0.00001, color='red')
        slider_ki.label.set_size(14)

        kd_slider_pos = plt.axes([0.15, 0.19, 0.4, 0.02])
        slider_kd = Slider(kd_slider_pos, '$K_D$', 0.0000000001, 50, valinit=1, valstep=0.00001, color='red')
        slider_kd.label.set_size(14)

        N_slider_pos = plt.axes([0.15, 0.15, 0.4, 0.02])
        slider_N = Slider(N_slider_pos, '$N$', 0.0000000001, 50, valinit=1, valstep=0.00001, color='red')
        slider_N.label.set_size(14)

        # Update Plot 
        def update(val):
            x = [slider_kp.val, slider_ki.val, slider_kd.val, slider_N.val]
            current_kp = x[0]
            current_ki = x[1]
            current_kd = x[2]
            current_N  = x[3]
            kp = current_kp
            ki = current_ki
            kd = current_kd
            N  = current_N
            Kpid = lti([kp*kd/N+kp*kd, kp**2+ki*kd/N, kp*ki], [kd/N, kp, 0])
            L = mult(Kpid, G_lti)
            T = feedback(L)

            (gm, pm, wgc, wpc) = control.margin(control.tf(L.num, L.den))
            gm_dB = 20*np.log10(gm)
            
            cl_dcgain = control.dcgain(control.tf(T.num, T.den))
            # text_dcgain.set_text('Closed Loop DC gain: ' + f'{cl_dcgain:.1f}')

            cl_poles = control.poles(control.tf(T.num, T.den))
            for i in range(len(cl_poles)):
                cl_poles[i] = f'{cl_poles[i]:.1f}'
            text_poles.set_text('Closed Loop poles: ' + str(cl_poles))

            cl_zeros = control.zeros(control.tf(T.num, T.den))
            for i in range(len(cl_zeros)):
                cl_zeros[i] = f'{cl_zeros[i]:.1f}'
            text_zeros.set_text('Closed Loop zeros: ' + str(cl_zeros))

            text_gm.set_text('Gain Margin (abs): ' + f'{gm:.1f}')
            text_pm.set_text('Phase Margin (deg): ' + f'{pm:.1f}')
            text_wpc.set_text('Phase Crossover freq. (rad/s): ' + f'{wpc:.1f}')
            text_wgc.set_text('Gain Crossover freq. (rad/s): ' + f'{wgc:.1f}')

            t, y2_new = T.step(T=t_span) # risposta al gradino in ciclo chiuso

            cl_plot.set_data(t,y2_new)

            # Redrawing the figure
            fig.canvas.draw()
            return [kp, ki, kd, cl_poles]
        
        slider_kp.on_changed(update)
        slider_ki.on_changed(update)
        slider_kd.on_changed(update)
        slider_N.on_changed(update)
        plt.show()
        print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Tuner is closed.")
        logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Tuner is closed.")
    else:
        pass