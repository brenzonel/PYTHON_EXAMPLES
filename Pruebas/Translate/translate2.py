import pandas as pd
from googletrans import Translator
from openpyxl import load_workbook, Workbook

translator = Translator()

def translateToEnglish(text):
    translated = translator.translate(text, src="es", dest="en")
    #print('Input Text:', text)
    #print('Translated Text:', translated.text)
    return translated.text

def translateToSpanish(text):
    translated = translator.translate(text, src="en", dest="es")
    #print('Input Text:', text)
    #print('Translated Text:', translated.text)
    return translated.text

try: 
    #df = pd.read_excel('Pruebas_traduccion.xlsx')
    #df = pd.read_csv('Pruebas_traduccion.csv')
    #print(df[:2])
    #df['A_Eng'] = df['A'].apply(translateToinglish)
    #dfl = df.applymap(translateToinglish)
    #dfl.to_excel('Translated_Data1.xlsx', index=False)
    filename = "c:/Users/brana/Desktop/Python/documentos_pruebas/Pruebas_traduccion.xlsx"
    destinationfile = "c:/Users/brana/Desktop/Python/documentos_pruebas/Pruebas_traduccion2.xlsx"

    # Load the source Excel file
    source_wb = load_workbook(filename)
    #workbook = load_workbook(filename="csv/Email_sample.xlsx")
    source_ws = source_wb.active

    # Create a new Excel file
    destination_wb = load_workbook(filename)
    destination_ws = destination_wb.active
    # Copy data from source to destination
    #destination_ws.delete_cols(1)
    destination_ws.delete_rows(1,source_ws.max_row)
    #print('Rows1:', destination_ws.max_row)
    #print('Rows1:', source_ws.max_row)
    #destination_ws.create_sheet('Translated')
    #i=1
    messages=[]
    for row in source_ws.iter_rows(min_row=1, max_row=source_ws.max_row, values_only=True):
        if row[0] == '':
            destination_ws.append({1:row[0],2:'No message'}) #Empty cell
        else:
            destination_ws.append({1:row[0],2:translateToEnglish(row[0])})
        #destination_ws.append({1:row[0],2:translateToEnglish(row[0])})
        #destination_ws.append({1:translateToinglish(row[0])})
        #print(row[0])
    #print('Rows2:', destination_ws.max_row)
    #print('Rows2:', source_ws.max_row)
    '''
    for i in range(len(messages)):
        if messages[i] == '':
            messages[i] = 'No message'

    destination_ws.delete_cols(1, source_ws.max_row)
    for i in range(len(messages)):
        destination_ws.append({1:messages[i], 2:translateToEnglish(messages[i])})
    '''

    # Save the destination file
    destination_wb.save(destinationfile)
    #print('Rows:', sheet_new.max_row)
    #print('Columns:', sheet_new.max_column)
    #print('Data:', sheet_new['A3'].value)
    #print('Data Translate:', translateToinglish(sheet_new['A3'].value))
    #source_wb.save('Pruebas_traduccion2.xlsx')
    destination_wb.close()
    source_wb.close()
    print('Translation complete!')

except Exception as e:
    destination_wb.close()
    source_wb.close()
    print('An error ocurred:', e)
    print('Translation failed!')

