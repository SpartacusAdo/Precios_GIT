from django.db import models
from django.db.models.fields import CharField

from io import BytesIO
from PIL import Image
from django.core.files import File

#--------------------------------------------------------------------------------------------
class Categoria(models.Model):
        categoria=models.CharField(max_length=25, unique=True)
        slug = models.SlugField(max_length=255)
        orden = models.IntegerField(default=0)

        def __str__(self):
            return self.categoria

        class Meta():
            ordering = ['categoria']

#--------------------------------------------------------------------------------------------
class Color(models.Model):
        color=models.CharField(max_length=20, unique=True)

        def __str__(self):
            return self.color

        class Meta():
            ordering = ['color']
#----------------------------------------------------------------------------------
#https://www.youtube.com/watch?v=Rr1-UTFCuH4

def upload_to(instance, filename):
    return 'uploads/%s/%s' % (instance.categoria, filename)

class Bulbo(models.Model):
    codigo=CharField(max_length=10, unique=True)
    categoria=models.ForeignKey(Categoria, related_name='bulbos', on_delete=models.CASCADE)
    variedad=CharField(max_length=12)
    color=models.ForeignKey('color', on_delete=models.DO_NOTHING)
    size=CharField(max_length=10)
    creado_en=models.DateField(auto_now_add=True)
    modificado_en=models.DateField(auto_now=True)
    image = models.ImageField(upload_to=upload_to,blank=True, null=True)
    thumbnail = models.ImageField(upload_to=upload_to,blank=True, null=True)
    
    @property
    def bulbo(self):
        return "%s %s %s %s"%(self.categoria, self.variedad, self.color, self.size)

    class Meta():
        ordering = ['categoria', 'variedad', 'color', 'size']
        constraints = [models.UniqueConstraint(fields=['categoria', 'variedad', 'color', 'size'], name='articulo')]
        indexes = [
            models.Index(fields=['codigo']),
            models.Index(fields=['categoria', 'variedad', 'color', 'size'], name='bulbo'),]

    def __str__(self): 
        return self.bulbo

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail=self.make_thumbnail(self.image)
                self.save()
                return self.thumbnail.url
            else:
                return ('/amedia/uploads/placeholder.jpg')

    def make_thumbnail(self, image, size=(200, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
