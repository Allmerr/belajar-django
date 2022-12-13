from django.db import models

# Create your models here.
class Keterangan(models.Model):
    nama = models.CharField(max_length=50)
    keterangan = models.TextField()

    def __str__(self):
        return self.nama

    def __unicode__(self):
        return self.nama


class Buku(models.Model):
    judul =  models.CharField(max_length=50)
    penulis = models.CharField(max_length=40)
    penerbit = models.CharField(max_length=40)
    jumlah = models.IntegerField(null=True)
    keterangan = models.ForeignKey("Keterangan", on_delete=models.CASCADE,null=True)
    cover = models.ImageField(upload_to='cover',null=True)
    tanggal = models.DateTimeField(auto_now_add=True,null=True)    

    def __str__(self):
        return self.judul

    def __unicode__(self):
        return self.judul

