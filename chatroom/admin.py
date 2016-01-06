from django.contrib import admin
from django.db.models import Sum

from login.models import User_Profiles
from chatroom.models import Comment, CRanking

class CRankingInline(admin.StackedInline):
    model = CRanking
    extra = 1

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'get_commenter_username','get_component_name','get_ranking', 'date', 'text')

    inlines = [CRankingInline]

    def get_ranking(self, obj):
        return CRanking.objects.get(comment = obj).aggregate(Sum('rank'))
    get_ranking.short_description = 'ranking'

    def get_commenter_username(self, obj):
        return User_Profiles.objects.get(user = obj.commenter).username
    get_commenter_username.short_description = 'commenter'

    def get_component_name(self, obj):
        return obj.component.common_name
    get_component_name.short_description = 'Component Name'
