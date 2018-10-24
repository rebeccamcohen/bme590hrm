#in numpy array: axis=0 refers to rows and axis=1 refers to columns
import numpy
import peakutils

def find_min_max(data):
    minVoltage = numpy.amin(data[:, 1])
    maxVoltage = numpy.amax(data[:, 1])
    extremes = (minVoltage, maxVoltage)
    return extremes

def find_duration(data):
    len_time = len(data[:,1])
    duration = data[len_time-1,0] - data[0,0]
    return duration

def find_peak_indices(data):
    ind = peakutils.indexes(data[:,1], thres=0.5*numpy.amax(data[:,1]))
    return ind

def find_num_peaks(i):
    if len(i) == 0:
        raise TypeError
    else:
        return len(i)

def find_time_of_peaks(data,ind):
    time_of_peaks = data[ind,0]
    return time_of_peaks

def find_bpm(duration, num_beats):
    duration_inMins = duration/60
    bpm = num_beats/duration_inMins
    return bpm

def create_metrics_dictionary(a,b,c,d,e):
    metrics_dict = {}
    metrics_dict["mean_hr_bpm"] = a
    metrics_dict["voltage_extremes"] = b
    metrics_dict["duration"] = c
    metrics_dict["num_beats"] = d
    metrics_dict["beats"] = e

    return metrics_dict