from django.http import HttpResponse
from django.shortcuts import redirect, render
from perpustakaan.models import Buku,Keterangan
from perpustakaan.form import FormBuku
from django.contrib import messages
from perpus.settings import LOGIN_URL
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Berhasil Membuat akun')
            return redirect('/signup/')
        else:
            messages.error(request, 'Gagal Mendafatar')
            return redirect('/signup/')
    else :
        konteks = {
            'form' : UserCreationForm()
        }
        return render(request,'signup.html',konteks)
    



@login_required(login_url=LOGIN_URL)
def penulis(request):
    konteks = {
        "page" : "penulis"
    }
    return render(request, 'penulis.html' ,konteks)

@login_required(login_url=LOGIN_URL)
def buku(request):
    buku_buku = Buku.objects.all()
    keterangan_keterangan = Keterangan.objects.all()

    buku_search = request.GET.get('buku')
    keterangan_search = request.GET.get('kategori')
    if buku_search:
        buku_buku = Buku.objects.filter(judul__icontains=buku_search)
    elif keterangan_search:
        buku_buku = Buku.objects.filter(keterangan=keterangan_search)
        

    konteks = {
        "page" : "buku",
        "buku_buku" : buku_buku ,
        "keterangan_keterangan" : keterangan_keterangan

    }
    return render(request,'buku.html', konteks)

@login_required(login_url=LOGIN_URL)
def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            form = FormBuku()
            konteks = {
                "pesan" : "Data Berhasil Tersimpan",
                "page" : "tambah-buku",
                "form" : form
            }
    else :
        form = FormBuku
        konteks = {
            "page" : "tambah-buku",
            "form" : form
        }

    return render(request, 'tambah-buku.html', konteks)


@login_required(login_url=LOGIN_URL)
def ubah_buku(request,id_buku):
    buku = Buku.objects.get(id=id_buku)
    if request.POST:
        form = FormBuku(request.POST,request.FILES, instance=buku)
        if form.is_valid():
            form.save()
            messages.success(request,"Data berhasil di ubah")
            return redirect(f'/buku/ubah/{id_buku}',id_buku=buku)
    else :
        form = FormBuku(instance=buku)
        konteks = {
            'form' : form,
            'buku' : buku
        }
        return render(request,'ubah-buku.html', konteks)

@login_required(login_url=LOGIN_URL)
def hapus_baku(request,id_buku):
    buku = Buku.objects.filter(id = id_buku)
    buku.delete()
    messages.success(request,'Berhasil menghapus buku')
    return redirect('/buku/')