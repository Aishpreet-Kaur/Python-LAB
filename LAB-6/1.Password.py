class PasswordManager:
    def __init__(self):
        self.__password = None

    def set_password(self,password):
        if isinstance(password,str) and len(password)>=8:
            self.__password = password
            print("Password is Set")
        else:
            print("ERROR! Password should contain atleast 8 charactes")  

    def get_password(self):
        if self.__password:
            return self.__password
        else:
            return "No password set"          
        
student_id = PasswordManager()
student_id.set_password("login@123")

print("password: ",student_id.get_password())
