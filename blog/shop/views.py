from django.db.models import F, Sum
from django.shortcuts import render
from django.core.paginator import Paginator


from shop.forms import ProductFiltersForm
from shop.models import Product, Iphone6

# можно сделать срез c 1 о 10 Product.objects.all()[1:10]
# products.filter(status=filters_form.cleaned_data["status"])[1:10]
def products_view(request):
    products = Product.objects.all()
    filters_form = ProductFiltersForm(request.GET)

    if filters_form.is_valid():
        if filters_form.cleaned_data["status"]:
            products = products.filter(status=filters_form.cleaned_data["status"])
        if filters_form.cleaned_data["price__gt"]:
            products = products.filter(cost__gt=filters_form.cleaned_data["price__gt"])
        if filters_form.cleaned_data["price__lt"]:
            products = products.filter(cost__lt=filters_form.cleaned_data["price__lt"])

        if filters_form.cleaned_data["order_by"]:
            order_by = filters_form.cleaned_data["order_by"]
            if order_by == "price_asc":
                products = products.order_by("cost")
            if order_by == "price_desc":
                products = products.order_by("-cost")
            if order_by == "max_count":
                products = products.annotate(
                    total_count=Sum("purchases__count")
                ).order_by("-total_count")
            if order_by == "max_price":
                products = products.annotate(
                    total_price=Sum("purchases__count") * F("cost")
                ).order_by("-total_price")

# paginator

    paginator = Paginator(products, 3)
    page_number = request.GET.get("page")
    products = paginator.get_page(page_number)


    return render(
        request,
        "products/list.html",
        {"filters_form": filters_form, "products": products},
    )


def product_details_view(request, *args, **kwargs):
    product = Product.objects.get(id=kwargs["product_id"])

    # Add to favorites if this is POST request
    if request.user.is_authenticated and request.method == "POST":
        if request.POST["action"] == "add":
            product.favorites.add(request.user)
        else:
            product.favorites.remove(request.user)

    return render(
        request,
        "products/details.html",
        {
            "product": product,
            "is_product_in_favorites": request.user in product.favorites.all(),
        },
    )


def iphone1(request):
    items = Iphone6.objects.all()
    return render(request, 'iphone.html', {'items': items})
