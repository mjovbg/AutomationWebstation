import inspect
import logging


def customLogger(logLevel=logging.DEBUG):
    # with debug you log everything.
    # Gets the name of the class / method from where this method is called (this is why you need inspect).
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("automation.log".format(loggerName),
                                      mode='w')  # mode = w means it will overwrite the file every time you run it. a means append.
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger
