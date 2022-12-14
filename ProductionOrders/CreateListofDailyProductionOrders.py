# Pre-requisite - Import the writer class from the csv module
from csv import writer
from os.path import exists
from pathlib import Path
from os import chdir
import argparse
import datetime
import logging
from time import sleep

# Move into the right folder

chdir("//SERVER1/ServerData/Production/ProductionOrders_DailyPrint")
date = datetime.datetime.now()      
FilePath = Path(date.strftime("%Y-%m-%d")+"_ProdOrder.csv")
LogPath = Path(date.strftime("%Y-%m-%d")+"_ProdOrder.log")
logging.basicConfig(filename=LogPath, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s',level=logging.DEBUG)

def ParseArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--ProdOrder", help="Production Order Number")
    parser.add_argument("--DueDate", help="Date of the production due")
    parser.add_argument("--Name", help="name of the customer for this production order")

    args = parser.parse_args()
    return args


# ParseArguments
arguments = ParseArguments()


# Get data
headersCSV = ['Production Order','Name','Due Date']

ProdOrder = arguments.ProdOrder
Name = arguments.Name
DueDate = arguments.DueDate
list_data=[ProdOrder,Name,DueDate]


if (not exists(FilePath)):
    try:
        with open(FilePath, 'w', newline='') as NewCsv:
            writer_object = writer(NewCsv, delimiter =',')
            writer_object.writerow(headersCSV)
            logging.info('A new file has been created :') 
            NewCsv.close()
    except Exception as e:
        logging.error('An error occured when creating the file - ')
        # logging.error(' '.join(list_data))
        logging.error(e)
# First, open the old CSV file in append mode, hence mentioned as 'a'
# Then, for the CSV file, create a file object

if (ProdOrder!=None):
    try:
        with open(FilePath, 'a', newline='') as CsvFile:  
            # Pass the CSV  file object to the writer() function
            writer_object = writer(CsvFile, delimiter =',')
            # Result - a writer object
            # Pass the data in the list as an argument into the writerow() function
            writer_object.writerow(list_data)  
            # Close the file object
            CsvFile.close()
            logging.info('A line has been added for Prod Order #')
            logging.info(ProdOrder)
    except Exception as e:
            logging.error('An error occured when updating the file - ')
            # logging.error(' '.join(list_data))
            logging.error(e)
            print("An Error Occured :")
            print(e)
            print("/!\ no line has been added into the ProdList.csv file /!\ ")
            sleep(20)
else:
    logging.warning("Production Number is Empty, not creating a new line")