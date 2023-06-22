from django.contrib import admin

# Register your models here.
from administracion.models import Producto, Detalle_venta, Venta, Varietal,Bodega


# Registro por defecto al admin de Django
admin.site.register(Producto)
admin.site.register(Detalle_venta)
admin.site.register(Venta)
admin.site.register(Varietal)
admin.site.register(Bodega)

# Creacion de un Admin Personalizado heredando de AdminSite
# class ECPruebaAdminSite(admin.AdminSite):
#     site_header = 'Administracion ECPrueba'
#     site_title = 'Administracion superuser'
#     index_title= 'Administracion del sitio'
#     empty_value_display = 'No hay datos para visualizar'

# # Personalizacion de visualizacion de modelos en el Admin de Django
# class ProductoAdmin(admin.ModelAdmin):
#     list_display = ( 'nombre', 'precio','stock', 'imagen','descripcion','bodega','varietal','cosecha','stock')
#     list_editable = ('nombre')
#     list_filter = ('varietal')
#     search_fields = ('nombre','varietal', 'bodega')

# class VarietalAdmin(admin.ModelAdmin):
#     list_display = ( 'nombre','descripcion')
#     exclude = ('activo')

#     #modificacion del listado que se quiere mostrar
#     def get_queryset(self, request):
#         query = super(VarietalAdmin, self).get_queryset(request)
#         filtered_query = query.filter(activo=False)
#         return filtered_query

# class BodegaAdmin(admin.ModelAdmin):
#     list_display = ( 'nombre','descripcion', 'ubicacion', 'telefono', 'email')
#     exclude = ('baja')

#     #modificacion del listado que se quiere mostrar
#     def get_queryset(self, request):
#         query = super(BodegaAdmin, self).get_queryset(request)
#         filtered_query = query.filter(baja=False)
#         return filtered_query
# class ProductoAdmin(admin.ModelAdmin):
    
#     #modificar listados de foreingkey
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == "varietal":
#             kwargs["queryset"] = Varietal.objects.filter(activo=False)
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == "bodega":
#             kwargs["queryset"] = Bodega.objects.filter(baja=False)
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)

# #permite mostrar y editar modelos relacionados en línea dentro de la interfaz de administración de otro modelo     
# #class InscripcionInline(admin.TabularInline):
#     model = Inscripcion

# #agregar la funcionalidad de creación de instancias de Inscripcion
# # class ComisionAdmin(admin.ModelAdmin):
# #     inlines = [
# #         InscripcionInline,
# #     ]

# #registros de modelos en Admin personalizado
# sitio_admin = ECPruebaAdminSite(name='ecpruebaadmin')
# sitio_admin.register(Varietal,VarietalAdmin)
# sitio_admin.register(Producto,ProductoAdmin)
# sitio_admin.register(Bodega,BodegaAdmin)
# sitio_admin.register(Usuario,UserAdmin)
# sitio_admin.register(Group, GroupAdmin)
# # admin.site.register(Curso,CursoAdmin)

