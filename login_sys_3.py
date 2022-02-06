class Account:
    func_list = ["login", "logout", "register"]

    def login(self):
        print("login")

    def logout(self):
        print("logout")

    def register(self):
        print("register")

    def run(self):
        while True:
            print("""
                Please choose the following menu options:
                    1. login
                    2. logout
                    3. register
            """)
            choice = int(input("Please put the number:"))
            func_name = Account.func_list[choice - 1]
            func = getattr(self, func_name)
            func()


obj = Account()
obj.run()
