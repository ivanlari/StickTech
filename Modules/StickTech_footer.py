def footer(root, Solve_OL, Print_TF, Solve_CL, ViewResult, ViewPlot, SaveInputs, LoadInputs, 
           AnimateResults, QuitRoot, OpenWD):
    
    from tkinter import Button, Frame
    from ttkbootstrap import Button as bt, Style
    import os
    import subprocess
    from subprocess import run

    Calcola_OL = Button(root, text="Solve \nOpen Loop", command=Solve_OL, height=3, width=15)
    Calcola_OL.grid(row=53, column=2)
  
    Result = Button(root, text="View Result", command=ViewResult, height=2, width=15)
    Result.grid(row=54, column=2)

    Animate = Button(root, text="Animate Result", command=AnimateResults, height=2, width=15)
    Animate.grid(row=55, column=2)

    tf = Button(root, text="Print \nTransfer Function", command=Print_TF, height=3, width=15)
    tf.grid(row=53, column=4)

    plot = Button(root, text="View Plot", command=ViewPlot, height=2, width=15)
    plot.grid(row=55, column=4)

    Calcola_CL = Button(root, text="Solve \nClosed Loop", command=Solve_CL, height=3, width=15)
    Calcola_CL.grid(row=53, column=5)

    Save_inputs = Button(root, text="Save Inputs", command=SaveInputs, height=1, width=15)
    Save_inputs.grid(row=54, column=6)

    Load_inputs = Button(root, text="Load Inputs", command=LoadInputs, height=1, width=15)
    Load_inputs.grid(row=55, column=6)

#     Help_style = Style()
#     Help_style.configure('warning.Outline.TButton', font=("Arial", 10))
#     Help_button = bt(text="Help", bootstyle='warning, outline', style="warning.Outline.TButton", 
#                      command=Help, width=7)
#     Help_button.grid(row=55, column=3)

    OpenWD_style = Style()
    OpenWD_style.configure('secondary.Outline.TButton', font=("Arial", 10))
    OpenWD_button = bt(text="Open Output Folder", bootstyle='secondary, outline', style="secondary.Outline.TButton", 
                     command=OpenWD, width=16)
    OpenWD_button.grid(row=55, column=5)

    Chiudi = Button(root, text="Quit", command=QuitRoot, height=2, width=10)
    Chiudi.grid(row=53, column=6)