import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

HEADER = 0

def init(Sheet_name, Sheet_number = 0):
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

    client = gspread.authorize(creds)

    if(Sheet_number == 0):
        sheet = client.open(Sheet_name).sheet1  # Open the spreadhseet
    elif(Sheet_number == 1):
        sheet = client.open(Sheet_name).sheet2  # Open the spreadhseet 2
    elif(Sheet_number == 2):
        sheet = client.open(Sheet_name).sheet3  # Open the spreadhseet 3
    else:
        sheet = client.open(Sheet_name).sheet4  # Open the spreadhseet 3

    data = sheet.get_all_records()  # Get a list of all records
    return data, sheet

def get_value(sheet,row=-1,col=-1):
    if(row + col == -2): return None

    elif( (row != -1) and (col == -1) ):
        return sheet.row_values(row)

    elif( (row == -1) and (col != -1) ):
        return sheet.col_values(col)

    else:
        return sheet.cell(row,col).value

def update_value(sheet,row,col,value):
    return sheet.update_cell(row,col, value) 

def value(sheet,row=-1,col=-1,val=None):
    if(val == None):
        return get_value(sheet,row,col)

    if( (row != -1) and (col != -1) ):
        return update_value(sheet,row,col,val)


def header(sheet):
    return value(sheet,row=1)

def number_lines(data):
    return len(data)

def number_columns(sheet):
    return len(header(sheet))

def table(sheet,data):
    return [ value(sheet,row = line) for line in range(1,number_lines(data)+2) ]

def filterWith(table,f):
    return list(filter(f,table))

def enumerate_swap(l):
    return list( map( lambda x: (x[1],x[0]),enumerate(l) ) )


def filter_atribute_val(table,atribute,value):
    atribute_ind =  dict(enumerate_swap( table[HEADER] ))[atribute]  
    func = lambda line : line[atribute_ind] == value
    return filterWith(table,func)



