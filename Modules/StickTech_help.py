def help(root):

    from tkinter import Toplevel, Button, Label
    import logging
    from datetime import datetime
    from ttkbootstrap import Label as lb, Menubutton, Button as bt, Style

    help_Window = Toplevel(root)
    help_Window.geometry("1200x700")
    help_Window.title("StickTech Help")

    title_label_size = 14
    sub_title_label_size = 12
    entry_label_size = 10

    print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Help window is opened.")
    logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Help window is opened.")

    vspace = lb(help_Window, text=" ", bootstyle='danger', font=("Arial", title_label_size))
    vspace.grid(row=0, column=0)

    Aircraft = lb(help_Window, text="Aircraft:", bootstyle='danger', font=("Arial", title_label_size))
    Aircraft.grid(row=1, column=0)

    LonDer = lb(help_Window, text="LONGITUDINAL DERIVATIVES", bootstyle='primary', font=("Arial", sub_title_label_size))
    LonDer.grid(row=2, column=1)

    Xu = Label(help_Window, text="Xu = -1/m*rho*S*U0*(Cd+Cdu) --> derivative of the resultant force in the 'x' direction with respect to the 'u' velocity.", 
               font=("Arial", entry_label_size))
    Xu.grid(row=3, column=1)

    Zu = Label(help_Window, text="Zu = -1/m*rho*S*U0*(Cl+Clu) --> derivative of the resultant force in the 'z' direction with respect to the 'u' velocity.", 
               font=("Arial", entry_label_size))
    Zu.grid(row=4, column=1)

    Mu = Label(help_Window, text="Mu = rho*S*U0*c/Jy*Cmu --> derivative of the resultant moment in the 'y' direction with respect to the 'u' velocity.", 
               font=("Arial", entry_label_size))
    Mu.grid(row=5, column=1)

    Xw = Label(help_Window, text="Xw = -1/(2*m)*rho*S*U0*(Cl-Cda) --> derivative of the resultant force in the 'x' direction with respect to the 'w' velocity.", 
               font=("Arial", entry_label_size))
    Xw.grid(row=6, column=1)

    Zw = Label(help_Window, text="Zw = -1/(2*m)*rho*S*U0*(Cla+Cd) --> derivative of the resultant force in the 'z' direction with respect to the 'w' velocity.", 
               font=("Arial", entry_label_size))
    Zw.grid(row=7, column=1)

    Mw = Label(help_Window, text="Mw = rho*S*U0*c/(2*Jy)*Cma --> derivative of the resultant moment in the 'y' direction with respect to the 'w' velocity.", 
               font=("Arial", entry_label_size))
    Mw.grid(row=8, column=1)

    MwD = Label(help_Window, text="MwD = rho*S*c^2/(4*Jy)*CmaD --> derivative of the resultant moment in the 'y' direction with respect to the derivative of the 'w' velocity.", 
               font=("Arial", entry_label_size))
    MwD.grid(row=9, column=1)

    Mq = Label(help_Window, text="Mq = rho*S*U0*c^2/(4*Jy)*Cmq --> derivative of the resultant moment in the 'y' direction with respect to the 'q' angular velocity.", 
               font=("Arial", entry_label_size))
    Mq.grid(row=10, column=1)

    Zde = Label(help_Window, text="Zde = -rho*S*U0^2/(2*m)*Clde --> derivative of the resultant force in the 'z' direction with respect to the 'de' elevator angle.", 
               font=("Arial", entry_label_size))
    Zde.grid(row=11, column=1)

    Mde = Label(help_Window, text="Mde = rho*S*U0^2*c/(2*Jy)*Cmde --> derivative of the resultant moment in the 'y' direction with respect to the 'de' elevator angle.", 
               font=("Arial", entry_label_size))
    Mde.grid(row=12, column=1)

    LatDer = lb(help_Window, text="LATERAL DERIVATIVES", bootstyle='primary', font=("Arial", sub_title_label_size))
    LatDer.grid(row=13, column=1)

    Yv = Label(help_Window, text="Yv = rho*S*U0/(2*m)*Cyb --> derivative of the resultant force in the 'y' direction with respect to the 'v' velocity.", 
               font=("Arial", entry_label_size))
    Yv.grid(row=14, column=1)

    Ydrstar = Label(help_Window, text="Ydr* = rho*S*U0/(2*m)*Cydr --> derivative of the resultant force in the 'y' direction with respect to the 'dr' rudder angle.", 
               font=("Arial", entry_label_size))
    Ydrstar.grid(row=15, column=1)

    Lbeta = Label(help_Window, text="Lb = rho*S*U0^2*b/(2*Jx)*Clb --> derivative of the resultant moment in the 'x' direction with respect to the 'beta' sideslip angle.", 
               font=("Arial", entry_label_size))
    Lbeta.grid(row=16, column=1)

    Lp = Label(help_Window, text="Lp = rho*S*U0*b^2/(4*Jx)*Clp --> derivative of the resultant moment in the 'x' direction with respect to the 'p' angular velocity.", 
               font=("Arial", entry_label_size))
    Lp.grid(row=17, column=1)

    Lr = Label(help_Window, text="Lr = rho*S*U0*b^2/(4*Jx)*Clr --> derivative of the resultant moment in the 'x' direction with respect to the 'r' angular velocity.", 
               font=("Arial", entry_label_size))
    Lr.grid(row=18, column=1)

    def quitHelp():
        print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Help window is closed.")
        logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Help window is closed.")
        help_Window.destroy()

    quit_help_button = Button(help_Window, text="Quit", command=quitHelp, height=1, width=10)
    quit_help_button.grid(row=100, column=0)