#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# boneup.py
#
# Copyright 2017 kerook <crafton.anna@gmail.com>
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#    
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#     GNU General Public License for more details.
#    
#     You should have received a copy of the GNU General Public License
#     along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# Please note:
# You should replace the file name with the one you're interesting in. (Example: here it's "questions")
# The file questions.txt must be in the same folder of this program.
# The file questions.txt must have ONE question per line.

""" This program ask you random question from a txt you've created before. 
In this way you can bone up for you're exam ;)"""

import argparse
import random

parser = argparse.ArgumentParser(description="Bone up for your exam")
parser.add_argument('file', type=argparse.FileType('r'),
                    help="questions file")
args = parser.parse_args()
print(random.choice(list(args.file)).rstrip())
