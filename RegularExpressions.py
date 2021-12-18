import re
import csv


file_name = "phonebook_raw.csv"


with open(file_name, encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)



# 1. поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно.
# В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О
def format_name(contacts_list):
    name_pattern = r"^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)"
    name_pattern_new = r"\1\3\10\4\6\9\7\8"
    contacts_list_updated = []
    for info in contacts_list:
        info_string = ','.join(info)
        res = re.sub(name_pattern, name_pattern_new, info_string)
        info_list = res.split(',')
        contacts_list_updated.append(info_list)
    return contacts_list_updated


# 2. привести все телефоны в формат +7(999)999-99-99.
# Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999
def format_phone(first_update):
    phone_pattern = r"(\+7|8)?(\s)?(\()?(\d{3})(\))?(\s|-)?(\d{3})(\s|-)?" \
                    r"(\d{2})(\s|-)?(\d+)((\s)?(\()?(доб)*(\.)\s(\d+)(\))?)?"
    phone_pattern_new = r"+7(\4)\7-\9-\11 \15\16\17"
    contacts_list_updated = []
    for info in first_update:
        info_string = ','.join(info)
        res = re.sub(phone_pattern, phone_pattern_new, info_string)
        info_list = res.split(',')
        contacts_list_updated.append(info_list)
    return contacts_list_updated


first_update = format_name(contacts_list)
second_update = format_phone(first_update)


# 3. объединить все дублирующиеся записи о человеке в одну.

final_list = []
final_list.append(second_update[0])
for string in second_update[1:]:
    for string2 in final_list:
        if string[0] == string2[0] and string[1] == string2[1] and string is not string2:
            if string2[2] == '':
                string2[2] = string[2]
            if string2[3] == '':
                string2[3] = string[3]
            if string2[4] == '':
                string2[4] = string[4]
            if string2[5] == '':
                string2[5] = string[5]
            if string2[6] == '':
                string2[6] = string[6]
                break
    else:
        final_list.append(string)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV

with open("phonebook.csv", "w",encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(final_list)