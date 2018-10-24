import json

def write_jsonfile(dict,filename):
    with open((filename + '.json'), 'w') as outfile:
    json.dump(dict, outfile, sort_keys=True, indent=4)
