def quitRoot(root):

    import logging
    from datetime import datetime

    print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Quit command is received.")
    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    StickTech is closing.")
    logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Quit command is received.\n")
    logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    StickTech is closed.\n")  
    root.quit()