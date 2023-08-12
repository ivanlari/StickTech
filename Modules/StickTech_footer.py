def footer(root, Solve_OL, Print_TF, Solve_CL, ViewResult, ViewPlot, SaveInputs, LoadInputs):
    
    # Buttons
    from tkinter import Button

    Calcola_OL = Button(root, text="Solve \nOpen Loop", command=Solve_OL, height=3, width=15)
    Calcola_OL.grid(row=53, column=2)

    Result = Button(root, text="View Result", command=ViewResult, height=2, width=15)
    Result.grid(row=54, column=2)

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

    Chiudi = Button(root, text="Close", command=root.quit, height=3, width=10)
    Chiudi.grid(row=53, column=6)