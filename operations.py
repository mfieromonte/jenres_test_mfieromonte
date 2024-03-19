import logging

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add formatter to ch
ch.setFormatter(formatter)

# Add ch to logger
logger.addHandler(ch)


def get_sums(nums):
  logger.info('Calculating the sum of numbers')
  sums = sum(nums)
  logger.debug('Sum calculated: %s', sums)
  return sums 

def get_nums(nums):
  logger.info('Generating a sequence of numbers')
  sequence = list(range(1, nums+1))
  logger.debug('Sequence generated: %s', sequence)
  return sequence 
