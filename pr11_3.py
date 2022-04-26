from ast import increment_lineno


class employee:
    salary=1000
    increment=1.5
    @property
    def sai(self):
        return self.salary*self.increment
    @sai.setter
    def sai(self,saai):
        self.increment=self.saai/self.salary
e=employee()
print(e.sai)