import numpy
import peakutils


def find_min_max(data):
    minVoltage = numpy.amin(data[:, 1])
    maxVoltage = numpy.amax(data[:, 1])
    extremes = (minVoltage, maxVoltage)
    return extremes


def find_duration(data):
    len_time = len(data[:, 1])
    duration = data[len_time-1, 0] - data[0, 0]
    return duration


def find_windowlen(data):
    numTime = len(data[:, 0])
    numVoltage = len(data[:, 1])
    if numVoltage != numTime:
        numEntries = min(numData, numTime)
    else:
        numEntries = numTime

    windowlen = round(numEntries/5)
    return windowlen


def divide_data(data, windowlen):
    w1 = data[0:windowlen, :]
    w2 = data[windowlen:windowlen*2, :]
    w3 = data[(windowlen * 2):windowlen * 3, :]
    w4 = data[(windowlen * 3):windowlen * 4, :]
    w5 = data[(windowlen * 4):, :]

    return w1, w2, w3, w4, w5


def find_peak_indices(w1, w2, w3, w4, w5):

    ind_w1 = peakutils.indexes(w1[:, 1], thres=0.5 * numpy.amax(w1[:, 1]))
    ind_w2 = peakutils.indexes(w2[:, 1], thres=0.5 * numpy.amax(w2[:, 1]))
    ind_w3 = peakutils.indexes(w3[:, 1], thres=0.5 * numpy.amax(w3[:, 1]))
    ind_w4 = peakutils.indexes(w4[:, 1], thres=0.5 * numpy.amax(w4[:, 1]))
    ind_w5 = peakutils.indexes(w5[:, 1], thres=0.5 * numpy.amax(w5[:, 1]))

    return ind_w1, ind_w2, ind_w3, ind_w4, ind_w5


def find_num_peaks_window(ind_w1, ind_w2, ind_w3, ind_w4, ind_w5):
    return len(ind_w1), len(ind_w2), len(ind_w3), len(ind_w4), len(ind_w5)


def find_num_peaks_total(ind_w1, ind_w2, ind_w3, ind_w4, ind_w5):
    return len(ind_w1) + len(ind_w2) + len(ind_w3) + len(ind_w4) + len(ind_w5)


def find_time_of_peaks(w1, w2, w3, w4, w5,
                       ind_w1, ind_w2, ind_w3, ind_w4, ind_w5):
    time_of_peaks1 = w1[ind_w1, 0]
    time_of_peaks2 = w2[ind_w2, 0]
    time_of_peaks3 = w3[ind_w3, 0]
    time_of_peaks4 = w4[ind_w4, 0]
    time_of_peaks5 = w5[ind_w5, 0]

    time_of_peaks = numpy.concatenate((time_of_peaks1, time_of_peaks2,
                                       time_of_peaks3, time_of_peaks4,
                                       time_of_peaks5))
    return time_of_peaks


def find_bpm(duration, total_numPeaks):

    duration_inmins = duration / 60
    bpm = total_numPeaks / duration_inmins

    return bpm


def create_metrics_dictionary(a, b, c, d, e):
    metrics_dict = {}
    metrics_dict["mean_hr_bpm"] = a
    metrics_dict["voltage_extremes"] = b
    metrics_dict["duration"] = c
    metrics_dict["num_beats"] = d
    metrics_dict["beats"] = e

    return metrics_dict
