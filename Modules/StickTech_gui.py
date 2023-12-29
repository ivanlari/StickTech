def LADS_GUI(code_name, code_build, root):

    from tkinter import Label, Entry, StringVar, OptionMenu, Checkbutton, IntVar
    from ttkbootstrap import Label as lb, Menubutton

    # back_color = "#ADD8E6"
    root.title(code_name + " " + code_build)
    root.geometry('1280x870')
    #root['background'] = back_color

    entry_size = 8
    entry_label_size = 10
    sub_title_label_size = 12
    title_label_size = 14
    
    Titolo1 = lb(root, text="   Aircraft:    ", bootstyle='danger', font=("Arial", title_label_size, 'bold'))
    Titolo1.grid(row=0, column=0)
    # Titolo1 = Label(root, text="AIRCRAFT", font=("Arial", 15), fg="red")
    # #Titolo1.config(bg=back_color)
    # Titolo1.grid(row=0, column=1)

    Titolo2 = lb(root, text="LONGITUDINAL", bootstyle='primary', font=("Arial", sub_title_label_size, 'bold'))
    #Titolo2.config(bg=back_color)
    Titolo2.grid(row=1, column=1)
    Titolo3 = lb(root, text="DERIVATIVES", bootstyle='primary', font=("Arial", sub_title_label_size, 'bold'))
    #Titolo3.config(bg=back_color)
    Titolo3.grid(row=1, column=2)

    Titolo4 = lb(root, text="                          LATERAL", bootstyle='primary', font=("Arial", sub_title_label_size, 'bold'))
    #Titolo4.config(bg=back_color)
    Titolo4.grid(row=1, column=3)
    Titolo5 = lb(root, text="DERIVATIVES", bootstyle='primary', font=("Arial", sub_title_label_size, 'bold'))
    #Titolo5.config(bg=back_color)
    Titolo5.grid(row=1, column=4)

    # space1 = Label(root, text=" ")
    # space1.config(bg=back_color)
    # space1.grid(row=1, column=1)

    testo1 = Label(root, text="Xu [1/s]: ", font=("Arial", entry_label_size, 'italic'))
    testo1.grid(row=2, column=1)
    #testo1.config(bg=back_color)
    e1 = Entry(root, borderwidth=1, font=("Arial", entry_size))
    e1.grid(row=2, column=2)
    e1.insert(0, -0.013)

    testo2 = Label(root, text="Zu [1/s]: ", font=("Arial", entry_label_size, 'italic'))
    testo2.grid(row=3, column=1)
    #testo2.config(bg=back_color)
    e2 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e2.grid(row=3, column=2)
    e2.insert(0, -0.1)

    testo3 = Label(root, text="Mu [1/(m*s)]: ", font=("Arial", entry_label_size, 'italic'))
    testo3.grid(row=4, column=1)
    #testo3.config(bg=back_color)
    e3 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e3.grid(row=4, column=2)
    e3.insert(0, -0.0001)

    testo4 = Label(root, text="Xw [1/s]: ", font=("Arial", entry_label_size, 'italic'))
    testo4.grid(row=5, column=1)
    #testo4.config(bg=back_color)
    e4 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e4.grid(row=5, column=2)
    e4.insert(0, 0.0482)

    testo5 = Label(root, text="Zw [1/s]: ", font=("Arial", entry_label_size, 'italic'))
    testo5.grid(row=6, column=1)
    #testo5.config(bg=back_color)
    e5 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e5.grid(row=6, column=2)
    e5.insert(0, -0.539)

    testo6 = Label(root, text="Mw [1/(m*s)]: ", font=("Arial", entry_label_size, 'italic'))
    testo6.grid(row=7, column=1)
    #testo6.config(bg=back_color)
    e6 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e6.grid(row=7, column=2)
    e6.insert(0, -0.0019)

    # testo7 = Label(root, text="ZwD [ ]: ", font=("Arial", 12))
    # testo7.grid(row=8, column=1)
    # testo7.config(bg=back_color)
    # e7 = Entry(root, borderwidth=2)
    # e7.grid(row=8, column=2)
    # e7.insert(0, 0.0156)

    testo7 = Label(root, text="Zq [m/(rad*s)]: ", font=("Arial", entry_label_size, 'italic'))
    #testo7.grid(row=8, column=1)
    #testo7.config(bg=back_color)
    e7 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    #e7.grid(row=8, column=2)
    #e7.insert(0, -8.09)

    testo8 = Label(root, text="MwD [1/m]: ", font=("Arial", entry_label_size, 'italic'))
    testo8.grid(row=8, column=1)
    #testo8.config(bg=back_color)
    e8 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e8.grid(row=8, column=2)
    e8.insert(0, -0.000155)

    testo9 = Label(root, text="Mq [1/s]: ", font=("Arial", entry_label_size, 'italic'))
    testo9.grid(row=9, column=1)
    #testo9.config(bg=back_color)
    e9 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e9.grid(row=9, column=2)
    e9.insert(0, -0.535)

    testo10 = Label(root, text="Xde [m/(rad*s^2)]: ", font=("Arial", entry_label_size, 'italic'))
    #testo10.grid(row=11, column=1)
    #testo10.config(bg=back_color)
    e10 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    #e10.grid(row=11, column=2)
    #e10.insert(0, 1.15)

    testo11 = Label(root, text="Zde [m/(rad*s^2)]: ", font=("Arial", entry_label_size, 'italic'))
    testo11.grid(row=10, column=1)
    #testo11.config(bg=back_color)
    e11 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e11.grid(row=10, column=2)
    e11.insert(0, -26.4)

    testo12 = Label(root, text="Mde [1/(rad*s^2)]: ", font=("Arial", entry_label_size, 'italic'))
    testo12.grid(row=11, column=1)
    #testo12.config(bg=back_color)
    e12 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e12.grid(row=11, column=2)
    e12.insert(0, -1.69)

    # PREDISPOSIZIONE SPINTA
    testoT1 = Label(root, text="Xdt [m/(kg*s^2)]: ", font=("Arial", entry_label_size, 'italic'))
    #testoT1.grid(row=12, column=1)
    eT1 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    #eT1.grid(row=12, column=2)
    eT1.insert(0, 0.000033936)

    testoT2 = Label(root, text="Zdt [m/(kg*s^2)]: ", font=("Arial", entry_label_size, 'italic'))
    #testoT2.grid(row=13, column=1)
    eT2 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    #eT2.grid(row=13, column=2)
    eT2.insert(0, -0.0000014784)

    testoT3 = Label(root, text="Mdt [1/(kg*s^2)]: ", font=("Arial", entry_label_size, 'italic'))
    #testoT3.grid(row=14, column=1)
    eT3 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    #eT3.grid(row=14, column=2)
    eT3.insert(0, 0.000000202944)

    testo16 = Label(root, text="            Yv [1/s]:       ", font=("Arial", entry_label_size, 'italic'))
    testo16.grid(row=2, column=3)
    #testo16.config(bg=back_color)
    e16 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e16.grid(row=2, column=4)
    e16.insert(0, -0.104)

    testo17 = Label(root, text="            Ydr* [1/(rad*s)]:       ", font=("Arial", entry_label_size, 'italic'))
    testo17.grid(row=3, column=3)
    #testo17.config(bg=back_color)
    e17 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e17.grid(row=3, column=4)
    e17.insert(0, 0.0142)

    testo18 = Label(root, text="            Lb' [1/s^2]:       ", font=("Arial", entry_label_size, 'italic'))
    testo18.grid(row=4, column=3)
    #testo18.config(bg=back_color)
    e18 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e18.grid(row=4, column=4)
    e18.insert(0, -2.96)

    testo19 = Label(root, text="            Lp' [1/s]:       ", font=("Arial", entry_label_size, 'italic'))
    testo19.grid(row=5, column=3)
    #testo19.config(bg=back_color)
    e19 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e19.grid(row=5, column=4)
    e19.insert(0, -0.804)

    testo20 = Label(root, text="            Lr' [1/s]:       ", font=("Arial", entry_label_size, 'italic'))
    testo20.grid(row=6, column=3)
    #testo20.config(bg=back_color)
    e20 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e20.grid(row=6, column=4)
    e20.insert(0, 0.317)

    testo21 = Label(root, text="            Lda' [1/(rad*s^2)]:       ", font=("Arial", entry_label_size, 'italic'))
    testo21.grid(row=7, column=3)
    #testo21.config(bg=back_color)
    e21 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e21.grid(row=7, column=4)
    e21.insert(0, 0.210)

    testo22 = Label(root, text="            Ldr' [1/(rad*s^2)]:       ", font=("Arial", entry_label_size, 'italic'))
    testo22.grid(row=8, column=3)
    #testo22.config(bg=back_color)
    e22 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e22.grid(row=8, column=4)
    e22.insert(0, 0.211)

    testo23 = Label(root, text="            Nb' [1/s^2]:       ", font=("Arial", entry_label_size, 'italic'))
    testo23.grid(row=9, column=3)
    #testo23.config(bg=back_color)
    e23 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e23.grid(row=9, column=4)
    e23.insert(0, 0.923)

    testo24 = Label(root, text="            Np' [1/s]:       ", font=("Arial", entry_label_size, 'italic'))
    testo24.grid(row=10, column=3)
    #testo24.config(bg=back_color)
    e24 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e24.grid(row=10, column=4)
    e24.insert(0, -0.0531)

    testo25 = Label(root, text="            Nr' [1/s]:       ", font=("Arial", entry_label_size, 'italic'))
    testo25.grid(row=11, column=3)
    #testo25.config(bg=back_color)
    e25 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e25.grid(row=11, column=4)
    e25.insert(0, -0.193)

    testo26 = Label(root, text="            Nda' [1/(rad*s^2)]:       ", font=("Arial", entry_label_size, 'italic'))
    testo26.grid(row=12, column=3)
    #testo26.config(bg=back_color)
    e26 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e26.grid(row=12, column=4)
    e26.insert(0, 0.0199)

    testo27 = Label(root, text="            Ndr' [1/(rad*s^2)]:       ", font=("Arial", entry_label_size, 'italic'))
    testo27.grid(row=13, column=3)
    #testo27.config(bg=back_color)
    e27 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e27.grid(row=13, column=4)
    e27.insert(0, -0.616)

    space2 = lb(root, text="    Settings:    ", bootstyle='danger', font=("Arial", title_label_size, 'bold'))
    #space2.config(bg=back_color)
    space2.grid(row=14, column=0)

    # space3 = Label(root, text=" ")
    # #space3.config(bg=back_color)
    # space3.grid(row=15, column=1)

    testo28 = Label(root, text="Velocity (m/s): ", font=("Arial", entry_label_size))
    testo28.grid(row=16, column=1)
    #testo28.config(bg=back_color)
    e28 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e28.grid(row=16, column=2)
    e28.insert(0, 205.4)

    space4 = lb(root, text="\n  Inputs:   ", bootstyle='danger', font=("Arial", title_label_size, 'bold'))
    #space4.config(bg=back_color)
    space4.grid(row=17, column=0)

    testo29 = lb(root, text="ELEVATOR", bootstyle='primary', font=("Arial", sub_title_label_size, 'bold'))
    testo29.grid(row=18, column=1)
    #testo29.config(bg=back_color)

    testo30 = Label(root, text="Angle (deg): ", font=("Arial", entry_label_size))
    testo30.grid(row=19, column=1)
    #testo30.config(bg=back_color)
    e30 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e30.grid(row=19, column=2)
    e30.insert(0, -2.0)

    testo31 = Label(root, text="Time (s): ", font=("Arial", entry_label_size))
    testo31.grid(row=20, column=1)
    #testo31.config(bg=back_color)
    e31 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e31.grid(row=20, column=2)
    e31.insert(0, 2.0)

    testo32 = Label(root, text="Duration (s): ", font=("Arial", entry_label_size))
    testo32.grid(row=21, column=1)
    #testo32.config(bg=back_color)
    e32 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e32.grid(row=21, column=2)
    e32.insert(0, 2.0)

    testo33 = lb(root, text="                 RUDDER       ", bootstyle='primary', font=("Arial", sub_title_label_size, 'bold'))
    testo33.grid(row=18, column=3)
    #testo33.config(bg=back_color)

    testo34 = Label(root, text="                 Angle (deg):       ", font=("Arial", entry_label_size))
    testo34.grid(row=19, column=3) 
    #testo34.config(bg=back_color)
    e34 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e34.grid(row=19, column=4)
    e34.insert(0, -1.0)

    testo35 = Label(root, text="                 Time (s):       ", font=("Arial", entry_label_size))
    testo35.grid(row=20, column=3) 
    #testo35.config(bg=back_color)
    e35 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e35.grid(row=20, column=4)
    e35.insert(0, 2.0)

    testo36 = Label(root, text="                 Duration (s):       ", font=("Arial", entry_label_size))
    testo36.grid(row=21, column=3) 
    #testo36.config(bg=back_color)
    e36 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e36.grid(row=21, column=4)
    e36.insert(0, 3.0)

    testo37 = lb(root, text="                 AILERON       ", bootstyle='primary', font=("Arial", sub_title_label_size, 'bold'))
    testo37.grid(row=18, column=5)
    #testo37.config(bg=back_color)

    testo38 = Label(root, text="                 Angle (deg):       ", font=("Arial", entry_label_size))
    testo38.grid(row=19, column=5) 
    #testo38.config(bg=back_color)
    e38 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e38.grid(row=19, column=6)
    e38.insert(0, 3.0)

    testo39 = Label(root, text="                 Time (s):       ", font=("Arial", entry_label_size))
    testo39.grid(row=20, column=5) 
    #testo39.config(bg=back_color)
    e39 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e39.grid(row=20, column=6)
    e39.insert(0, 6.0)

    testo40 = Label(root, text="                 Duration (s):       ", font=("Arial", entry_label_size))
    testo40.grid(row=21, column=5) 
    #testo40.config(bg=back_color)
    e40 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e40.grid(row=21, column=6)
    e40.insert(0, 2.0)

    space5 = lb(root, text="\n  Analysis:   ", bootstyle='danger', font=("Arial", title_label_size, 'bold'))
    #space5.config(bg=back_color)
    space5.grid(row=22, column=0)

    # space6 = Label(root, text=" ")
    # #space6.config(bg=back_color)
    # space6.grid(row=23, column=1)

    testo41 = lb(root, text="                          INITIAL", bootstyle='success', font=("Arial", sub_title_label_size, 'bold'))
    testo41.grid(row=1, column=5) 
    #testo41.config(bg=back_color)
    testo42 = lb(root, text="CONDITIONS       ", bootstyle='success', font=("Arial", sub_title_label_size, 'bold'))
    testo42.grid(row=1, column=6) 
    #testo42.config(bg=back_color)

    testo43 = Label(root, text="                 u0 (m/s):       ", font=("Arial", entry_label_size))
    testo43.grid(row=2, column=5) 
    #testo43.config(bg=back_color)
    e43 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e43.grid(row=2, column=6)
    e43.insert(0, 0.0)

    testo44 = Label(root, text="                 w0 (m/s):       ", font=("Arial", entry_label_size))
    testo44.grid(row=3, column=5) 
    #testo44.config(bg=back_color)
    e44 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e44.grid(row=3, column=6)
    e44.insert(0, 0.0)

    testo45 = Label(root, text="                 q0 (deg/s):       ", font=("Arial", entry_label_size))
    testo45.grid(row=4, column=5) 
    #testo45.config(bg=back_color)
    e45 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e45.grid(row=4, column=6)
    e45.insert(0, 0.0)

    testo46 = Label(root, text="                 Theta0 (deg):       ", font=("Arial", entry_label_size))
    testo46.grid(row=5, column=5) 
    #testo46.config(bg=back_color)
    e46 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e46.grid(row=5, column=6)
    e46.insert(0, 0.0)

    testo47 = Label(root, text="                 h0 (m):       ", font=("Arial", entry_label_size))
    testo47.grid(row=6, column=5) 
    #testo47.config(bg=back_color)
    e47 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e47.grid(row=6, column=6)
    e47.insert(0, 0.0)

    testo48 = Label(root, text="                 Beta0 (deg):       ", font=("Arial", entry_label_size))
    testo48.grid(row=7, column=5) 
    #testo48.config(bg=back_color)
    e48 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e48.grid(row=7, column=6)
    e48.insert(0, 0.0)

    testo49 = Label(root, text="                 p0 (deg/s):       ", font=("Arial", entry_label_size))
    testo49.grid(row=8, column=5) 
    #testo49.config(bg=back_color)
    e49 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e49.grid(row=8, column=6)
    e49.insert(0, 0.0)

    testo50 = Label(root, text="                 r0 (deg/s):       ", font=("Arial", entry_label_size))
    testo50.grid(row=9, column=5) 
    #testo50.config(bg=back_color)
    e50 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e50.grid(row=9, column=6)
    e50.insert(0, 0.0)

    testo51 = Label(root, text="                 Phi0 (deg):       ", font=("Arial", entry_label_size))
    testo51.grid(row=10, column=5) 
    #testo51.config(bg=back_color)
    e51 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e51.grid(row=10, column=6)
    e51.insert(0, 0.0)

    testo52 = Label(root, text="                 Psi0 (deg):       ", font=("Arial", entry_label_size))
    testo52.grid(row=11, column=5) 
    #testo52.config(bg=back_color)
    e52 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e52.grid(row=11, column=6)
    e52.insert(0, 0.0)

    # checkbox
    chk_var = IntVar(value=1)
    # chk = Checkbutton(root, text='Magic', variable=chk_var, onvalue=1, offvalue=0)
    # chk.grid(row=13, column=6)

    testo53 = Label(root, text="                     Tmax (s): ", font=("Arial", entry_label_size))
    testo53.grid(row=16, column=3)
    #testo53.config(bg=back_color)
    e53 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e53.grid(row=16, column=4)
    e53.insert(0, 30.0)

    testo54 = Label(root, text="                     DeltaT (s): ", font=("Arial", entry_label_size))
    testo54.grid(row=16, column=5)
    #testo54.config(bg=back_color)
    e54 = Entry(root, borderwidth=2, font=("Arial", entry_size))
    e54.grid(row=16, column=6)
    e54.insert(0, 0.1)

    # Option Menu 1
    variable_option_menu = StringVar(root)
    variable_option_menu.set("Select a TF") # default value
    option_menu = OptionMenu(root, variable_option_menu, "theta/de", "q/de", "w/de", "alpha/de", "gamma/de", 
                             "u/de", "phi/da", "beta/da", "beta/dr", "r/dr", "p/da", "psi/dr")
    option_menu.config(width=12, height=1)
    option_menu.grid(row=53, column=3)

    # Option Menu 2
    variable_option_menu_2 = StringVar(root)
    variable_option_menu_2.set("Select a Result") # default value
    option_menu_2 = OptionMenu(root, variable_option_menu_2, "Longitudinal \nDynamics", "Lateral \nDynamics", 
                               "Poles \nPlacement")
    option_menu_2.config(width=12, height=2)
    option_menu_2.grid(row=54, column=1)

    # Option Menu 3
    variable_option_menu_3 = StringVar(root)
    variable_option_menu_3.set("Select a Plot") # default value
    option_menu_3 = OptionMenu(root, variable_option_menu_3, "Bode Plot", "Root Locus", "Nyquist Plot")
    option_menu_3.config(width=12, height=1)
    option_menu_3.grid(row=54, column=4)

    # space7 = Label(root, text=" ")
    # space7.config(bg=back_color)
    # space7.grid(row=52, column=3)

    testo55 = Label(root, text="Open Loop Analysis", font=("Arial", 10))
    testo55.grid(row=52, column=1)
    #testo55.config(bg=back_color)

    testo56 = Label(root, text="Closed Loop Analysis", font=("Arial", 10))
    testo56.grid(row=52, column=5)
    #testo56.config(bg=back_color)

    testo57 = Label(root, text="Transfer Function Analysis", font=("Arial", 10))
    testo57.grid(row=52, column=3)
    #testo57.config(bg=back_color)

    # Define Outputs
    GUI_outputs_1 = [e1, e2, 
        e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e16, e17, e18, e19, e20, e21, e22, e23, 
        e24, e25, e26, e27, e30, e34, e38, e31, e35, e39, e32, e36, e40, e28, eT1, eT2, eT3]
    
    GUI_outputs_2 = [e43, e44, e45, e46, e47, e48, e49, e50, e51, e52, e53, e54]

    return GUI_outputs_1, GUI_outputs_2, variable_option_menu, variable_option_menu_2, variable_option_menu_3, chk_var