import pytest

from django.contrib.auth.models import User

@pytest.mark.django_db  #to gain access to the database 
def test_user_create():
  User.objects.create_user('nexhi1', 'sulanexhi@gmail.com', 'nexhi1993')
  assert User.objects.count() == 1