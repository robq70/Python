
str = "Hello World!"
print(str);
print( len(str) )
print( type(str) )

print( str[ len(str) - 1 ] )

print( str[0:5] ) # Hello - jeśli damy 4 to wyświetli tylko Hell

print( str * 4 )

strX3 = str * 3
print(strX3)

str2 = str + " and Hello again!"
print(str2)

print(str2[6:]) # World! and Hello again! - od 6 do końca

print(str2[::3]) # HlWl deogn - co 3 literka ale z uwzględnieniem 1

multiLine = """Pierwsza linia
Druga linia
Trzecia linia
"""

print(multiLine)


multiLine2 = "Pierwsza linia\nDruga Linia\nTrzecia \t linia \" \\ "
print(multiLine2)