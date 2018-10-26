import numpy
import peakutils
import logging

logging.basicConfig(filename="main_log.txt",
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)


def find_min_max(data):
    """Find extreme voltage values

    Args:
        data (ndarray): Time and voltage data

    Returns:
        extremes (list): Minimum and maximum voltage values
    """

    minVoltage = numpy.amin(data[:, 1])
    maxVoltage = numpy.amax(data[:, 1])
    extremes = [minVoltage, maxVoltage]
    logging.info('Calculated the voltage extremes as %s', extremes)
    return extremes


def find_duration(data):
    """Find time duration of of the ECG strip

    Args:
        data (ndarray): Time and voltage data

    Returns:
        duration (float): time duration of ECG strip
    """
    len_time = len(data[:, 1])
    duration = data[len_time-1, 0] - data[0, 0]
    logging.info('Calculated the duration as %s', duration)
    return duration


def find_windowlen(data):
    """Calculates length of five smaller arrays,
    will refer to as windows

    Args:
        data (ndarray): Time and voltage data

    Returns:
        windowlen (int): Length of sub-arrays
    """
    numTime = len(data[:, 0])
    numVoltage = len(data[:, 1])
    if numVoltage != numTime:
        numEntries = min(numData, numTime)
    else:
        numEntries = numTime

    windowlen = round(numEntries/5)
    return windowlen


def divide_data(data, windowlen):
    """Divides data array into five smaller arrays

    Args:
        data (ndarray): Time and voltage data
        windowlen (int): Length of sub-arrays

    Returns:
        w1 (ndarray): Time and voltage data in window 1
        w2 (ndarray): Time and voltage data in window 2
        w3 (ndarray): Time and voltage data in window 3
        w4 (ndarray): Time and voltage data in window 4
        w5 (ndarray): Time and voltage data in window 5
    """
    w1 = data[0:windowlen, :]
    w2 = data[windowlen:windowlen*2, :]
    w3 = data[(windowlen * 2):windowlen * 3, :]
    w4 = data[(windowlen * 3):windowlen * 4, :]
    w5 = data[(windowlen * 4):, :]

    return w1, w2, w3, w4, w5


def find_peak_indices(w1, w2, w3, w4, w5):
    """Finds indices of peaks in all 5 windows

    Args:
        w1 (ndarray): Time and voltage data in window 1
        w2 (ndarray): Time and voltage data in window 2
        w3 (ndarray): Time and voltage data in window 3
        w4 (ndarray): Time and voltage data in window 4
        w5 (ndarray): Time and voltage data in window 5

    Returns:
        ind_w1 (ndarray): Indices of voltage peaks in window 1
        ind_w2 (ndarray): Indices of voltage peaks in window 2
        ind_w3 (ndarray): Indices of voltage peaks in window 3
        ind_w4 (ndarray): Indices of voltage peaks in window 4
        ind_w5 (ndarray): Indices of voltage peaks in window 5
    """
    import peakutils

    ind_w1 = peakutils.indexes(w1[:, 1], thres=0.5 * numpy.amax(w1[:, 1]))
    ind_w2 = peakutils.indexes(w2[:, 1], thres=0.5 * numpy.amax(w2[:, 1]))
    ind_w3 = peakutils.indexes(w3[:, 1], thres=0.5 * numpy.amax(w3[:, 1]))
    ind_w4 = peakutils.indexes(w4[:, 1], thres=0.5 * numpy.amax(w4[:, 1]))
    ind_w5 = peakutils.indexes(w5[:, 1], thres=0.5 * numpy.amax(w5[:, 1]))

    return ind_w1, ind_w2, ind_w3, ind_w4, ind_w5


def find_num_peaks_window(ind_w1, ind_w2, ind_w3, ind_w4, ind_w5):
    """Computes number of peaks in each window

    Args:
        ind_w1 (ndarray): Indices of voltage peaks in window 1
        ind_w2 (ndarray): Indices of voltage peaks in window 2
        ind_w3 (ndarray): Indices of voltage peaks in window 3
        ind_w4 (ndarray): Indices of voltage peaks in window 4
        ind_w5 (ndarray): Indices of voltage peaks in window 5

    Returns:
        num_peaks1 (int): Number of peaks in window 1
        num_peaks2 (int): Number of peaks in window 2
        num_peaks3 (int): Number of peaks in window 3
        num_peaks4 (int): Number of peaks in window 4
        num_peaks5 (int): Number of peaks in window 5

    """
    return len(ind_w1), len(ind_w2), len(ind_w3), len(ind_w4), len(ind_w5)


def find_num_peaks_total(ind_w1, ind_w2, ind_w3, ind_w4, ind_w5):
    """Computes number of detected beats in the ECG strip

    Args:
        ind_w1 (ndarray): Indices of voltage peaks in window 1
        ind_w2 (ndarray): Indices of voltage peaks in window 2
        ind_w3 (ndarray): Indices of voltage peaks in window 3
        ind_w4 (ndarray): Indices of voltage peaks in window 4
        ind_w5 (ndarray): Indices of voltage peaks in window 5

    Returns:
        num_peaks_total (int): Total number of detected beats in the ECG strip"
    """
    num_peaks_total = len(ind_w1) + len(ind_w2) \
        + len(ind_w3) + len(ind_w4) + len(ind_w5)
    logging.info('Calculated the number of detected beats as %s',
                 num_peaks_total)
    return num_peaks_total


def find_time_of_peaks(w1, w2, w3, w4, w5,
                       ind_w1, ind_w2, ind_w3, ind_w4, ind_w5):
    """Creates numpy array of times corresponding to beats

    Args:
        w1 (ndarray): Time and voltage data in window 1
        w2 (ndarray): Time and voltage data in window 2
        w3 (ndarray): Time and voltage data in window 3
        w4 (ndarray): Time and voltage data in window 4
        w5 (ndarray): Time and voltage data in window 5
        ind_w1 (ndarray): Indices of voltage peaks in window 1
        ind_w2 (ndarray): Indices of voltage peaks in window 2
        ind_w3 (ndarray): Indices of voltage peaks in window 3
        ind_w4 (ndarray): Indices of voltage peaks in window 4
        ind_w5 (ndarray): Indices of voltage peaks in window 5

    Returns:
        time_of_peaks (ndarray): Time values corresponding
        to each detected beat
    """
    time_of_peaks1 = w1[ind_w1, 0]
    time_of_peaks2 = w2[ind_w2, 0]
    time_of_peaks3 = w3[ind_w3, 0]
    time_of_peaks4 = w4[ind_w4, 0]
    time_of_peaks5 = w5[ind_w5, 0]

    time_of_peaks = numpy.concatenate((time_of_peaks1, time_of_peaks2,
                                       time_of_peaks3, time_of_peaks4,
                                       time_of_peaks5))
    time_of_peaks = numpy.ndarray.tolist(time_of_peaks)
    logging.info('Calculated the times when a beat occurred: %s',
                 time_of_peaks)
    return time_of_peaks


def find_bpm(duration, num_peaks_total):
    """Calculates estimated average heart rate

    Args:
        duration (float): time duration of ECG strip
        num_peaks_total (int): Total number of detected beats in the ECG strip

    Returns:
        bpm (float): Estimated average heart rate

    Raises:
        ValueError: If calculated bpm is larger than 200
    """
    logging.basicConfig(filename="dict.txt",
                        format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')

    duration_inmins = duration / 60

    bpm = num_peaks_total / duration_inmins
    logging.info('Calculated the bpm as %s', bpm)

    if bpm > 200:
        logging.warning('bpm is too high, most likely due to faulty data')
    return bpm


def create_metrics_dictionary(bpm, extremes, duration,
                              num_peaks_total, time_of_peaks):
    """Creates dictionary with calculated metrics

    Args:
        bpm (float): Estimated average heart rate
        extremes (list): Minimum and maximum voltage values
        duration (float): Time duration of ECG strip
        num_peaks_total (int): Total number of detected beats in the ECG strip
        time_of_peaks (ndarray): Time values corresponding
        to each detected beat"

    Returns:
        metrics_dict (dict): dictionary consisting of calculated metrics
    """
    metrics_dict = {}
    metrics_dict["mean_hr_bpm"] = bpm
    metrics_dict["voltage_extremes"] = extremes
    metrics_dict["duration"] = duration
    metrics_dict["num_beats"] = num_peaks_total
    metrics_dict["beats"] = time_of_peaks

    logging.info("Created dictionary for metrics")
    return metrics_dict
