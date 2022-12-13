from django.contrib import admin

from perpustakaan.models import Buku,Keterangan

# Register your models here.

@admin.register(Buku)
class BukuAdmin(admin.ModelAdmin):
    list_display = ['judul','penulis','penerbit', 'jumlah', 'keterangan']
    search_fields = ['judul', 'penulis', 'penerbit']
    list_filter = ('keterangan',)
    list_per_page = 4



admin.site.register(Keterangan)

