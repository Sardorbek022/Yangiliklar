from modeltranslation.translator import register, TranslationOptions, translator
from .models import NewsModel, CategoryModel


@register(NewsModel)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body')


@register(CategoryModel)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)