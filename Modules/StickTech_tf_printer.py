def print_tf(tf_outputs, selected_tf):
    
    from datetime import datetime
    import control
    import logging

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

    def tf_prop(H):
        # Print TF properties:
        ol_zeros = control.zeros(H)
        ol_poles = control.poles(H)
        for i in range(len(ol_poles)):
            ol_poles[i] = f'{ol_poles[i]:.2f}'
        for i in range(len(ol_zeros)):
            ol_zeros[i] = f'{ol_zeros[i]:.2f}'
        print("DC gain: " + f'{control.dcgain(H):.2f}')
        logging.info("DC gain: " + f'{control.dcgain(H):.2f}')
        print("Zeros: " + str(ol_zeros))
        logging.info("Zeros: " + str(ol_zeros))
        print("Poles: " + str(ol_poles))
        logging.info("Poles: " + str(ol_poles) + "\n")

    # TF printer
    if selected_tf == "Select a TF":
        print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Select a Transfer Function to be printed.")
    elif selected_tf == "theta/de":
        print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        print(theta_de)
        logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        logging.info(theta_de)
        tf_prop(theta_de)
    elif selected_tf == "q/de":
        print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        print(q_de)
        logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        logging.info(q_de)
        tf_prop(q_de)
    elif selected_tf == "w/de":
        print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        print(w_de)
        logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        logging.info(w_de)
        tf_prop(w_de)
    elif selected_tf == "alpha/de":
        print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        print(alpha_de)
        logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        logging.info(alpha_de)
        tf_prop(alpha_de)
    elif selected_tf == "gamma/de":
        print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        print(gamma_de)
        logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        logging.info(gamma_de)
        tf_prop(gamma_de)
    elif selected_tf == "u/de":
        print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        print(u_de)
        logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        logging.info(u_de)
        tf_prop(u_de)
    elif selected_tf == "phi/da":
        print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        print(phi_da)
        logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        logging.info(phi_da)
        tf_prop(phi_da)
    elif selected_tf == "beta/da":
        print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        print(beta_da)
        logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        logging.info(beta_da)
        tf_prop(beta_da)
    elif selected_tf == "beta/dr":
        print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        print(beta_dr)
        logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        logging.info(beta_dr)
        tf_prop(beta_dr)
    elif selected_tf == "r/dr":
        print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        print(r_dr)
        logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        logging.info(r_dr)
        tf_prop(r_dr)
    elif selected_tf == "p/da":
        print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        print(p_da)
        logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        logging.info(p_da)
        tf_prop(p_da)
    elif selected_tf == "psi/dr":
        print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        print(psi_dr)
        logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Transfer Function: {}".format(selected_tf))
        logging.info(psi_dr)
        tf_prop(psi_dr)
    else:
        pass