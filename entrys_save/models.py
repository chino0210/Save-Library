from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager

# Model user
class MyUser(AbstractBaseUser):
  name = models.CharField(max_length=255)
  document_type = models.CharField(max_length=100)
  document_number = models.CharField(max_length=100, unique=True)
  email = models.EmailField(unique=True)
  status = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)
  is_active = models.BooleanField(default=True)

  objects = UserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  class Meta:
    db_table = 'users'

  def __str__(self) -> str:
    return self.email

class EntryModel (models.Model):
  id = models.AutoField (primary_key=True)
  name = models.CharField(max_length=100)
  autor = models.CharField(max_length=100)
  description = models.TextField()
  times_saved = models.IntegerField(default=0)
  likes = models.IntegerField(default=0)
  document = CloudinaryField("documento",resource_type="auto")
  status = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = 'entrys'

  def __str__(self) -> str:
    return self.name

class LibraryModel (models.Model):
  id = models.AutoField(primary_key=True)
  user_id = models.ForeignKey(MyUser, on_delete=models.CASCADE)
  status = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = 'library'

  def __str__(self) -> str:
    return self.id

class LibraryDetailModel (models.Model):
  id = models.AutoField(primary_key=True)
  entry_id = models.ForeignKey(EntryModel, on_delete=models.CASCADE)
  status_saved = models.BooleanField(default=True)
  library_id = models.ForeignKey(LibraryModel, on_delete=models.CASCADE, related_name='libraryDetails')

  class Meta:
    db_table = 'library_details'

  def __str__(self) -> str:
    return self.id