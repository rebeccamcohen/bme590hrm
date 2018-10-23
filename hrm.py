from hrm_reader import import_data

if __name__ == "__main__":
    data = import_data('test_data/test_data1.csv')
    print(data)
    time = data[0]
    print(time)
    voltage = data[1]
    print(voltage)





