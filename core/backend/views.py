# from django.shortcuts import render

from ativ.aquisition import GetData

get_data = GetData()
rec = get_data.from_pdb('1a0a')
print(rec)
