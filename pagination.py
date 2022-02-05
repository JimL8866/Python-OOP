class Pagination:
    """
    code for deal with pagination
    """
    def __init__(self, data_list, page, per_page_num=10):
        """
        define object attribute
        :param data_list: data for pagination
        :param page: current page user want to check
        :param per_page_num: how many items per page
        """
        self.data_list = data_list
        self.page = page
        self.per_page_num = per_page_num

    def start(self):
        """
        calculate starting index in data_list
        :return:
        """
        return (self.page - 1) * self.per_page_num

    def end(self):
        """
        calculate end index in data_list
        :return:
        """
        return self.page * self.per_page_num

    def show(self):
        """
        show content in a page
        :return:
        """
        page_content = self.data_list[self.start():self.end()]
        for row in page_content:
            print(row)


my_num_list = []
for i in range(1, 1001):
    my_num_list.append(f"my number list is {i}")

while True:
    user_page = int(input("which page do you want to see?"))
    pagination = Pagination(my_num_list, user_page)
    pagination.show()


class Pagination:
    def __init__(self, page, per_page_num=10):
        self.page = page
        self.per_page_num = per_page_num

    @property
    def start(self):
        return (self.page - 1) * self.per_page_num

    @property
    def end(self):
        return self.page * self.per_page_num


my_num_list = []
for i in range(1, 1001):
    my_num_list.append(f"my number list is {i}")

while True:
    user_page = int(input("which page do you want to see?"))
    pagination = Pagination(user_page)
    page_content = my_num_list[pagination.start:pagination.end]
    for row in page_content:
        print(row)


