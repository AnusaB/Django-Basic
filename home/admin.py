from django.contrib import admin
from home.models import Contact,Books, Author

# Register your models here.

admin.site.register(Books)
admin.site.register(Author)
admin.site.register(Contact)