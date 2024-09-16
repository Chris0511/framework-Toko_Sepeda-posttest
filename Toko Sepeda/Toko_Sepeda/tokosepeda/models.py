from django.db import models

class Sepeda(models.Model):
    nama = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    stok = models.IntegerField()
    deskripsi = models.TextField()
    gambar = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.nama