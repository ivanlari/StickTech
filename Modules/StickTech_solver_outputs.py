def outputs(solver_outputs, dynamics_outputs):

    t_span  = solver_outputs[0]
    q       = solver_outputs[1]
    t_max   = solver_outputs[2]
    theta   = solver_outputs[3]
    alpha   = solver_outputs[4]
    h       = solver_outputs[5]
    gamma   = solver_outputs[6]
    beta    = solver_outputs[7]
    p       = solver_outputs[8]
    r       = solver_outputs[9]
    phi     = solver_outputs[10]
    u       = solver_outputs[11]
    w       = solver_outputs[12]
    psi     = solver_outputs[13]

    w_SP        = dynamics_outputs[0]
    z_SP        = dynamics_outputs[1]
    w_LP        = dynamics_outputs[2]
    z_LP        = dynamics_outputs[3]
    p_roll      = dynamics_outputs[4]
    p_spiral    = dynamics_outputs[5]
    w_DR        = dynamics_outputs[6]
    z_DR        = dynamics_outputs[7]

    with open(r'Solver_Outputs.txt', 'w') as solver_output_file:
            solver_output_file.write("AIRCRAFT DYNAMICS CHARACTERISTICS \n")
            solver_output_file.write("\nLONGITUDINAL \n")
            solver_output_file.write("\nShort Period frequency: " + str(f'{w_SP:.3f}') + " rad/s \n")
            solver_output_file.write("\nShort Period damping: " + str(f'{z_SP:.3f}') + "\n")
            solver_output_file.write("\nPhugoid frequency: " + str(f'{w_LP:.3f}') + " rad/s \n")
            solver_output_file.write("\nPhugoid damping: " + str(f'{z_LP:.3f}') + "\n")
            solver_output_file.write("\nLATERAL-DIRECTIONAL \n")
            solver_output_file.write("\nRoll subsidence pole: " + str(f'{p_roll:.3f}') + " rad/s \n")
            solver_output_file.write("\nSpiral pole: " + str(f'{p_spiral:.3f}') + " rad/s \n")
            solver_output_file.write("\nDutch Roll frequency: " + str(f'{w_DR:.3f}') + " rad/s \n")
            solver_output_file.write("\nDutch Roll damping: " + str(f'{z_DR:.3f}') + "\n")
            solver_output_file.write("\nOPEN-LOOP DYNAMIC ANALYSIS OUTPUTS \n")
            solver_output_file.write("\n" + "t    " + "    " + "u    " + "    " + "w    " + "    " + 
                "q    " + "    " + "Theta" + "    " + "h    " + "    " + "Beta " + "    " + 
                "p    " + "    " + "r    " + "    " + "phi  " + "    " + "psi   ")
            solver_output_file.write("\n")
            for i in range(len(t_span)):
                # write each item on a new line
                solver_output_file.write("\n" + str(f'{t_span[i]:.3f}') + "    " + str(f'{u[i]:.3f}') + "    " + 
                    str(f'{w[i]:.3f}') + "    " + str(f'{q[i]:.3f}') + "    " + str(f'{theta[i]:.3f}') + "    " + 
                    str(f'{h[i]:.3f}') + "    " + str(f'{beta[i]:.3f}') + "    " + str(f'{p[i]:.3f}') + "    " + 
                    str(f'{r[i]:.3f}') + "    " + str(f'{phi[i]:.3f}') + "    " + str(f'{psi[i]:.3f}'))     