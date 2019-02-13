"""
Convert slack black.css to snooker.css
"""

import re
import pandas as pd

infile = 'template.css'
outfile = 'snooker.css'
snookerfile = 'color_snooker.csv'

def convert_colors():
    with open(infile, 'r') as fin:
        css_template = fin.read()

    css_snooker = replace_with_dict(css_template, csv2dict(snookerfile))

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
