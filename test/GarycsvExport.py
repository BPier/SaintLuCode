import logging
import argparse

logging.basicConfig(filename='//server1/ServerData/_SaintLuCode/test/Garycsv.log' ,level=logging.DEBUG,format='%(asctime)s - %(message)s')


# Instantiate the parser
parser = argparse.ArgumentParser(description='Prepare report for tinting')

parser.add_argument('csvline')
args = parser.parse_args()

logging.info(f"csvfil generate for {str(args.csvline)}")