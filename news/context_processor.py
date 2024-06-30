from .models import (
    CategoryModel
)


def UniverCategory(self,):
    
    category_list = CategoryModel.objects.all()

    context = {
        'category_list' : category_list,
    }
    return context