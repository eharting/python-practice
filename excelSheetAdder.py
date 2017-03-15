#Creates and renames new sheets in Excel

import openpyxl, os
os.chdir('C:\\Users\\HartingE\\Desktop\\Park Potomac')

# this code creates sheets for Book1
file = 'Book1.xlsx'
wb = openpyxl.load_workbook(file)
sheets = ['SCU1N', 'SCU2N', 'SCU3N', 'SCU4N', 'SCU5N', 'SCU6N', 
			'SCU7N', 'SCU8N', 'SCU9N', 'SCU10N', 'SCU11N', 'SCU12N', 
			'SCU1S', 'SCU2S', 'SCU3S', 'SCU4S', 'SCU5S', 'SCU6S', 
			'SCU7S', 'SCU8S', 'SCU9S', 'SCU10S', 'SCU11S', 'SCU12S']

for i in range(len(sheets)):
	wb.create_sheet(index=i, title=sheets[i])

wb.save(file)
