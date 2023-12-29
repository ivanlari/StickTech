def openWD(savepath):
    import os
    import logging
    from datetime import datetime
    print("\n" + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Working directory is opened.")
    logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Working directory is opened.")
    os.startfile(savepath)