from django.contrib import admin

# Register your models here.
from .models import Post        # Importing Model 

admin.site.register(Post)       # Registering Model To CRUD in Admin Site 
