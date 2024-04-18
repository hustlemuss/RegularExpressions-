from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re
with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
def format_phone(phone):
  # Паттерн для извлечения номера телефона и дополнительного номера
  phone_pattern = r'(\+?\d{1,2})?[\s\(\)-]*(\d{3})[\s\(\)-]*(\d{3})[\s\(\)-]*(\d{2})[\s\(\)-]*(\d{2})[\s\(\)-]*доб\.\s*(\d+)?'
  match = re.match(phone_pattern, phone)
  if match:
    groups = match.groups()
    # Форматирование номера телефона
    formatted_phone = f"+7({groups[1]}){groups[2]}-{groups[3]}-{groups[4]}"
    # Добавление дополнительного номера, если есть
    if groups[5]:
      formatted_phone += f" доб.{groups[5]}"
    return formatted_phone
  else:
    return None


def process_contacts(contacts):
  processed_contacts = {}
  for contact in contacts:
    # Извлечение Фамилии, Имени и Отчества
    fullname = contact[0].split()
    lastname = fullname[0]
    firstname = fullname[1] if len(fullname) > 1 else ''
    surname = ' '.join(fullname[2:]) if len(fullname) > 2 else ''

    # Форматирование номера телефона
    contact[5] = format_phone(contact[5])

    # Создание ключа на основе ФИО и добавление контакта в словарь
    key = (lastname, firstname, surname)
    if key in processed_contacts:
      # Объединение контактов, оставляя уникальные значения
      existing_contact = processed_contacts[key]
      processed_contacts[key] = list(set(existing_contact + contact))
    else:
      processed_contacts[key] = contact

  return list(processed_contacts.values())




def main():
  # Чтение адресной книги из CSV файла
  with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

  # Обработка контактов
  processed_contacts = process_contacts(contacts_list)

  # Сохранение обработанных данных в другой файл CSV
  with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(processed_contacts)


if __name__ == "__main__":
  main()

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(contacts_list)