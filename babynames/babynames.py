#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
from lxml import html
import re
import glob
import os
"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    file_name = filename.split("/")[-1]
    f = open(file_name, 'r')
    data = f.read()
    ano = file_name.split('.')[0][-4:]
    tree = html.fromstring(data)

    name = tree.xpath('//td//td/text()')
    dic = []

    for i in range(len(name)-3):
        if i % 3 == 0:
            dic.append(name[i+2] + " " + name[i])

    dic = sorted(dic)
    dic2 = [ano]
    dic2 += dic
    return dic2


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]


    for f in args[1:]:
        print(extract_names(f))
    # +++your code here+++
        # For each filename, get the names, then either print the text output
        # or write it to a summary file
    # print(extract_names(args))

if __name__ == '__main__':
    main()
