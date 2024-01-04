from django.contrib import admin
from siswa.models import Siswa, SiswaKelas, PresensiSiswa, ArsipSiswaKelas, PresensiSiswaHarian


@admin.register(Siswa)
class SiswaAdmin(admin.ModelAdmin):
    pass


@admin.register(SiswaKelas)
class SiswaKelasAdmin(admin.ModelAdmin):
    pass


@admin.register(PresensiSiswa)
class PresensiSiswaAdmin(admin.ModelAdmin):
    pass


@admin.register(ArsipSiswaKelas)
class ArsipSiswaAdmin(admin.ModelAdmin):
    pass


@admin.register(PresensiSiswaHarian)
class PresensiSiswaHarianAdmin(admin.ModelAdmin):
    pass
