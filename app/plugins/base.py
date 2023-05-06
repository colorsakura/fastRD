class BaseSite:
    safetime = 5   # 访问间隔时间 second
    lasttime = 0    # 上一期访问时间 second

    def __init__(self) -> None:
        self.site = None
        self.sitename = None

    def request(self):
        pass

    def search(self, keyword: str):
        """搜索书籍
        """
        pass

    def detail(self, bid: int):
        """获取书籍详细信息
        bid: book id
        """
        pass


class Book:
    name = None

    def __init__(self):
        pass
    