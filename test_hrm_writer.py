from hrm_writer import write_jsonfile
import json


def test_write_jsonfile():
    test_dict = {}
    test_dict["Name"] = "Rebecca"
    test_dict["Last Name"] = "Cohen"
    test_dict["Age"] = 21
    test_dict["Tuple"] = [1, 2]
    test_dict["Empty"] = []
    test_dict["Nested"] = {}
    test_dict["Nested"]["a"] = 1
    test_dict["Nested"]["b"] = "It is cool that dictionaries can be nested"
    func_result = write_jsonfile(test_dict, "test_jsonfile")

    with open('test_jsonfile.json', 'r') as readfile:
        read_test_dict = json.load(readfile)

    assert test_dict == read_test_dict
