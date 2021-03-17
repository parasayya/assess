import pandas as pd
import sqlite3


'''
|H|Customer_Name|Customer_Id|Open_Date|Last_Consulted_Date|Vaccination_Id|Dr_Name|State|Country|DOB|Is_Active
|D|Alex|123457|20101012|20121013|MVD|Paul|SA|USA|06031987|A
|D|John|123458|20101012|20121013|MVD|Paul|TN|IND|06031987|A
|D|Mathew|123459|20101012|20121013|MVD|Paul|WAS|PHIL|06031987|A
|D|Matt|12345|20101012|20121013|MVD|Paul|BOS|NYC|06031987|A
|D|Jacob|1256|20101012|20121013|MVD|Paul|VIC|AU|06031987|A
'''
df = pd.read_csv('filename.ext', sep = '|',  engine = 'python') 
# like spark data frame
print(df.columns)

df2 = df[df.columns[2:]] # eliminates unnessary data

conn = sqlite3.connect('TestDB.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS Customer(Name VARCHAR(255), 
Customer_ID VARCHAR(18), Customer_Open_Date DATE,
		Last_Consulted_Date DATE,
		Vaccination_type varchar(5),
		Doctor_Consulted VARCHAR(255),
		State VARCHAR(5),
		Country VARCHAR(5),
		Post_Code INT,
		Date_of_Birth DATE,
		Active_Customer CHAR
 )
''')
conn.commit()

print(df2)

# we got data cleaned we can make now sql table from df2
'''
output
  Customer_Name  Customer_Id  Open_Date  Last_Consulted_Date Vaccination_Id Dr_Name State Country      DOB Is_Active
0          Alex       123457   20101012             20121013            MVD    Paul    SA     USA  6031987         A
1          John       123458   20101012             20121013            MVD    Paul    TN     IND  6031987         A
2        Mathew       123459   20101012             20121013            MVD    Paul   WAS    PHIL  6031987         A
3          Matt        12345   20101012             20121013            MVD    Paul   BOS     NYC  6031987         A
4         Jacob         1256   20101012             20121013            MVD    Paul   VIC      AU  6031987         A
'''

'''
alternativeyly we can i dentify and headers and rows using regex

like 
1. header = "^|H|.*\n"
2. row = "^|D|.*\n"
'''

df2.to_sql('Customer', conn, if_exists='replace', index = False)

countries = df2['Country']
#extracting countries

Query1 = " CREATE TABLE IF NOT EXISTS table_"
Query2 = " AS select * from Customer where country = "

for each in countries:
	query = Query1 + each + Query2 +'"'+ each +'" '+ ""
	# creating table for each country with respective data
	c.execute(query)
	conn.commit()
	

