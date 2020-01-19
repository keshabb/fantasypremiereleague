from django.contrib import admin
from .models import Season, Gameweek, Winner


class SeasonAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Season", {"fields": ["name"]})
    ]


class GameweekAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Game Week", {"fields": ["name", "season"]})
    ]


class WinnerAdmin(admin.ModelAdmin):
    fieldsets = [
        ("User Info", {"fields": ["first_name", "middle_name", "last_name",
                                  "email", "phone", "profile_pic"]}),
        ("Game Week", {"fields": ["game_week"]})
    ]


admin.site.register(Season)
admin.site.register(Gameweek)
admin.site.register(Winner)

