def place_inputs(gui_list_trim_load, GUI_outputs_1, GUI_outputs_2):

    import tkinter as tk

    e1 = GUI_outputs_1[0]
    e2 = GUI_outputs_1[1]
    e3 = GUI_outputs_1[2]
    e4 = GUI_outputs_1[3]
    e5 = GUI_outputs_1[4]
    e6 = GUI_outputs_1[5]
    e7 = GUI_outputs_1[6]
    e8 = GUI_outputs_1[7]
    e9 = GUI_outputs_1[8]
    e10 = GUI_outputs_1[9]
    e11 = GUI_outputs_1[10]
    e12 = GUI_outputs_1[11]
    e16 = GUI_outputs_1[12]
    e17 = GUI_outputs_1[13]
    e18 = GUI_outputs_1[14]
    e19 = GUI_outputs_1[15]
    e20 = GUI_outputs_1[16]
    e21 = GUI_outputs_1[17]
    e22 = GUI_outputs_1[18]
    e23 = GUI_outputs_1[19]
    e24 = GUI_outputs_1[20]
    e25 = GUI_outputs_1[21]
    e26 = GUI_outputs_1[22]
    e27 = GUI_outputs_1[23]
    e30 = GUI_outputs_1[24]
    e34 = GUI_outputs_1[25]
    e38 = GUI_outputs_1[26]
    e31 = GUI_outputs_1[27]
    e35 = GUI_outputs_1[28]
    e39 = GUI_outputs_1[29]
    e32 = GUI_outputs_1[30]
    e36 = GUI_outputs_1[31]
    e40 = GUI_outputs_1[32]
    e28 = GUI_outputs_1[33]

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
    e53 = GUI_outputs_2[10]
    e54 = GUI_outputs_2[11]

    e1.delete(0, tk.END)
    e1.insert(0, gui_list_trim_load[0])

    e2.delete(0, tk.END)
    e2.insert(0, gui_list_trim_load[2])

    e3.delete(0, tk.END)
    e3.insert(0, gui_list_trim_load[7])

    e4.delete(0, tk.END)
    e4.insert(0, gui_list_trim_load[1])

    e5.delete(0, tk.END)
    e5.insert(0, gui_list_trim_load[3])

    e6.delete(0, tk.END)
    e6.insert(0, gui_list_trim_load[8])

    # e7 (Zq) is not used

    e8.delete(0, tk.END)
    e8.insert(0, gui_list_trim_load[9])

    e9.delete(0, tk.END)
    e9.insert(0, gui_list_trim_load[10])

    # e10 (Xde) is not used

    e11.delete(0, tk.END)
    e11.insert(0, gui_list_trim_load[4])

    e12.delete(0, tk.END)
    e12.insert(0, gui_list_trim_load[11])

    e16.delete(0, tk.END)
    e16.insert(0, gui_list_trim_load[12])

    e17.delete(0, tk.END)
    e17.insert(0, gui_list_trim_load[13])

    e18.delete(0, tk.END)
    e18.insert(0, gui_list_trim_load[15])

    e19.delete(0, tk.END)
    e19.insert(0, gui_list_trim_load[16])

    e20.delete(0, tk.END)
    e20.insert(0, gui_list_trim_load[17])

    e21.delete(0, tk.END)
    e21.insert(0, gui_list_trim_load[18])

    e22.delete(0, tk.END)
    e22.insert(0, gui_list_trim_load[20])

    e23.delete(0, tk.END)
    e23.insert(0, gui_list_trim_load[21])

    e24.delete(0, tk.END)
    e24.insert(0, gui_list_trim_load[22])

    e25.delete(0, tk.END)
    e25.insert(0, gui_list_trim_load[23])

    e26.delete(0, tk.END)
    e26.insert(0, gui_list_trim_load[24])

    e27.delete(0, tk.END)
    e27.insert(0, gui_list_trim_load[25])

    e30.delete(0, tk.END)
    e30.insert(0, gui_list_trim_load[28])

    e34.delete(0, tk.END)
    e34.insert(0, gui_list_trim_load[31])

    e38.delete(0, tk.END)
    e38.insert(0, gui_list_trim_load[34])

    e31.delete(0, tk.END)
    e31.insert(0, gui_list_trim_load[26])

    e35.delete(0, tk.END)
    e35.insert(0, gui_list_trim_load[29])

    e39.delete(0, tk.END)
    e39.insert(0, gui_list_trim_load[32])

    e32.delete(0, tk.END)
    e32.insert(0, gui_list_trim_load[27])

    e36.delete(0, tk.END)
    e36.insert(0, gui_list_trim_load[30])

    e40.delete(0, tk.END)
    e40.insert(0, gui_list_trim_load[33])

    # gui_list_trim_save = [Xu, Xw, Zu, Zw, Zde, de, U0, Mu, Mw, Mw_dot, Mq, Mde, Yv, Ydr_star, dr, Lb_apice (15), 
    #                     Lp_apice, Lr_apice, Lda_apice, da, Ldr_apice, Nb_apice, Np_apice, Nr_apice (23), 
    #                     Nda_apice, Ndr_apice, t_e, tau_e, de_deg, t_r, tau_r, dr_deg, t_a, tau_a, da_deg (34)]

    print("\nInputs correctly loaded.")