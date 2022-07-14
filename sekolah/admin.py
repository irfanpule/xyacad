from django.contrib import admin
from sekolah.models import Sekolah, Gedung, Ruangan, Jurusan, Kelas


class AdminSekolah(admin.ModelAdmin):
    pass


class AdminGedung(admin.ModelAdmin):
    pass


class AdminRuangan(admin.ModelAdmin):
    pass


class AdminJurusan(admin.ModelAdmin):
    pass


class AdminKelas(admin.ModelAdmin):
    pass


admin.site.register(Sekolah, AdminSekolah)
admin.site.register(Gedung, AdminGedung)
admin.site.register(Ruangan, AdminRuangan)
admin.site.register(Jurusan, AdminJurusan)
admin.site.register(Kelas, AdminKelas)
