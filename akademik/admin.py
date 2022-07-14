from django.contrib import admin
from akademik.models import (
    TahunAkademik, Tingkat, Kurikulum, KelompokMalep, MataPelajaran
)


class AdminTahunAkademik(admin.ModelAdmin):
    pass


class AdminTingkat(admin.ModelAdmin):
    pass


class AdminKurikulum(admin.ModelAdmin):
    pass


class AdminKelompokMapel(admin.ModelAdmin):
    pass


class AdminMataPelajaran(admin.ModelAdmin):
    pass


admin.site.register(TahunAkademik, AdminTahunAkademik)
admin.site.register(Tingkat, AdminTingkat)
admin.site.register(Kurikulum, AdminKurikulum)
admin.site.register(KelompokMalep, AdminKelompokMapel)
admin.site.register(MataPelajaran, AdminMataPelajaran)
