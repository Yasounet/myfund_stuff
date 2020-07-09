import datetime

input_data = """
"""

mi_list = ['XBLC', 'XXSC', 'XSX6']

data = input_data.split("\n")
result = ''

for row in data:
    values = row.split("\t") #split rows into list of values
    new_date = datetime.datetime.strptime(values[0], "%d.%m.%Y").strftime("%Y-%m-%d") #change date format to YYYY-MM-DD
    
    ticker = values[-1]
    
    ticker = ticker.replace("GR","MI") if ticker.split('.')[0] in mi_list else ticker.replace("GR", "DE") #change ticker to one tracked by myfund
    ticker = 'BORSE_' + ticker #add internal myfund prefix 
    
    bos = "KUPNO" if values[1] == 'Zakup' else "SPRZEDAŻ" #determine type of transaction
    amount = values[2] #extract transaction amount
    price = values[3].replace("€", "[EUR]") #extract price and use proper currency notation
    new_list = [new_date, ticker, bos, amount, price, "0", "0"] #create new list
    new_row = ";".join(new_list) + "\n" #format list into single csv row
    result += new_row #add row to results
    
print(result)