# What's in the text file called list.txt:
# Helen: 1982
# Alex: 1933
# Martin: 1984
# Kate: 1986
# Alan: 1984
# Jane: 2001
# Jack: 1995
# Jessica: 2015

file1 = open("list.txt", "r")
newlist = [item[0:-1] for item in file1.readlines()]

strx = ""
list_of_years = []

for item in newlist:
    for letter in item:
        if letter.isdigit():
            strx += letter
            if len(strx) % 4 == 0:
                list_of_years.append(int(strx))
                strx = ""

oldest_year = min(list_of_years)
youngest_year = max(list_of_years)

counter = 0

while counter < len(list_of_years):
    for item in list_of_years:
        if item == oldest_year:
            index_of_oldest = counter
        elif item == youngest_year:
            index_of_youngest = counter
        counter += 1

hh = ""
names_list = []
for item in newlist:
    for letter in item:
        if letter == ":":
            names_list.append(hh)
            hh = ""
            break
        hh += letter

for number in list_of_years:
    ages_list = [(2024 - number) for number in list_of_years]

summ = 0
for number in ages_list:
    summ += number

print(
    f"The oldest person listed in the file is {names_list[index_of_oldest]}. They were born in {list_of_years[index_of_oldest]}. They are celebrating their {2024 - list_of_years[index_of_oldest]}. birthday in 2024!"
)

print(
    f"The youngest person listed in the file is {names_list[index_of_youngest]}. They were born in {list_of_years[index_of_youngest]}. They will be {2024 - list_of_years[index_of_youngest]} years old in 2024."
)

print(f"Average age of the people listed: {summ//len(ages_list)}")
