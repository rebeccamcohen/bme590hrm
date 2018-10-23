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

#def validate_data(x,y):
    len_time = len(x)
    len_voltage = len(y)

    #if len_time != len_voltage:


if __name__ == "__main__":
    data = import_data('test_data/test_data1.csv')
    print(data)
    time = data[0]
    print(time)
    voltage = data[1]
    print(voltage)





