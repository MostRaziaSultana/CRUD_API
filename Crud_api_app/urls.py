from django.urls import path
from .views import *

urlpatterns = [
    path('save_data/', add_profile),
    path('see_profile/', see_profile),
    path('del_prof/<int:id>/', del_prof),
    path('update_prof/<int:id>/', update_prof),
]







#--------------Documentation-----------------

# http://127.0.0.1:8000/save_data/ <POST> ------------ save data in database API


# Data format to save :
#  {
#   "f_name": "razia",
#  "l_name": "sultana",
#  "name": "arhamrahman",
#  "email": "arham@gmail.com",
#  "phone_number": "01522334567"
#  }


# http://127.0.0.1:8000/see_profile/ <GET> ----------- show data from database in API

# http://127.0.0.1:8000/del_prof/id/ ------------------ delete data from database where id must be profile id

# http://127.0.0.1:8000/update_prof/2/ ----------------- update data from database

#--------------Documentation-----------------

