def import_data(file):
    """load in CSV data

    Args:
        file (str): filename

    Raises:
        ValueError on ill-conditioned CSV file

    Returns:
        data (ndarray)
    """
    import numpy as np

    try:
        data = np.loadtxt(file, delimiter=',')
    except ValueError:
        raise ValueError("CSV file must only contain numbers")

    return data
