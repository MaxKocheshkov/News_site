from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Thematic, Membership


class MembershipInlineFormset(BaseInlineFormSet):
    def clean(self):
        super(MembershipInlineFormset, self).clean()
        check_tag = 0
        for form in self.forms:
            if not form.is_valid():
                return
            if form.cleaned_data and not form.cleaned_data.get('DELETE'):
                if form.cleaned_data['main_tag']:
                    check_tag += 1
            if check_tag > 1:
                raise ValidationError('Основной тег уже выбран!')
            elif check_tag < 1:
                raise ValidationError('Выберите основной тег статьи')
        return super().clean()  # вызываем базовый код переопределяемого метода


class RelationshipInline(admin.TabularInline):
    model = Membership
    formset = MembershipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]


@admin.register(Thematic)
class ThematicAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]
