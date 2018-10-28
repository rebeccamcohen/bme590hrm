import logging

logging.basicConfig(filename="main_log.txt",
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)


def import_data(file):
    """load in csv file containing data

    Args:
        file (str): filename

    Raises:
        ValueError on ill-conditioned CSV file

    Returns:
        data (array): Time and voltage

    """
    import numpy as np
    import logging

    try:
        data = np.loadtxt(file, delimiter=',')
    except ValueError:
        logging.warning("CSV file could not be uploaded")
        raise ValueError("CSV file must only contain numbers")

    logging.info('data successfully uploaded')
    return data
