def save_inputs(inputs_list):

    Xu              = inputs_list[0]
    Xw              = inputs_list[1]
    g               = inputs_list[2]
    Zu              = inputs_list[3]
    Zw              = inputs_list[4]
    Zde             = inputs_list[5]
    de              = inputs_list[6]
    U0              = inputs_list[7]
    Mu              = inputs_list[8]
    Mw              = inputs_list[9]
    Mw_dot          = inputs_list[10]
    Mq              = inputs_list[11]
    Mde             = inputs_list[12]
    equilibratore   = inputs_list[13]
    Yv              = inputs_list[14]
    Ydr_star        = inputs_list[15]
    dr              = inputs_list[16]
    Lb_apice        = inputs_list[17]
    Lp_apice        = inputs_list[18]
    Lr_apice        = inputs_list[19]
    Lda_apice       = inputs_list[20]
    da              = inputs_list[21]
    Ldr_apice       = inputs_list[22]
    Nb_apice        = inputs_list[23]
    Np_apice        = inputs_list[24]
    Nr_apice        = inputs_list[25]
    Nda_apice       = inputs_list[26]
    Ndr_apice       = inputs_list[27]
    alettone        = inputs_list[28]
    timone          = inputs_list[29]
    t_e             = inputs_list[30]
    tau_e           = inputs_list[31]
    de_deg          = inputs_list[32]
    t_r             = inputs_list[33]
    tau_r           = inputs_list[34]
    dr_deg          = inputs_list[35]
    t_a             = inputs_list[36]
    tau_a           = inputs_list[37]
    da_deg          = inputs_list[38]

    gui_list_trim_save = [Xu, Xw, Zu, Zw, Zde, de, U0, Mu, Mw, Mw_dot, Mq, Mde, Yv, Ydr_star, dr, Lb_apice, 
                        Lp_apice, Lr_apice, Lda_apice, da, Ldr_apice, Nb_apice, Np_apice, Nr_apice, 
                        Nda_apice, Ndr_apice, t_e, tau_e, de_deg, t_r, tau_r, dr_deg, t_a, tau_a, da_deg]

    with open(r'GUI_Inputs.txt', 'w') as gui_inputs_file:
            for i in range(len(gui_list_trim_save)):
                gui_inputs_file.write(str(gui_list_trim_save[i]) + "\n")

    print("\nInputs correctly saved.")