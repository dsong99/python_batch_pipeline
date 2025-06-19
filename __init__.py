import sys, os
import logging
logging.basicConfig(
    filename='batch.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(process)d - %(thread)d - %(levelname)s - %(message)s'
)