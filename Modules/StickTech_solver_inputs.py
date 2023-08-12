def inputs(GUI_outputs_1):

    import math

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

    g   = 9.81                  # m/s^2
    H   = 20000/3.281           # m
    M   = 0.65
    U0  = float(e28.get())      # m/s
    W   = 636636 * 0.453        # kg
    Ix  = 0.182*10**8 * 1.356   # kg*m^2
    Iy  = 0.331*10**8 * 1.356   # kg*m^2
    Iz  = 0.497*10**8 * 1.356   # kg*m^2
    Ixz = 970056 * 1.356        # kg*m^2

    # Derivate aerodinamiche

    Xu          = float(e1.get())
    Zu          = float(e2.get())
    Mu          = float(e3.get())
    Xw          = float(e4.get())
    Zw          = float(e5.get())
    Mw          = float(e6.get())
    # Zw_dot      = 0.0156
    # Zq          = float(e7.get())
    Mw_dot      = float(e8.get())
    Mq          = float(e9.get())
    # Xde         = float(e10.get())
    Zde         = float(e11.get())
    Mde         = float(e12.get())
    # Xdt         = 0.505*10**(-4)
    # Zdt         = -0.220*10**(-5)
    # Mdt         = 0.302*10**(-6)

    Yv          = float(e16.get())
    Ydr_star    = float(e17.get())
    # Yda_star    = 0
    Lb_apice    = float(e18.get())
    Lp_apice    = float(e19.get())
    Lr_apice    = float(e20.get())
    Lda_apice   = float(e21.get())
    Ldr_apice   = float(e22.get())
    Nb_apice    = float(e23.get())
    Np_apice    = float(e24.get())
    Nr_apice    = float(e25.get())
    Nda_apice   = float(e26.get())
    Ndr_apice   = float(e27.get())

    # ----------------------------- Input Comandi --------------------------------

    # Ampiezza
    de_deg = float(e30.get())       # equilibratore (deg)
    dr_deg = float(e34.get())       # timone (deg)
    da_deg = float(e38.get())       # alettone (deg)

    t_e = float(e31.get())          # Istante in cui arriva il comando di equilibratore (s)
    t_r = float(e35.get())          # Istante in cui arriva il comando di timone (s)
    t_a = float(e39.get())          # Istante in cui arriva il comando di alettone (s)

    tau_e = float(e32.get())        # Durata del comando di equilibratore (s)
    tau_r = float(e36.get())        # Durata del comando di timone (s)
    tau_a = float(e40.get())        # Durata del comando di alettone (s)

    # ----------------------------------------------------------------------------

    # deg to rad
    de = math.radians(de_deg) # rad
    dr = math.radians(dr_deg) # rad
    da = math.radians(da_deg) # rad

    # Comando di equilibratore (gradino finito)
    equilibratore = lambda x: 1 if x == t_e else 0 if x < t_e else 0 if x > t_e+tau_e else 1

    # Comando di timone (gradino finito)
    timone = lambda x: 1 if x == t_r else 0 if x < t_r else 0 if x > t_r+tau_r else 1

    # Comando di alettone (gradino finito)
    alettone = lambda x: 1 if x == t_a else 0 if x < t_a else 0 if x > t_a+tau_a else 1

    inputs_list = [Xu, Xw, g, Zu, Zw, Zde, de, U0, Mu, Mw, Mw_dot, Mq, Mde, equilibratore, 
        Yv, Ydr_star, dr, Lb_apice, Lp_apice, Lr_apice, Lda_apice, da, Ldr_apice,
        Nb_apice, Np_apice, Nr_apice, Nda_apice, Ndr_apice, alettone, timone, t_e, tau_e, 
        de_deg, t_r, tau_r, dr_deg, t_a, tau_a, da_deg]
    
    plots_inputs_list = [t_e, tau_e, de_deg, t_r, tau_r, dr_deg, t_a, tau_a, da_deg]

    return inputs_list, plots_inputs_list