# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 21:50:56 2020

@author: natal
"""
import pandas as pd
from matplotlib import pyplot as plt

ID1 = 'Jonas'
# ID2 = 'Ferre'
# ID3 = 'Bla'
# ID4 = 'Blabla'

lijst = [0.8
         ]

plotdata = pd.DataFrame({"score": lijst}, index = [ID1])
plotdata.plot(kind = "bar")

