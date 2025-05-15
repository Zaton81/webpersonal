from django.contrib import admin
from .models import Posts, Category
class PostsAdmin(admin.ModelAdmin):
    '''clase PostsAdmin para personalizar el admin de Posts
    readonly_fields: campos que no se pueden editar
    list_display: campos que se muestran en la lista de posts
    ordering: ordena los campos en la lista de posts
    '''
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'published', 'author', "post_categories") #campos que se muestran en la lista de posts
    ordering = ("author", "published") # muestra los campos en la lista de posts
    search_fields = ('title', 'content', "author__username", "categories__name") #busca en los campos title y content
    list_filter = ('author__username', 'categories__name') #filtros en la lista de posts
    date_hierarchy = 'published' #filtro por fecha de publicación

    def post_categories(self, obj):
        '''muestra las categorias en el admin de posts'''
        return ", ".join([c.name for c in obj.categories.all()])
    post_categories.short_description = 'Categorías' #nombre del campo en el admin de posts

    # Inyectamos nuestro fichero css
    class Media:
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }


admin.site.register(Posts, PostsAdmin) #Configura el admin de Posts


class CategoryAdmin(admin.ModelAdmin):
    '''clase CategoryAdmin para personalizar el admin de Category
    readonly_fields: campos que no se pueden editar'''
    readonly_fields = ('created', 'updated')

admin.site.register(Category, CategoryAdmin)