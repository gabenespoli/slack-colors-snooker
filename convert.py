"""
Convert slack black.css to snooker.css
"""

import re
import pandas as pd

infile = 'black.css'
outfile = 'snooker.css'
mapfile = 'color_map.csv'
snookerfile = 'color_snooker.csv'

def convert_colors():
    with open(infile, 'r') as fin:
        css = fin.read()

    css_base16 = replace_with_dict(css, csv2dict(mapfile))
    css_snooker = replace_with_dict(css_base16, csv2dict(snookerfile))

    with open(outfile, 'w') as fout:
        fout.write(css_snooker)
        fout.close()

def replace_with_dict(string, d):
    for key, val in d.items():
        string = re.sub('#'+key, '#'+val, string)
    return string

def csv2dict(fname):
    """convert a two-column csv to a dict"""
    return pd.read_csv(fname, header=None, index_col=0, squeeze=True).to_dict()

if __name__ == '__main__':
    convert_colors()
