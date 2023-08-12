def load_inputs():
    
    import os
    import re

    # Read inputs file
    if os.path.isfile("GUI_Inputs.txt"):
        gui_inputs = open('GUI_Inputs.txt', 'r')
        inputsLines = gui_inputs.readlines()
        
        # Removing newline character from string
        # Using regex
        gui_list_trim_load = []
        for sub in inputsLines:
            gui_list_trim_load.append(float(re.sub('\n', '', sub))) # Store inputs in a list
        
        return gui_list_trim_load
    else:
        print("\nNo Inputs file was found in current working directory.")

    