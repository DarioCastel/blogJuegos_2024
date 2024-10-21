from django.db import models

from django.contrib.auth.models import AbstractUser, User

# Create your models here.



    




class Posts(models.Model):  # nombreapp_nombreclase
    titulo = models.CharField(
        max_length=250, null=False, blank=False, verbose_name="Titulo"
    )
    contenido = models.TextField(verbose_name="Contenido")
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to="media/posts", null=True, blank=True)




# class Imagenes(models.Model):
#     imagen = models.ImageField(upload_to="/media/Posts")
#     post = models.ForeignKey(Posts, on_delete=models.CASCADE)


