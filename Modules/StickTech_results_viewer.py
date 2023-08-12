def results_viewer(selected_result):
    
    import os

    if selected_result == "Longitudinal \nDynamics":
        if os.path.isfile("Longitudinal_Dynamics.png"):
            print("\nSelected Result: Longitudinal Dynamics")
            os.system("Longitudinal_Dynamics.png")
        else:
            print("\nAn output file for the selected request is not present. \nRun an analysis before viewing the result.")
    elif selected_result == "Lateral \nDynamics":
        if os.path.isfile("LateralDirectional_Dynamics.png"):
            print("\nSelected Result: Lateral-Directional Dynamics")
            os.system("LateralDirectional_Dynamics.png")
        else:
            print("\nAn output file for the selected request is not present. \nRun an analysis before viewing the result.")
    elif selected_result == "Poles \nPlacement":
        if os.path.isfile("Poles_Placement.png"):
            print("\nSelected Result: Poles Placement")
            os.system("Poles_Placement.png")
        else:
            print("\nAn output file for the selected request is not present. \nRun an analysis before viewing the result.")
    else:
        print("\nSelect a Result to be opened.")