import logging

logger = logging.getLogger(__name__)


def hello_world():
    logger.info("Hello World function is called")
    print("Ciao Mondo ! ")
    unused = 13
    logger.debug("Unused variable set to 13")
    unused = 13
    logger.debug("Unused variable set again to 13")
    unused = 13
    logger.debug("Unused variable set yet again to 13")
    unused = 13
    logger.debug("And again, unused variable set to 13")
    unused = 13
    logger.debug("Finally, unused variable set to 13 for the last time")


def hello_mars():
    logger.info("Hello Mars function is called")
    print("Ciao Marte ! ")


if __name__ == "__main__":
    logger.info("Main execution started")
    hello_world()
    hello_mars()
    logger.info("Main execution finished")
