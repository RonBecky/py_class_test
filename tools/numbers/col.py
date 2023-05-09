"""
this is col.py here i colide the first list and the
second list into one list that creats my friends names
"""

listFNames = ['Ron', 'Rachel', 'Snir'] # a list of first names
listLNames = ['Bekerman', 'Tinkov', 'Ezer'] # a list of last names 
zipped_list = zip(listFNames, listLNames) # colliding them into full names
for a, b in zipped_list:
    print(f"{a}_{b}", end=",") #changing the appirence of the two lists to my liking
