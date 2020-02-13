from django.contrib import admin

# Register your models here.
## parsed_data/admin.py
from django.contrib import admin
## models에서 BlogData를 import 해옵니다.
from .models import Link
from .models import Member
from .models import Cmt


## 아래의 코드를 입력하면 BlogData를 admin 페이지에서 관리할 수 있습니다.
## 출처: https://beomi.github.io/gb-crawling/posts/2017-03-01-HowToMakeWebCrawler-Save-with-Django.html

# admin.site.register(Cmt)

# Register the Admin classes for Book using the decorator
class CmtInline(admin.TabularInline):
    model = Cmt

@admin.register(Cmt)
class CmtAdmin(admin.ModelAdmin):
    list_display = ('comment', 'nickname', 'date', 'link')
    search_fields = ['comment', 'url']

# Register the Admin classes for BookInstance using the decorator
@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')
    search_fields = ['title', 'link']

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    inlines = [CmtInline]
    search_fields = ['nickname_text']