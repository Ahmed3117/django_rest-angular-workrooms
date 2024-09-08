from django.contrib import admin

from room.models import Room
from todo.models import Todo

class TodoInline(admin.TabularInline):
    model = Todo
    extra = 0

# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display = ('title', 'room_id','admin','is_done')
    list_editable = ('admin','is_done')
    list_filter = ('admin','is_done')
    search_fields = ('admin__username','admin__name','title','room_id')
    readonly_fields = ('room_id',)
    autocomplete_fields = ('admin','members')
    inlines = [TodoInline]
    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        obj = form.instance
        if not obj.admin and obj.members.exists():
            obj.admin = obj.members.first()
            obj.save()
admin.site.register(Room,RoomAdmin)