import csv 
import pyodbc
import os.path


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=TP2019\SQLEXPRESS;'
                      'Database=Testing DB;'
                      'UID=quote;'
                      'PWD=quote;'
                      'Trusted_Connection=no;')                     

while True:    
    quote_number = input("Enter quote number you wish to change pricing on. \n")
    try:
        quote_number=int(quote_number)
    except:
        print('Please use numaric digits.')
        continue
    if quote_number < 1000:
        print('Please enter a postive number that is at least 4 digits.')
        continue
    break

while True:
    csv_name = input("Please enter correct csv file name and press enter. \n")    
    if not os.path.exists(csv_name):   
        print('File does not exist.')
        continue
    break

while True:
    sell_margin = input("Pleave enter pricing margin percent and press enter. \n")
    try:
        sell_margin=int(sell_margin)
    except:
        print('Please use numaric digits.')
        continue
    if sell_margin < 1:
        print('Please enter a postive number.')
        continue
    break


input_file = csv.DictReader(open(csv_name))
print('\nPlease check all in data input from csv file.')
input('Press enter to show input data. \n')
for column in input_file:
    print(column['em'], column['cost'])

input('Press enter to continue. \n')

cursor = conn.cursor()
input_file = csv.DictReader(open(csv_name))
for column in input_file:
    em_numb = column['em']
    cost = float(column['cost'])
    selling_price = float(cost*sell_margin)
    cursor.execute('Select [Quantity] FROM [Tigerpaw].[dbo].[tblQuoteDetail] Where QuoteNumber = ' + str(quote_number) )
    quantity = cursor.fetchall()
    print("%s, %s, %s" % (cost, selling_price, quantity ))

    #cursor.execute('update dbo.tblQuoteDetail Set Cost = ' + column['cost'] + ', SellingPrice = ' + int(column['cost']) * sell_margin)
#query = cursor.fetchall()
#results = []

#print(query)