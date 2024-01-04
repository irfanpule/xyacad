from django.contrib import admin
from akademik.models import (
    TahunAkademik, Tingkat, Kurikulum, KelompokMapel, MataPelajaran, Jadwal
)


@admin.register(TahunAkademik)
class AdminTahunAkademik(admin.ModelAdmin):
    pass


@admin.register(Tingkat)
class AdminTingkat(admin.ModelAdmin):
    pass


@admin.register(Kurikulum)
class AdminKurikulum(admin.ModelAdmin):
    pass


@admin.register(KelompokMapel)
class AdminKelompokMapel(admin.ModelAdmin):
    pass


@admin.register(MataPelajaran)
class AdminMataPelajaran(admin.ModelAdmin):
    pass


@admin.register(Jadwal)
class AdminJadwal(admin.ModelAdmin):
    pass
