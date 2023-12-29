# StickTech - Linear Aircraft Dynamics Simulator

import os
import subprocess
import sys
from tkinter import *
from tkinter.ttk import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from Modules import outputs, plots, solver_model, inputs, header, LADS_GUI, footer, print_tf, compute_tf
from Modules import StepTech, results_viewer, plot_viewer, save_inputs, load_inputs, place_inputs
from Modules import animate_outputs, quitRoot, openWD

code_name       = "StickTech"
code_build      = "2.0"
code_developer  = "Ivan Lari"
last_update     = "December 2023"

# ===================================== Set directories =====================================

# Save directory name:
directory   = code_name
    
# Parent directory path:
parent_dir  = os.sep # C:\

# Save path:
save_path   = os.path.join(parent_dir, directory)

# Code directory:
code_dir    = os.path.dirname(os.path.abspath(sys.argv[0]))

# This script:
this_script = os.path.join(code_dir, "StickTech_main.py")

# ===================================== Run GUI =============================================

root = tb.Window(themename = "solar")

GUI_outputs_1, GUI_outputs_2, variable_option_menu, variable_option_menu_2, variable_option_menu_3, chk_var = LADS_GUI(code_name, code_build, root)

# ===================================== Run Header ==========================================

header(code_name, code_build, code_developer, last_update, save_path, directory)

# ===================================== Run Main Solver =====================================

def Solve_OL():

    # ------------------------------------- Run Solver Inputs -------------------------------------

    inputs_list, plots_inputs_list = inputs(GUI_outputs_1)

    # ------------------------------------- Run Model ---------------------------------------------

    solver_outputs, initial_conditions, delta_X0 = solver_model(inputs_list, GUI_outputs_2, chk_var)

    # ------------------------------------- Run Compute TF ----------------------------------------

    [tf_outputs, dynamics_outputs] = compute_tf(inputs_list)

    # ------------------------------------- Run Plotter -------------------------------------------

    plots(solver_outputs, plots_inputs_list, dynamics_outputs, initial_conditions, delta_X0)

    # ------------------------------------- Run Outputs -------------------------------------------

    outputs(solver_outputs, dynamics_outputs)

# ===================================== Run TF printer ======================================

def Print_TF():

    selected_tf = variable_option_menu.get() # get selected Transfer Function

    # ------------------------------------- Run Solver Inputs -------------------------------------

    inputs_list, plots_inputs_list = inputs(GUI_outputs_1)

    # ------------------------------------- Run Compute TF ----------------------------------------

    [tf_outputs, dynamics_outputs] = compute_tf(inputs_list)

    # ------------------------------------- Run Transfer Functions Printer ------------------------

    print_tf(tf_outputs, selected_tf)

# ===================================== Run StepTec =========================================

def Solve_CL():

    selected_tf = variable_option_menu.get() # get selected Transfer Function

    # ------------------------------------- Run Solver Inputs -------------------------------------

    inputs_list, plots_inputs_list = inputs(GUI_outputs_1)

    # ------------------------------------- Run Compute TF ----------------------------------------

    [tf_outputs, dynamics_outputs] = compute_tf(inputs_list)

    # ------------------------------------- Run StepTech PID Tuner --------------------------------

    StepTech(tf_outputs, selected_tf, code_build)

# ===================================== Run Result Viewer ===================================

def ViewResult():
    
    selected_result = variable_option_menu_2.get() # get selected Result to view

    results_viewer(selected_result)

# ===================================== Run Plot Viewer =====================================

def ViewPlot():

    selected_tf = variable_option_menu.get() # get selected Transfer Function
    
    selected_plot = variable_option_menu_3.get() # get selected plot to view

    inputs_list, plots_inputs_list = inputs(GUI_outputs_1)

    [tf_outputs, dynamics_outputs] = compute_tf(inputs_list)

    plot_viewer(selected_plot, selected_tf, tf_outputs)

# ===================================== Run Save Inputs =====================================

def SaveInputs():

    inputs_list, plots_inputs_list = inputs(GUI_outputs_1)

    save_inputs(inputs_list, GUI_outputs_2)

# ===================================== Run Load Inputs =====================================

def LoadInputs():
    
    gui_list_trim_load = load_inputs()

    place_inputs(gui_list_trim_load, GUI_outputs_1, GUI_outputs_2)

# ===================================== Run Load Inputs =====================================

def AnimateResults():

    selected_result = variable_option_menu_2.get() # get selected Result to view
    
    # ------------------------------------- Run Solver Inputs -------------------------------------

    inputs_list, plots_inputs_list = inputs(GUI_outputs_1)

    # ------------------------------------- Run Model ---------------------------------------------

    solver_outputs = solver_model(inputs_list, GUI_outputs_2)

    # ------------------------------------- Run Animation -----------------------------------------

    animate_outputs(solver_outputs, plots_inputs_list, selected_result, inputs_list)

# ===================================== Quit Root ===========================================

def QuitRoot():
    quitRoot(root)

# ===================================== Open Working Directory ==============================

def OpenWD():
    openWD(save_path)

# ===================================== Run Footer ==========================================

footer(root, Solve_OL, Print_TF, Solve_CL, ViewResult, ViewPlot, SaveInputs, LoadInputs, 
       AnimateResults, QuitRoot, OpenWD)

root.mainloop()