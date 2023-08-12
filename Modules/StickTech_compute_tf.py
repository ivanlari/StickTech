def compute_tf(inputs_list):

    import control
    import math

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

    M_alpha = U0*Mw
    M_alpha_dot = U0*Mw_dot
    Xalpha = Xw*U0
    Zalpha = Zw*U0

    s = control.TransferFunction.s # Laplace variable

    # Longitudinal

    w_SP = math.sqrt(-M_alpha+Zw*Mq) # short period frequency
    z_SP = -1/(2*w_SP)*(Zw+Mq+M_alpha_dot) # short period damping
    w_LP = math.sqrt(-g/U0*Zu) # long period frequency
    z_LP = -1/(2*w_LP)*Xu # long period damping

    # Longitudinal TFs denominator
    Delta_Longitudinal = (s**2+2*z_LP*w_LP*s+w_LP**2)*(s**2+2*z_SP*w_SP*s+w_SP**2)

    # theta/de
    z1_theta_de = -Xu*(1-Xw*Zu/(Zw*Xu)) # 1/T_theta_1
    z2_theta_de = -Zw # 1/T_theta_2

    theta_de_num = -Mde*(s+z1_theta_de)*(s+z2_theta_de)
    theta_de_den = Delta_Longitudinal
    theta_de = theta_de_num/theta_de_den

    # q/de
    q_de_num = theta_de_num*s
    q_de_den = Delta_Longitudinal
    q_de = q_de_num/q_de_den

    # w/de
    z_w_de = -Mq+U0*Mde/Zde # 1/Tw
    w_w = math.sqrt(-g/U0*(Zu-Mu*Zde/Mde))
    z_w = -1/(2*w_w)*Xu

    w_de_num = -Zde*(s+z_w_de)*(s**2+2*z_w*w_w*s+w_w**2)
    w_de_den = Delta_Longitudinal
    w_de = w_de_num/w_de_den

    # alpha/de
    alpha_de_num = w_de_num
    alpha_de_den = U0*w_de_den
    alpha_de = alpha_de_num/alpha_de_den

    # gamma/de
    z_gamma_de_1 = -Xu*(1-Zu/Xu*(Xalpha-g)/Zalpha)
    z_gamma_de_2 = -math.sqrt(z_w_de*z2_theta_de)
    z_gamma_de_3 = math.sqrt(z_w_de*z2_theta_de)

    gamma_de_num = Zde*(s+z_gamma_de_1)*(s+z_gamma_de_2)*(s+z_gamma_de_3)
    gamma_de_den = U0*Delta_Longitudinal
    gamma_de = gamma_de_num/gamma_de_den

    # u/de
    z_u_de = g/(Xalpha-g)*(-z2_theta_de)
    u_de_num = Mde*(Xalpha-g)*(s+z_u_de)
    u_de_den = Delta_Longitudinal
    u_de = u_de_num/u_de_den

    # Lateral

    B = -Lp_apice-Nr_apice-Yv
    C = Nb_apice+Lp_apice*(Nr_apice+Yv)-Np_apice*Lr_apice+Yv*Nr_apice
    D = -Lp_apice*(Nb_apice+Yv*Nr_apice)+Np_apice*(Lb_apice+Yv*Lr_apice)-Lb_apice*g/U0
    E = (Lb_apice*Nr_apice-Nb_apice*Lr_apice)*g/U0
    lambda_R_3 = (B**2+C)/(B+C**2/D)
    w_DR = math.sqrt(Nb_apice+Yv*Nr_apice) # dutch roll frequency
    z_DR = 1/(2*w_DR)*(-(Nr_apice+Yv)-Lp_apice-lambda_R_3) # dutch roll damping
    p_roll = lambda_R_3 # roll pole
    p_spiral = E/D # spiral pole

    # Lateral-Directional TFs denominator
    Delta_Lateral = (s+p_roll)*(s+p_spiral)*(s**2+2*z_DR*w_DR*s+w_DR**2)

    # phi/da
    w_phi = math.sqrt(w_DR**2*(1-Nda_apice*Lb_apice/(Lda_apice*w_DR**2)))
    z_phi = 1/w_phi*(z_DR*w_DR)

    phi_da_num = Lda_apice*(s**2+2*z_phi*w_phi*s+w_phi**2)
    phi_da_den = Delta_Lateral
    phi_da = phi_da_num/phi_da_den

    # p/da
    p_da_num = s*phi_da_num
    p_da_den = phi_da_den
    p_da = p_da_num/p_da_den

    # beta/da
    z_beta_da_1 = g/U0*(-Lr_apice+Lda_apice/Nda_apice*Nr_apice)/(-Lp_apice+Lda_apice/Nda_apice*(Np_apice-g/U0)) # 1/T_beta1
    z_beta_da_2 = -Lp_apice+Lda_apice/Nda_apice*(Np_apice-g/U0) # 1/T_beta2

    beta_da_num = -Nda_apice*(s+z_beta_da_1)*(s+z_beta_da_2)
    beta_da_den = Delta_Lateral
    beta_da = beta_da_num/beta_da_den

    # beta/dr
    z_beta_dr_1 = g/U0*(-Lr_apice+Ldr_apice/Ndr_apice*Nr_apice)/(-Lp_apice+Ldr_apice/Ndr_apice*(Np_apice-g/U0)) # 1/T_beta1
    z_beta_dr_2 = -Lp_apice+Ldr_apice/Ndr_apice*(Np_apice-g/U0) # 1/T_beta2
    z_beta_dr_3 = -Ndr_apice/Ydr_star # 1/T_beta3

    beta_dr_num = Ydr_star*(s+z_beta_dr_1)*(s+z_beta_dr_2)*(s+z_beta_dr_3)
    beta_dr_den = Delta_Lateral
    beta_dr = beta_dr_num/beta_dr_den

    # r/dr
    z_r_dr = -Lp_apice
    w_r = math.sqrt(Lb_apice*g/(Lp_apice*U0))
    z_r = -1/(2*w_r)*(Yv-Ydr_star/Ndr_apice*Nb_apice-Lb_apice*g/(U0*Lp_apice**2))

    r_dr_num = Ndr_apice*(s+z_r_dr)*(s**2+2*z_r*w_r*s+w_r**2)
    r_dr_den = Delta_Lateral
    r_dr = -r_dr_num/r_dr_den # sign '-' to account for the dr sign

    # psi/dr
    psi_dr_num = r_dr_num
    psi_dr_den = s*r_dr_den
    psi_dr = -psi_dr_num/psi_dr_den # sign '-' to account for the dr sign

    # Outputs
    tf_outputs = [theta_de, q_de, w_de, alpha_de, gamma_de, u_de, phi_da, beta_da, beta_dr, r_dr, p_da, psi_dr]
    dynamics_outputs = [w_SP, z_SP, w_LP, z_LP, p_roll, p_spiral, w_DR, z_DR]

    return [tf_outputs, dynamics_outputs]