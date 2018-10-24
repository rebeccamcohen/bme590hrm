from hrm_reader import import_data
import numpy
import pytest

def test_data_simple():
    data = import_data("test_hrm_reader_data3.csv")
    numpy.testing.assert_array_equal(data, [(1, 2), (3, 4), (5, 6)])

def test_data_floatsOnly():
    with pytest.raises(ValueError):
        data1 = import_data("test_hrm_reader_data1.csv")

def test_data_extraColumn():
    with pytest.raises(ValueError):
        data2 = import_data("test_hrm_reader_data2.csv")

