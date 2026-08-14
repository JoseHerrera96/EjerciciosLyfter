from abc import ABC, abstractmethod

class User(ABC):
    @abstractmethod
    def get_role(self):
        pass
    @abstractmethod
    def has_permission(self, permission):
        pass
   
class adminUser(User):
    def get_role(self):
        return "admin"
    def has_permission(self, permission):
        if permission == "read":
            return True
        elif permission == "write":
            return True
        elif permission == "delete":
            return True
            

class regularUser(User):
    def get_role(self):
        return "regular"
    def has_permission(self, permission):
        if permission == "read":
            return True
        elif permission == "write":
            return False
        elif permission == "delete":
            return False