'''
This file is used to generate csv files 

log numbers 300-399 
'''

import csv


def generate_csv(colHeaders: list, listContent: list[list], csvFileName: str) -> int:
    '''
    generate_csv: generates a csv file with the given content 

    parameters: 
        contentDict - dict, a dictionary of etf objects \\
        csvFile - str, the path to the output csv file 

    returns:  0 for success or non-zero for error
    '''
    try: 
        with open(csvFileName, mode='w') as curCsv:
            fieldnames = colHeaders
            writer = csv.DictWriter(curCsv, fieldnames=fieldnames)
            writer.writeheader() # creates the csv header from fieldnames 
            for row in listContent:
                writer.writerow(dict(zip(colHeaders, row)))
        # config.logmsg('DEBUG', 400, f'saving csv file as {csvFile}')
    except Exception as e:
        # config.logmsg('ERROR', 401, f'{e}')
        print(f"ERROR: {e}")
        return 1
    return 0

if __name__ == "__main__":
    x = ["a", "b", "c"]
    y = [["1", "2", "3"], ["4", "5", "6"]]
    TEST_FILE = "test.csv"
    print(f"generate csv status: {generate_csv(colHeaders=x, listContent=y, csvFileName=TEST_FILE)}")