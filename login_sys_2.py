# User register, login, checking

class User:
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd


class Account:
    def __init__(self):
        self.user_list = []

    def register(self):
        i = 0
        while i < 3:
            i += 1
            username = input("What is your username?")
            password = input("What is your password?")
            user = User(username, password)
            self.user_list.append(user)

    def login(self):
        for row in self.user_list:
            flag = False
            i = 0
            while i < 3:
                i += 1
                user_name = input("Please put your username?")
                pass_word = input("Please put your password?")
                if row.name == user_name and row.pwd == pass_word:
                    flag = True
                    break
            if flag:
                print("Access Granted")
            else:
                print("Access denied")

    def run(self):
        self.register()
        self.login()


if __name__ == "__main__":
    obj = Account()
    obj.run()
