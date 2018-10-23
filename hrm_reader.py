def import_data(file):
    import numpy as np

    try:
        data = np.loadtxt(file, delimiter=',')
    except ValueError:
       print("CSV file must only contain numbers")
    else:
        return data
