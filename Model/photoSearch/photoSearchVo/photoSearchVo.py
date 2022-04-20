
class photoSearchVo:

    __no = ''
    __name = ''

    def __init__(self, CSP_dict):
        self.__no = CSP_dict['no']
        self.__name = CSP_dict['name']

    def __del__(self):
        print(self, ' 인스턴스 소멸됨.')

    def getno(self):
        return self.no;
    def getname(self):
        return self.name;

    def setno(self,no):
        self.no = no;
    def setname(self,name):
        self.name = name;

    def __str__(self):
        return '{} {}'.format(self.no, self.name)

