class UserInfo:
    def __init__(self):
        self.name = None

    def info(self):
        print(f"Current user is : {self.name}")

    def account(self):
        pass

    def shopping(self):
        pass

    def login(self):
        username = input("Please put your username")
        pwd = input("Please put your password")
        if username == "jim" and pwd == "1234":
            self.name = username
            while True:
                print("""
                    1. View user information
                    2. View user account
                    3. Purchase history
                """)
                num = int(input("Please put a number"))
                if num == 1:
                    self.info()
                elif num == 2:
                    self.account()
                elif num == 3:
                    self.shopping()
                else:
                    print("Input number is not correct. Please re-inter")

        else:
            print("Access Denied")


obj = UserInfo()
obj.login()
