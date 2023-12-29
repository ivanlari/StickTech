def header(code_name, code_build, code_developer, last_update, save_path, directory):
    
    import os
    import logging
    from datetime import datetime

    print("##########################################################################")
    print("##----------------------------------------------------------------------##")
    print("##---------------------------- " + code_name + " " + code_build + " ---------------------------##")
    print("##----------------------------------------------------------------------##")
    print("##----------------------- Developed by " + code_developer + " -----------------------##")
    print("##---------------------------- " + last_update + " ---------------------------##")
    print("##----------------------------------------------------------------------##")
    print("##########################################################################\n")

    try: 
        os.mkdir(save_path) 
        print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    A directory called %s " % directory + "has been created in C:/.")
        #logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    A directory called %s " % directory + "has been created in C:/.")
    except OSError as error: 
        # print(error)
        print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    A directory for this analysis already exists.")
        #logging.error(error) 
        #logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    A directory for this analysis already exists.")

    # Make save directory the current working directory:
    cwd = save_path
    os.chdir(cwd)

    # Set Log file
    logfile = os.path.join(save_path, 'StickTechLOG.log')
    logging.basicConfig(filename=logfile, level=logging.INFO, 
                        format='%(levelname)s:%(message)s') # Add filemode="w" to overwrite the log file at each run
    
    logging.info('########################################################################################\n')
    logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + '    StickTech RUN' +  '\n')

    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Current working directory:  %s" % cwd)
    logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Current working directory:  %s" % cwd)