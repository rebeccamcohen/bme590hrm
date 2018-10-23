def import_data(file):
    import csv
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        time = []
        voltage = []

        for row in csv_reader:
            t = float(row[0])
            v = float(row[1])
            time.append(t)
            voltage.append(v)
        return time, voltage