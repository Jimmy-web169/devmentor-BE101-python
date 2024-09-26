# User class
class User:
    id:str
    email:str
    phone:str
    prefers_language:str    
    def __init__(self, id: str, email: str, phone: str, prefers_language: str):

        self.id = id
        self.email = email
        self.phone = phone
        self.prefers_language = prefers_language



class Student(User):
    def __init__(self, id: str, email: str, phone: str, prefers_language: str):
        super().__init__(id, email, phone, prefers_language)


