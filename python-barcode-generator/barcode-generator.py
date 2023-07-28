# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 07:04:59 2023

@author: IdrisIbrahimERTEN
"""

from barcode import EAN13

from barcode.writer import ImageWriter

number = '120120120120120'
my_code = EAN13(number, writer=ImageWriter())

my_code.save("newcode1")