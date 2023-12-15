from django.contrib import admin
from pegawai.models import (
    Golongan, JenisPTK, StatusPegawai, JabatanStruktural, JabatanFungsional,
    Pegawai, Presensi
)


@admin.register(Golongan)
class AdminGolongan(admin.ModelAdmin):
    pass


@admin.register(JenisPTK)
class AdminJenisPTK(admin.ModelAdmin):
    pass


@admin.register(StatusPegawai)
class AdminStatus(admin.ModelAdmin):
    pass


@admin.register(JabatanStruktural)
class AdminStruktural(admin.ModelAdmin):
    pass


@admin.register(JabatanFungsional)
class AdminFungsional(admin.ModelAdmin):
    pass


@admin.register(Pegawai)
class AdminPegawai(admin.ModelAdmin):
    pass


@admin.register(Presensi)
class PresensiAdmin(admin.ModelAdmin):
    pass
