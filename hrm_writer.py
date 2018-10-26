import json


def write_jsonfile(dict, filename):
    """
    Args:
        dict (dict): dictionary consisting of calculated metrics
        filename (str): name of input CSV file

    Returns:
        file (json): contains values of object attributes

    """

    with open((filename + '.json'), 'w') as outfile:
        json.dump(dict, outfile, sort_keys=True, indent=4)
