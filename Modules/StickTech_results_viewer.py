def results_viewer(selected_result):
    
    import os
    import logging
    from datetime import datetime

    if selected_result == "Longitudinal \nDynamics":
        if os.path.isfile("Longitudinal_Dynamics.png"):
            print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Result: Longitudinal Dynamics")
            logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Result: Longitudinal Dynamics")
            os.system("Longitudinal_Dynamics.png")
        else:
            print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    An output file for the selected request is not present.")
            logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    An output file for the selected request is not present.")
            print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Run an analysis before viewing the result.")
    elif selected_result == "Lateral \nDynamics":
        if os.path.isfile("LateralDirectional_Dynamics.png"):
            print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Result: Lateral-Directional Dynamics")
            logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Result: Lateral-Directional Dynamics")
            os.system("LateralDirectional_Dynamics.png")
        else:
            print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    An output file for the selected request is not present.")
            logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    An output file for the selected request is not present.")
            print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Run an analysis before viewing the result.")
    elif selected_result == "Poles \nPlacement":
        if os.path.isfile("Poles_Placement.png"):
            print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Result: Poles Placement")
            logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Selected Result: Poles Placement")
            os.system("Poles_Placement.png")
        else:
            print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    An output file for the selected request is not present.")
            logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    An output file for the selected request is not present.")
            print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Run an analysis before viewing the result.")
    else:
        print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Select a Result to be opened.")