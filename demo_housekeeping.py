import logging

logger = logging.getLogger(__name__)


def hello_world():
    logger.info("Executing hello_world function")
    print("Ciao Mondo ! ")
    unused = 13
    logger.debug("Unused variable set to 13")
    unused = 13
    logger.debug("Unused variable set to 13 again")
    unused = 13
    unused = 13
    unused = 13


def hello_mars():
    logger.info("Executing hello_mars function")
    print("Ciao Marte ! ")


if __name__ == "__main__":
    logger.info("Starting the main execution")
    main()
