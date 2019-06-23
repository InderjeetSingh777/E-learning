from django.db import models

# Create your models here.
from django.contrib.auth.models import(AbstractBaseUser,BaseUserManager)


class UserManager(BaseUserManager):
    def create_user(self,username,full_name,password=None,active=True,is_staff=False,is_admin=False):
        if not username:
            raise ValueError("User must have a username")
        if not password:
            raise ValueError("User must have a password")

        user_obj=self.model(username=username)
        user_obj.set_password(password)#change user password
        user_obj.full_name=full_name
        user_obj.staff=is_staff
        user_obj.admin=is_admin
        user_obj.active=active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self,username,full_name,password=None):
        user=self.create_user(username,full_name,password=password,is_staff=True)
        return user

    def create_superuser(self,username,full_name,password=None):
        user=self.create_user(username,full_name,password=password,is_staff=True,is_admin=True)
        return user

class User(AbstractBaseUser):
    username=models.CharField(max_length=255,unique=True)
    full_name=models.CharField(max_length=255,blank=False,null=False)
    role=models.CharField(max_length=20,default='Student')
    active=models.BooleanField(default=True)#can login
    staff=models.BooleanField(default=False)#staff user non-superuser
    admin=models.BooleanField(default=False)
    #username and password are required by default
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['full_name']

    objects = UserManager()
    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.username

    def get_role(self):
        return self.role

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True
    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active



    
    