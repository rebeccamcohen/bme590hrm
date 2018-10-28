import json
import logging

logging.basicConfig(filename="main_log.txt",
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)


def write_jsonfile(dict, filename):
    """writes a json file for the metrics dictionary

    Args:
        dict (dict): dictionary consisting of calculated metrics
        filename (str): name of input CSV file

    Returns:
        file (json): contains values of object attributes

    """

    with open((filename + '.json'), 'w') as outfile:
        json.dump(dict, outfile, sort_keys=True, indent=4)

    logging.info('Wrote json file containing dict with metrics')
