from django.contrib import admin
from pegawai.models import (
    Golongan, JenisPTK, StatusPegawai, JabatanStruktural, JabatanFungsional,
    Pegawai
)


class AdminGolongan(admin.ModelAdmin):
    pass


class AdminJenisPTK(admin.ModelAdmin):
    pass


class AdminStatus(admin.ModelAdmin):
    pass


class AdminStruktural(admin.ModelAdmin):
    pass


class AdminFungsional(admin.ModelAdmin):
    pass


class AdminPegawai(admin.ModelAdmin):
    pass


admin.site.register(Golongan, AdminGolongan)
admin.site.register(JenisPTK, AdminJenisPTK)
admin.site.register(StatusPegawai, AdminStatus)
admin.site.register(JabatanStruktural, AdminStruktural)
admin.site.register(JabatanFungsional, AdminFungsional)
admin.site.register(Pegawai, AdminPegawai)
