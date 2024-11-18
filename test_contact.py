from contact import User
import csv

test_contact = User("Mamarajabov", "Dilmurod", "+998 94 635 99 35")

def test_answer():
    assert test_contact.first_name[0].isupper(), "first_namening bosh harfini bosh harf bilan yozing"
    assert test_contact.last_name[0].isupper() , "last_namening bosh harfini bosh harf bilan yozing"
    assert test_contact.phone_name[0] == "+", "phone_nameni to'g'ri yozing"

def test_phone_name():
    assert test_contact.phone_name[0] == "+", "boshlanishiga '+' belgisini qo'ying"
    assert test_contact.phone_name[4] == ' ', "4-belgidan keyin boshliq bo'lishi kerak"
    assert test_contact.phone_name[7] == ' ', "7-belgidan keyin boshliq bo'lishi kerak"
    assert test_contact.phone_name[11] == ' ', "11-belgidan keyin boshliq bo'lishi kerak"
    assert test_contact.phone_name[14] == ' ', "14-belgidan keyin boshliq bo;lishi kerak"
    assert test_contact.phone_name.count(' ') == 4, "phone_nameda 4ta boshliq bo'lishi kerak"
    assert len(test_contact.phone_name) == 17, "phone_name 17ta belgidan oshmasligi va kam bo'lmasligi kerak"
    assert all(x.isdigit() or x == '+' for x in test_contact.phone_name.replace(' ', '')), "phone_name faqat '+' va raqamlarda iborat bo'lishi kerak"

    # a = 0
    # for x in test_contact.phone_name.replace(' ',''):
    #     if x.isdigit():
    #         a += 1
    # assert a - 1 == len(test_contact.phone_name.replace(' ','')), "phone_name faqat '+' va raqamlarda iborat bo'lishi kerak"

# with open('contacts.csv', mode='a', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow([test_contact.first_name, test_contact.last_name, test_contact.phone_name])


file = open ('contacts.csv', "a")
file.write(f"\n{test_contact.first_name},{test_contact.last_name},{test_contact.phone_name}")
file.close()