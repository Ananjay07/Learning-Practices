#Data hiding - a technique used to prevent direct access to an object's internal data
class myclass:
    def __init__(self):
        self.hidden_var = 0
    def get_hidden_var(self):
        return self.hidden_var
    def set_hidden_var(self,value):
        self.hidden_var = value

v1 = myclass()
v1.set_hidden_var(25)
print(v1.get_hidden_var())