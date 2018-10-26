from hrm_processor import find_min_max
from hrm_processor import find_duration
from hrm_processor import find_windowlen
from hrm_processor import divide_data
from hrm_processor import find_peak_indices
from hrm_processor import find_num_peaks_window
from hrm_processor import find_num_peaks_total
from hrm_processor import find_time_of_peaks
from hrm_processor import find_bpm
from hrm_processor import create_metrics_dictionary
import numpy


def test_find_min():
    data = numpy.array([(1, 2), (3, 4), (5, 6)])
    extremes = find_min_max(data)
    expected = [2, 6]
    assert extremes == [2, 6]


def test_find_duration():
    data = numpy.array([(1.5, 2), (3, 4), (5.5, 6)])
    duration = find_duration(data)
    expected = 4
    assert duration == expected


def test_find_windowlen():
    data = numpy.array([(1.5, 2), (3, 4), (5.5, 6), (1.5, 2), (3, 4),
                        (5.5, 6), (1.5, 2), (3, 4), (5.5, 6), (1.5, 2),
                        (3, 4), (5.5, 6), (1.5, 2), (3, 4), (5.5, 6),
                        (3, 4), (5.5, 6)])
    windowlen = find_windowlen(data)
    expected = 3
    assert windowlen == expected


def test_divide_data():
    data = numpy.array([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12),
                        (13, 14), (15, 16), (17, 18), (19, 20), (21, 22),
                        (23, 24), (25, 26), (27, 28), (29, 30), (31, 32),
                        (33, 34)])
    windowlen = 3
    (w1, w2, w3, w4, w5) = divide_data(data, windowlen)
    expectedw1 = numpy.array([(1, 2), (3, 4), (5, 6)])
    expectedw2 = numpy.array([(7, 8), (9, 10), (11, 12)])
    expectedw3 = numpy.array([(13, 14), (15, 16), (17, 18)])
    expectedw4 = numpy.array([(19, 20), (21, 22), (23, 24)])
    expectedw5 = numpy.array([(25, 26), (27, 28), (29, 30),
                              (31, 32), (33, 34)])

    numpy.testing.assert_array_equal(w1, expectedw1)
    numpy.testing.assert_array_equal(w2, expectedw2)
    numpy.testing.assert_array_equal(w3, expectedw3)
    numpy.testing.assert_array_equal(w4, expectedw4)
    numpy.testing.assert_array_equal(w5, expectedw5)


def test_find_peak_indices():
    data = numpy.loadtxt("test_hrm_processorData.csv", delimiter=',')

    w1 = data[0:80, :]
    w2 = data[80:160, :]
    w3 = data[160:240, :]
    w4 = data[240:320, :]
    w5 = data[320:, :]

    (peakInds_w1, peakInds_w2, peakInds_w3, peakInds_w4, peakInds_w5) = \
        find_peak_indices(w1, w2, w3, w4, w5)

    numpy.testing.assert_array_equal(peakInds_w1, ([8, 39, 71]))
    numpy.testing.assert_array_equal(peakInds_w2, ([22, 54]))
    numpy.testing.assert_array_equal(peakInds_w3, ([5, 36, 68]))
    numpy.testing.assert_array_equal(peakInds_w4, ([19, 51]))
    numpy.testing.assert_array_equal(peakInds_w5, ([2, 33, 65]))


def test_find_num_peaks_window():
    peakInds_w1 = [8, 39, 71]
    peakInds_w2 = [22, 54]
    peakInds_w3 = [5, 36, 68]
    peakInds_w4 = [19, 51]
    peakInds_w5 = [2, 33, 65]
    (numBeats_w1, numBeats_w2, numBeats_w3, numBeats_w4,
     numBeats_w5) = find_num_peaks_window(peakInds_w1, peakInds_w2,
                                          peakInds_w3, peakInds_w4,
                                          peakInds_w5)

    assert numBeats_w1 == 3
    assert numBeats_w2 == 2
    assert numBeats_w3 == 3
    assert numBeats_w4 == 2
    assert numBeats_w5 == 3


def test_find_num_peaks_total():
    peakInds_w1 = [8, 39, 71]
    peakInds_w2 = [22, 54]
    peakInds_w3 = [5, 36, 68]
    peakInds_w4 = [19, 51]
    peakInds_w5 = [2, 33, 65]

    numBeats = find_num_peaks_total(peakInds_w1,
                                    peakInds_w2, peakInds_w3, peakInds_w4,
                                    peakInds_w5)

    assert numBeats == 13


def test_find_time_of_peaks():
    data = numpy.loadtxt("test_hrm_processorData.csv", delimiter=',')

    w1 = data[0:80, :]
    w2 = data[80:160, :]
    w3 = data[160:240, :]
    w4 = data[240:320, :]
    w5 = data[320:, :]

    peakInds_w1 = [8, 39, 71]
    peakInds_w2 = [22, 54]
    peakInds_w3 = [5, 36, 68]
    peakInds_w4 = [19, 51]
    peakInds_w5 = [2, 33, 65]

    time_of_peaks = find_time_of_peaks(w1, w2, w3, w4, w5,
                                       peakInds_w1, peakInds_w2, peakInds_w3,
                                       peakInds_w4, peakInds_w5)

    numpy.testing.assert_array_almost_equal(time_of_peaks,
                                            ([1.6, 7.8, 14.2, 20.4, 26.8, 33.,
                                              39.2, 45.6, 51.8, 58.2, 64.4,
                                              70.6, 77.]))


def test_find_bpm():
    duration = 6000
    numbeats = 100
    bpm = find_bpm(duration, numbeats)
    assert bpm == 1


def test_create_metrics_dictionary():
    a = []
    b = 'hi'
    c = 6
    d = 5.59
    e = ([1, 2, 3])
    metrics = create_metrics_dictionary(a, b, c, d, e)

    assert metrics == {'mean_hr_bpm': [],
                       'voltage_extremes': 'hi',
                       'duration': 6,
                       'num_beats': 5.59,
                       'beats': [1, 2, 3]}
