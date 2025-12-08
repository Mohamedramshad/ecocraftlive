from django.shortcuts import render
from django.shortcuts import render
from web.models import Slider,Legacy,Aboutbox,ProductCategory,ProductFeature,Product,GalleryCategory,Galleryimage
from django.http import JsonResponse



# Create your views here.

def index(request):
    product_category = ProductCategory.objects.all()
    slider=Slider.objects.all()
    legacy=Legacy.objects.all()
    context={
        "product_category":product_category,
        "slider":slider,
        "legacy":legacy,
    }
    return render(request, 'web/index.html',context=context)

def about(request):
    product_category = ProductCategory.objects.all()
    about=Aboutbox.objects.all()
    context={
        "product_category":product_category,
        "about":about,
    }
    return render(request, 'web/about.html',context=context)

def product(request,id):
    product_category = ProductCategory.objects.all()
    category=ProductCategory.objects.get(id=id)
    product=Product.objects.filter(category=category)
    context={
        "product_category":product_category,
        "product":product,
        "category":category,
    }
    
    return render(request, 'web/product.html',context=context)



def contact(request):
    product_category = ProductCategory.objects.all()

    context={
        "product_category":product_category,        
    }
    
    return render(request, 'web/contact.html',context=context)


def gallery(request):
    product_category = ProductCategory.objects.all()
    gallery_category = GalleryCategory.objects.all()
    image= Galleryimage.objects.all()
    context={
        "product_category":product_category,
        "gallery_category":gallery_category,
        "image":image,
    }
    return render(request, 'web/gallery.html',context=context)



def product_gallery(request , id):
    gallery_category = GalleryCategory.objects.all()
    category=GalleryCategory.objects.get(id=id)
    image= Galleryimage.objects.filter(category=category)
    context={
        "gallery_category":gallery_category,
        "image":image,
        "category":category,
    }
    return render(request, 'web/gallery.html',context=context)



def gallery_images(request, category_id):
    images = Galleryimage.objects.filter(category_id=category_id)
    image_list = [{'image_url': image.image.url} for image in images]
    return JsonResponse({'images': image_list})

def visualise(request):
    return render(request, 'web/visualise.html',)

        