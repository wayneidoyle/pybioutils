""" pybioutils- Collection of functions used for bioinformatics related analyses"""

__version__ = '0.1.0'
__author__ = 'Wayne Doyle'
__all__ = ['bedutils',
           ]
# Set-up logger
import logging
log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO,
                    format=log_fmt,
                    datefmt='%b-%d-%y  %H%M:%S')
logger = logging.getLogger(__name__)

# Import packages
from pybioutils  import *
