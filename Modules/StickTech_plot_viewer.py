def plot_viewer(selected_plot, selected_tf, tf_outputs):

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

    import control
    import matplotlib.pyplot as plt

    # TF Selector
    if selected_tf == "Select a TF":
        print("\nSelect a Transfer Function before requesting a Plot.")
    elif selected_tf == "theta/de":
        print("\nSelected Transfer Function: {}".format(selected_tf))
        TF = theta_de
    elif selected_tf == "q/de":
        print("\nSelected Transfer Function: {}".format(selected_tf))
        TF = q_de
    elif selected_tf == "w/de":
        print("\nSelected Transfer Function: {}".format(selected_tf))
        TF = w_de
    elif selected_tf == "alpha/de":
        print("\nSelected Transfer Function: {}".format(selected_tf))
        TF = alpha_de
    elif selected_tf == "gamma/de":
        print("\nSelected Transfer Function: {}".format(selected_tf))
        TF = gamma_de
    elif selected_tf == "u/de":
        print("\nSelected Transfer Function: {}".format(selected_tf))
        TF = u_de
    elif selected_tf == "phi/da":
        print("\nSelected Transfer Function: {}".format(selected_tf))
        TF = phi_da
    elif selected_tf == "beta/da":
        print("\nSelected Transfer Function: {}".format(selected_tf))
        TF = beta_da
    elif selected_tf == "beta/dr":
        print("\nSelected Transfer Function: {}".format(selected_tf))
        TF = beta_dr
    elif selected_tf == "r/dr":
        print("\nSelected Transfer Function: {}".format(selected_tf))
        TF = r_dr
    elif selected_tf == "p/da":
        print("\nSelected Transfer Function: {}".format(selected_tf))
        TF = p_da
    elif selected_tf == "psi/dr":
        print("\nSelected Transfer Function: {}".format(selected_tf))
        TF = psi_dr
    else:
        pass

    if selected_tf == "Select a TF":
        pass
    else:
        H = TF
        fig_size = (12,7)
        if selected_plot == "Select a Plot":
            print("\nSelect a Plot to be opened.")
        elif selected_plot == "Bode Plot":
            print("\nOpening Bode Plot.")
            fig_bode = plt.figure("Bode Plot: " + selected_tf, figsize=fig_size)
            control.bode_plot(control.tf(H.num, H.den), dB=True, deg=True)
            plt.show()
            plt.close(fig_bode)
        elif selected_plot == "Root Locus":
            print("\nOpening Root Locus.")
            fig_rl = plt.figure("Root Locus: " + selected_tf, figsize=fig_size)
            control.root_locus(control.tf(H.num, H.den))
            plt.show()
            plt.close(fig_rl)
        elif selected_plot == "Nyquist Plot":
            print("\nOpening Nyquist Plot.")
            fig_nyq = plt.figure("Nyquist Plot: " + selected_tf, figsize=fig_size)
            control.nyquist_plot(control.tf(H.num, H.den))
            plt.show()
            plt.close(fig_nyq)
        else:
            pass