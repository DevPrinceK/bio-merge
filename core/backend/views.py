# from django.shortcuts import render

from ativ.aquisition import GetData

# get data from pdb
get_data_from_pdb = GetData()
rec = get_data_from_pdb.from_pdb('1a0a')
print(rec)


