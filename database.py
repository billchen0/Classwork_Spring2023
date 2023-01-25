print('This is the database.py file')
print(f'Python think this is called {__name__}')

from blood_calculator import HDL_analysis, HDL_input

HDL = 55

HDL_analysis = HDL_analysis(HDL)

print(f'The HDL analysis is {HDL_analysis}')

HDL_input('Other Test')

