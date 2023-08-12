def solver_model(inputs_list, GUI_outputs_2):

    import math
    import numpy as np
    from scipy.integrate import odeint

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

    def model(X, t):

        # Longitudinal
        u       = X[0]
        w       = X[1]
        q       = X[2]
        theta   = X[3]
        h       = X[4]

        du_dt       = Xu*u + Xw*w - g*theta
        dw_dt       = Zu*u + Zw*w + Zde*de*equilibratore(t) + U0*q
        dq_dt       = Mu*u + Mw*w + Mw_dot*dw_dt + Mq*q + Mde*de*equilibratore(t)
        dtheta_dt   = q
        dh_dt       = U0*theta - w

        # Lateral-Directional
        beta    = X[5]
        p       = X[6]
        r       = X[7]
        phi     = X[8]
        psi     = X[9]

        dbeta_dt    = Yv*beta + g/U0*phi + Ydr_star*dr*timone(t) - r
        dp_dt       = Lb_apice*beta + Lp_apice*p + Lr_apice*r + Lda_apice*da*alettone(t) + Ldr_apice*dr*timone(t)
        dr_dt       = Nb_apice*beta + Np_apice*p + Nr_apice*r + Nda_apice*da*alettone(t) + Ndr_apice*dr*timone(t)
        dphi_dt     = p
        dpsi_dt     = r

        return [du_dt, dw_dt, dq_dt, dtheta_dt, dh_dt, dbeta_dt, dp_dt, dr_dt, dphi_dt, dpsi_dt]

    # Initial conditions
    u0      = float(e43.get())
    w0      = float(e44.get())
    q0      = float(e45.get())
    theta0  = float(e46.get())
    h0      = float(e47.get())
    beta0   = float(e48.get())
    p0      = float(e49.get())
    r0      = float(e50.get())
    phi0    = float(e51.get())
    psi0    = float(e52.get())

    X0 = [u0, w0, q0, theta0, h0, beta0, p0, r0, phi0, psi0] # (deg, deg/s)

    # Deg to Rad
    for i in range(len(X0)):
        X0[i] = math.radians(X0[i])

    # Solve model
    t_max   = float(e53.get())
    Delta_T = float(e54.get())
    t_span  = np.arange(0, t_max, Delta_T)

    X = odeint(model,X0,t_span)

    u       = X[:,0] # velocity u
    w       = X[:,1] # velocity w
    q       = X[:,2] # angular velocity q
    theta   = X[:,3] # angle theta
    h       = X[:,4] # altitude
    beta    = X[:,5] # angle beta
    p       = X[:,6] # angular velocity p
    r       = X[:,7] # angular velocity r
    phi     = X[:,8] # angle phi
    psi     = X[:,9] # angle psi

    alpha   = w/U0 # angle alpha
    gamma   = theta - alpha # angle gamma

    # Rad to Deg
    for i in range(len(beta)):
        q[i]        = math.degrees(q[i])
        theta[i]    = math.degrees(theta[i])
        alpha[i]    = math.degrees(alpha[i])
        gamma[i]    = math.degrees(gamma[i])
        beta[i]     = math.degrees(beta[i])
        p[i]        = math.degrees(p[i])
        r[i]        = math.degrees(r[i])
        phi[i]      = math.degrees(phi[i])
        psi[i]      = math.degrees(psi[i])
    
    solver_outputs = [t_span, q, t_max, theta, alpha, h, gamma, beta, p, r, phi, u, w, psi]

    return solver_outputs