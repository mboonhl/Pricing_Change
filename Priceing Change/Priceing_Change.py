import csv 
import pyodbc
import os.path


conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=TP2019\SQLEXPRESS;'
                      'Database=Testing DB;'
                      'UID=pricing;'
                      'PWD=pricing;'
                      'Trusted_Connection=no;')                     

while True:    
    quote_number = input("Enter quote number you wish to change pricing on. \n")
    quote_number = 4036
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
    csv_name = 'test.csv'
    if not os.path.exists(csv_name):   
        print('File does not exist.')
        continue
    break

while True:
    sell_margin = input("Pleave enter pricing margin percent and press enter. \n")
    sell_margin = 20
    try:
        sell_margin=int(sell_margin)
    except:
        print('Please use numaric digits.')
        continue
    if sell_margin < 1:
        print('Please enter a postive number.')
        continue
    break
sell_margin = (sell_margin/100)+1

input_file = csv.DictReader(open(csv_name))
print('\nPlease check all in data input from csv file.')
input('Press enter to show input data. \n')
for column in input_file:
    print(column['EM#'], column['Cost'])

input('Press enter to continue. \n')

cursor = conn.cursor()
input_file = csv.DictReader(open(csv_name))
for column in input_file:
    em_numb = column['EM#']
    cost = float(column['Cost'])
    selling_price = float(cost*sell_margin)
    cursor.execute("update dbo.tblQuoteDetail Set Cost = " + str(cost) + " , SellingPrice = " + str(selling_price) + " , TotalSellingPrice = (" + str(selling_price) + "*Quantity)" + 
                  " , TotalCost = (" + str(cost) + "*Quantity)" + "Where QuoteNumber = " + str(quote_number) + " and ItemID = '" + em_numb + "'" )
    cursor.commit()
    
    cursor.execute("Select [ItemID], [Quantity], [Cost], [SellingPrice], [TotalSellingPrice], [TotalCost] FROM [Testing DB].[dbo].[tblQuoteDetail] Where QuoteNumber = " + str(quote_number) + " and ItemID = '" + em_numb + "'" )
    quantity = cursor.fetchone()
    print(quantity)

input_file = csv.DictReader(open(csv_name))
for column in input_file:
    em_numb = column['EM#']
    cost = float(column['Cost'])
    selling_price = float(cost*sell_margin)
    cursor.execute("update dbo.tblQuoteAssemblyDetail Set Cost = " + str(cost) + " , SellingPrice = " + str(selling_price) + " , TotalSellingPrice = (" + str(selling_price) + "*Quantity)" + 
                  " , TotalCost = (" + str(cost) + "*Quantity)" + "Where QuoteNumber = " + str(quote_number) + " and ItemID = '" + em_numb + "'" )
    cursor.commit()
    
    cursor.execute("Select [ItemID], [Quantity], [Cost], [SellingPrice], [TotalSellingPrice], [TotalCost] FROM [Testing DB].[dbo].[tblQuoteAssemblyDetail] Where QuoteNumber = " + str(quote_number) + " and ItemID = '" + em_numb + "'" )
    quantity = cursor.fetchone()
    print(quantity)
   