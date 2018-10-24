from hrm_processor import find_min_max
from hrm_processor import find_duration
from hrm_processor import find_peak_indices
from hrm_processor import find_num_peaks
from hrm_processor import find_time_of_peaks
from hrm_processor import find_bpm
from hrm_processor import create_metrics_dictionary
import numpy
import pytest

def test_find_min():
    data = numpy.array([(1, 2), (3, 4), (5, 6)])
    extremes = find_min_max(data)
    expected = (2, 6)
    assert extremes == (2, 6)

def test_find_duration():
    data = numpy.array([(1, 2), (3, 4), (5, 6)])
    duration = find_duration(data)
    expected = 4
    assert duration == expected

def test_find_peak_indices():
    data = numpy.loadtxt("test_hrm_processorData.csv", delimiter=',')
    peakInds = find_peak_indices(data)
    numpy.testing.assert_array_equal(peakInds, ([8, 39, 71, 102, 134, 165, 196, 228, 259, 291, 322, 353, 385]))

def test_find_num_peaks1():
    ind = [8, 39, 71, 102, 134, 165, 196, 228, 259, 291, 322, 353, 385]
    expected = 13
    num_beats = find_num_peaks(ind)

def test_find_num_peaks2():
    with pytest.raises(TypeError):
        ind = []
        find_num_peaks(ind)

def test_find_time_of_peaks():
    data = numpy.loadtxt("test_hrm_processor_data.csv", delimiter=',')
    ind = [8, 39, 71, 102, 134, 165, 196, 228, 259, 291, 322, 353, 385]
    time_of_peaks = find_time_of_peaks(data, ind)
    numpy.testing.assert_array_almost_equal(time_of_peaks, ([1.6, 7.8, 14.2, 20.4, 26.8, 33., 39.2, 45.6, 51.8, 58.2, 64.4, 70.6, 77.]))

def test_find_bpm():
    bpm = find_bpm(6000, 100)
    expected = 1
    assert bpm == expected

def test_create_metrics_dictionary():
    a = 1000
    b = 'hi'
    c = 6
    d = 5.59
    e = ([1, 2, 3])
    metrics = create_metrics_dictionary(a, b, c, d, e)

    assert metrics == {'mean_hr_bpm': 1000,
        'voltage_extremes': 'hi',
        'duration': 6,
        'num_beats': 5.59,
        'beats': [1, 2, 3]}
