class User:
    def __init__(self, first_name, last_name, phone_name):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_name = phone_name
    
    def contact(self):
        if self.first_name[0].isupper() and self.last_name[0].isupper():
            return True
        else:
            return False

    def phone(self):
        listt = []
        if self.phone_name[0] == '+':
            listt.append(True)
        if self.phone_name[4] == ' ':
            listt.append(True)
        if self.phone_name[7] == ' ':
            listt.append(True)
        if self.phone_name[11] == ' ':
            listt.append(True)
        if self.phone_name[14] == ' ':
            listt.append(True)
        if self.phone_name.count(' ') == 4:
            listt.append(True)
        if len(self.phone_name) == 17:
            listt.append(True)
        if all(x.isdigit() or x == '+' for x in self.phone_name.replace(' ','')):
            listt.append(True)
        if False not in listt:
            return True


test_answer = User("Mamarajabov", "Dilmurod", "+998 94 635 99 35")
