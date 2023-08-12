def header(code_name, code_build, code_developer, last_update, save_path, directory):
    
    import os

    print("##########################################################################")
    print("##----------------------------------------------------------------------##")
    print("##---------------------------- " + code_name + " " + code_build + " ---------------------------##")
    print("##----------------------------------------------------------------------##")
    print("##----------------------- Developed by " + code_developer + " -----------------------##")
    print("##---------------------------- " + last_update + " -----------------------------##")
    print("##----------------------------------------------------------------------##")
    print("##########################################################################\n")

    try: 
        os.mkdir(save_path) 
        print ("\nA directory called %s " % directory + "has been ceated in C:/.")
    except OSError as error: 
        # print(error)
        print("\nA directory for this analysis already exists.") 

    # Make save directory the current working directory:
    cwd = save_path
    os.chdir(cwd)
    print("Current working directory:  %s" % cwd)