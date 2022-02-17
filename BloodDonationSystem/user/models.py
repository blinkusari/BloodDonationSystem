from django.db import models
from django.contrib.auth.models import User
from abc import ABC, abstractmethod

class UserFactory(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_surname(self):
        pass

    @abstractmethod
    def get_age(self):
        pass
    