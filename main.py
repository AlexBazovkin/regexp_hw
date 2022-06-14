from pprint import pprint
import csv
import re

# читаем адресную книгу в формате CSV в список contacts_list
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# refactor last name, name, surname. PH#s standardization. Combine in one list.
raw_list = []
for data in contacts_list[1:]:
    clear_name = ' '.join(data[0:3])
    name = re.split(r'\W+', clear_name)
    phone_pattern = r"(\+7|8)\s*\(?(\d{3})\)?\s?-?(\d{3})\s?-?(\d{2})\s?-?(\d{2})\s?\(?([а-яёА-ЯЁ.]+)?\s?(\d+)?\)?"
    phone_replacement = r"+7(\2)\3-\4-\5 \6\7"
    phone = re.sub(phone_pattern, phone_replacement, data[-2])
    data_list_raw = [name[0], name[1], name[2], data[3], data[4], phone.strip(), data[6]]
    raw_list.append(data_list_raw)

# Combine duplicates.
for element in raw_list:
    last_name = element[0]
    name = element[1]
    for compare_element in raw_list:
        new_lastname = compare_element[0]
        new_name = compare_element[1]
        if last_name == new_lastname and new_name == name:
            if element[2] == "": element[2] = compare_element[2]
            if element[3] == "": element[3] = compare_element[3]
            if element[4] == "": element[4] = compare_element[4]
            if element[5] == "": element[5] = compare_element[5]
            if element[6] == "": element[6] = compare_element[6]

rebuilt_contact_list = []
for i in raw_list:
    if i not in rebuilt_contact_list:
        rebuilt_contact_list.append(i)
# pprint(rebuilt_contact_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(rebuilt_contact_list)