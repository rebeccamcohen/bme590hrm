import hrm_processor as p
from hrm_reader import import_data
import numpy as np
import logging

if __name__ == "__main__":
    logging.basicConfig(filename="main_log.txt",
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        level=logging.DEBUG)
    
    file = 'test_data/test_data12.csv'
    data = import_data(file)
    print(data)

    extremes = p.find_min_max(data)
    print(extremes)

    duration = p.find_duration(data)
    print(duration)

    windowlen = p.find_windowlen(data)
    (w1, w2, w3, w4, w5) = p.divide_data(data, windowlen)
    (ind_w1, ind_w2, ind_w3, ind_w4, ind_w5) = \
        p.find_peak_indices(w1, w2, w3, w4, w5)

    (num_peaks1, num_peaks2, num_peaks3, num_peaks4, num_peaks5) = \
        p.find_num_peaks_window(ind_w1, ind_w2, ind_w3, ind_w4, ind_w5)

    num_peaks_total = p.find_num_peaks_total(ind_w1, ind_w2, ind_w3, ind_w4,
                                             ind_w5)

    time_of_peaks = p.find_time_of_peaks(w1, w2, w3, w4, w5, ind_w1,
                                         ind_w2, ind_w3, ind_w4, ind_w5)
    print(time_of_peaks)
    try:
        bpm = p.find_bpm(duration, num_peaks_total)
    except ValueError:
        logging.error("div")
    print(bpm)

    metrics = p.create_metrics_dictionary(bpm, extremes, duration,
                                          num_peaks_total, time_of_peaks)
    print(metrics)
    
