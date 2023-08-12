def print_tf(tf_outputs, selected_tf):
    
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

    # TF printer
    if selected_tf == "Select a TF":
        print("\nSelect a Transfer Function to be printed.")
    elif selected_tf == "theta/de":
        print("\nSelected Transfer Function: {}".format(selected_tf))
        print(theta_de)
    elif selected_tf == "q/de":
        print("\nSelected Transfer Function: {}".format(selected_tf))
        print(q_de)
    elif selected_tf == "w/de":
        print("\nSelected Transfer Function: {}".format(selected_tf))
        print(w_de)
    elif selected_tf == "alpha/de":
        print("\nSelected Transfer Function: {}".format(selected_tf))
        print(alpha_de)
    elif selected_tf == "gamma/de":
        print("\nSelected Transfer Function: {}".format(selected_tf))
        print(gamma_de)
    elif selected_tf == "u/de":
        print("\nSelected Transfer Function: {}".format(selected_tf))
        print(u_de)
    elif selected_tf == "phi/da":
        print("\nSelected Transfer Function: {}".format(selected_tf))
        print(phi_da)
    elif selected_tf == "beta/da":
        print("\nSelected Transfer Function: {}".format(selected_tf))
        print(beta_da)
    elif selected_tf == "beta/dr":
        print("\nSelected Transfer Function: {}".format(selected_tf))
        print(beta_dr)
    elif selected_tf == "r/dr":
        print("\nSelected Transfer Function: {}".format(selected_tf))
        print(r_dr)
    elif selected_tf == "p/da":
        print("\nSelected Transfer Function: {}".format(selected_tf))
        print(p_da)
    elif selected_tf == "psi/dr":
        print("\nSelected Transfer Function: {}".format(selected_tf))
        print(psi_dr)
    else:
        pass
