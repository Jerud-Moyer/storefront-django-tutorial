from django.db.models.aggregates import Count
from django.shortcuts import render
from django.db.models import Q, F, Value
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Customer, OrderItem, Order
from tags.models import TaggedItem




def say_hello(request):
    # queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
    # queryset = Order.objects.aggregate(count=Count('id'))

    content_type = ContentType.objects.get_for_model(Product)

    TaggedItem.objects. \
        select_related('tag') \
        .filter(
            content_type=content_type,
            object_id=1
        )



    return render(request, 'hello.html', {'name': 'Jerud'})
