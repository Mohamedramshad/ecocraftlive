from django.shortcuts import render,reverse,redirect
from django.http import HttpResponseRedirect,HttpResponse
from web.models import *
from manager.forms import *
from core.functions import generate_form_errors
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from .forms import ManagerLoginForm
from django.contrib import messages
from core.decorators import allow_manager

@login_required(login_url='manager:login')
def index(request):
    total_products = Product.objects.count()
    context = {
        'total_products': total_products,
    }
    return render(request,'manager/index.html',context=context)





def manager_login(request):
    if request.method == "POST":
        form = ManagerLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_superuser:  # Allow only superusers (admin)
                    login(request, user)
                    return redirect("manager:product")  # Redirect to the manager's dashboard
                else:
                    messages.error(request, "Unauthorized access. Only admins can log in.")
                    return HttpResponse("Unauthorized", status=401)
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Form is invalid.")
    else:
        form = ManagerLoginForm()

    return render(request, "manager/login.html", {"form": form})




def manager_logout(request):
    logout(request) 
    return redirect('manager:login') 







# list


@login_required(login_url='manager:login')
def slider(request):
    instences = Slider.objects.all()

    context = {
        "instences": instences
    }
    return render(request,'manager/slider.html',context=context)


@login_required(login_url='manager:login')
def legacy(request):
    instences = Legacy.objects.all()

    context = {
        "instences": instences
    }
    return render(request,'manager/legacy.html',context=context)



@login_required(login_url='manager:login')
def product_category(request):
    instences = ProductCategory.objects.all()

    context = {
        "instences": instences
    }
    return render(request,'manager/product-category.html',context=context)


@login_required(login_url='manager:login')
def product_feature(request):
    instences = ProductFeature.objects.all()

    context = {
        "instences": instences
    }
    return render(request,'manager/product-feature.html',context=context)



@login_required(login_url='manager:login')
def product(request):
    instences = Product.objects.all()

    context = {
        "instences": instences
    }
    return render(request,'manager/product.html',context=context)



@login_required(login_url='manager:login')
def gallery_category(request):
    instences = GalleryCategory.objects.all()

    context = {
        "instences": instences
    }
    return render(request,'manager/gallery-category.html',context=context)


@login_required(login_url='manager:login')
def gallery(request):
    instences = Galleryimage.objects.all()

    context = {
        "instences": instences
    }
    return render(request,'manager/gallery.html',context=context)




@login_required(login_url='manager:login')
def aboutbox(request):
    instences = Aboutbox.objects.all()

    context = {
        "instences": instences
    }
    return render(request,'manager/about-box.html',context=context)








# ADD



@login_required(login_url='manager:login')
def slider_add(request):
    if request.method == 'POST':
        form = SliderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('manager:slider'))
        else:
            message = generate_form_errors(form)
    else:
        form = SliderForm()
        message = None
    context = {"form": form, "error": bool(message), "message": message}
    return render(request, "manager/slider_add.html", context)

@login_required(login_url='manager:login')
def legacy_add(request):
    if request.method == 'POST':
        form = LegacyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('manager:legacy'))
        else:
            message = generate_form_errors(form)
    else:
        form = LegacyForm()
        message = None
    context = {"form": form, "error": bool(message), "message": message}
    return render(request, "manager/legacy_add.html", context)

@login_required(login_url='manager:login')
def aboutbox_add(request):
    if request.method == 'POST':
        form = AboutboxForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('manager:aboutbox'))
        else:
            message = generate_form_errors(form)
    else:
        form = AboutboxForm()
        message = None
    context = {"form": form, "error": bool(message), "message": message}
    return render(request, "manager/aboutbox_add.html", context)

@login_required(login_url='manager:login')
def product_category_add(request):
    if request.method == 'POST':
        form = ProductCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('manager:product_category'))
        else:
            message = generate_form_errors(form)
    else:
        form = ProductCategoryForm()
        message = None
    context = {"form": form, "error": bool(message), "message": message}
    return render(request, "manager/product_category_add.html", context)

@login_required(login_url='manager:login')
def product_feature_add(request):
    if request.method == 'POST':
        form = ProductFeatureForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('manager:product_feature'))
        else:
            message = generate_form_errors(form)
    else:
        form = ProductFeatureForm()
        message = None
    context = {"form": form, "error": bool(message), "message": message}
    return render(request, "manager/product_feature_add.html", context)

@login_required(login_url='manager:login')
def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('manager:product'))
        else:
            message = generate_form_errors(form)
    else:
        form = ProductForm()
        message = None
    context = {"form": form, "error": bool(message), "message": message}
    return render(request, "manager/product_add.html", context)

@login_required(login_url='manager:login')
def gallery_category_add(request):
    if request.method == 'POST':
        form = GalleryCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('manager:gallery_category'))
        else:
            message = generate_form_errors(form)
    else:
        form = GalleryCategoryForm()
        message = None
    context = {"form": form, "error": bool(message), "message": message}
    return render(request, "manager/gallery_category_add.html", context)

@login_required(login_url='manager:login')
def gallery_add(request):
    if request.method == 'POST':
        form = GalleryimageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('manager:gallery'))
        else:
            message = generate_form_errors(form)
    else:
        form = GalleryimageForm()
        message = None
    context = {"form": form, "error": bool(message), "message": message}
    return render(request, "manager/gallery_add.html", context)




# delete



@login_required(login_url='manager:login')
def slider_delete(request, id):
    instance = Slider.objects.get(id=id)
    instance.delete()
    return HttpResponseRedirect(reverse('manager:slider'))


@login_required(login_url='manager:login')
def legacy_delete(request, id):
    instance = Legacy.objects.get(id=id)
    instance.delete()
    return HttpResponseRedirect(reverse('manager:legacy'))  



@login_required(login_url='manager:login')
def aboutbox_delete(request, id):
    instance = Aboutbox.objects.get(id=id)
    instance.delete()
    return HttpResponseRedirect(reverse('manager:aboutbox'))  



@login_required(login_url='manager:login')
def product_category_delete(request, id):
    instance = ProductCategory.objects.get(id=id)
    instance.delete()
    return HttpResponseRedirect(reverse('manager:product_category'))  



@login_required(login_url='manager:login')
def product_feature_delete(request, id):
    instance = ProductFeature.objects.get(id=id)
    instance.delete()
    return HttpResponseRedirect(reverse('manager:product_feature'))  



@login_required(login_url='manager:login')
def product_delete(request, id):
    instance = Product.objects.get(id=id)
    instance.delete()
    return HttpResponseRedirect(reverse('manager:product'))  



@login_required(login_url='manager:login')
def gallery_category_delete(request, id):
    instance = GalleryCategory.objects.get(id=id)
    instance.delete()
    return HttpResponseRedirect(reverse('manager:gallery_category'))  



@login_required(login_url='manager:login')
def gallery_delete(request, id):
    instance = Galleryimage.objects.get(id=id)
    instance.delete()
    return HttpResponseRedirect(reverse('manager:gallery'))





# EDIT




@login_required(login_url='manager:login')
def slider_edit(request, id):
    instance = Slider.objects.get(id=id)
    if request.method == 'POST':
        form = SliderForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('manager:slider'))
        else:
            message = generate_form_errors(form)
            context = {
                "error": True,
                "message": message,
                "form": form,
                "instance": instance,
            }
            return render(request, "manager/slider_add.html", context=context)
    else:
        form = SliderForm(instance=instance)
        context = {
            "form": form,
            "instance": instance,
        }
        return render(request, "manager/slider_add.html", context=context)






@login_required(login_url='manager:login')
def legacy_edit(request, id):
    instance = Legacy.objects.get(id=id)
    if request.method == 'POST':
        form = LegacyForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('manager:legacy'))
        else:
            message = generate_form_errors(form)
            context = {
                "error": True,
                "message": message,
                "form": form,
                "instance": instance,
            }
            return render(request, "manager/legacy_add.html", context=context)
    else:
        form = LegacyForm(instance=instance)
        context = {
            "form": form,
            "instance": instance,
        }
        return render(request, "manager/legacy_add.html", context=context)





@login_required(login_url='manager:login')
def aboutbox_edit(request, id):
    instance = Aboutbox.objects.get(id=id)
    if request.method == 'POST':
        form = AboutboxForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('manager:aboutbox'))
        else:
            message = generate_form_errors(form)
            context = {
                "error": True,
                "message": message,
                "form": form,
                "instance": instance,
            }
            return render(request, "manager/aboutbox_add.html", context=context)
    else:
        form = AboutboxForm(instance=instance)
        context = {
            "form": form,
            "instance": instance,
        }
        return render(request, "manager/aboutbox_add.html", context=context)





@login_required(login_url='manager:login')
def product_category_edit(request, id):
    instance = ProductCategory.objects.get(id=id)
    if request.method == 'POST':
        form = ProductCategoryForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('manager:product_category'))
        else:
            message = generate_form_errors(form)
            context = {
                "error": True,
                "message": message,
                "form": form,
                "instance": instance,
            }
            return render(request, "manager/product_category_add.html", context=context)
    else:
        form = ProductCategoryForm(instance=instance)
        context = {
            "form": form,
            "instance": instance,
        }
        return render(request, "manager/product_category_add.html", context=context)






@login_required(login_url='manager:login')
def product_feature_edit(request, id):
    instance = ProductFeature.objects.get(id=id)
    if request.method == 'POST':
        form = ProductFeatureForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('manager:product_feature'))
        else:
            message = generate_form_errors(form)
            context = {
                "error": True,
                "message": message,
                "form": form,
                "instance": instance,
            }
            return render(request, "manager/product_feature_add.html", context=context)
    else:
        form = ProductFeatureForm(instance=instance)
        context = {
            "form": form,
            "instance": instance,
        }
        return render(request, "manager/product_feature_add.html", context=context)







@login_required(login_url='manager:login')
def product_edit(request, id):
    instance = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('manager:product'))
        else:
            message = generate_form_errors(form)
            context = {
                "error": True,
                "message": message,
                "form": form,
                "instance": instance,
            }
            return render(request, "manager/product_add.html", context=context)
    else:
        form = ProductForm(instance=instance)
        context = {
            "form": form,
            "instance": instance,
        }
        return render(request, "manager/product_add.html", context=context)







@login_required(login_url='manager:login')
def gallery_category_edit(request, id):
    instance = GalleryCategory.objects.get(id=id)
    if request.method == 'POST':
        form = GalleryCategoryForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('manager:gallery_category'))
        else:
            message = generate_form_errors(form)
            context = {
                "error": True,
                "message": message,
                "form": form,
                "instance": instance,
            }
            return render(request, "manager/gallery_category_add.html", context=context)
    else:
        form = GalleryCategoryForm(instance=instance)
        context = {
            "form": form,
            "instance": instance,
        }
        return render(request, "manager/gallery_category_add.html", context=context)






@login_required(login_url='manager:login')
def gallery_edit(request, id):
    instance = Galleryimage.objects.get(id=id)
    if request.method == 'POST':
        form = GalleryimageForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('manager:gallery'))
        else:
            message = generate_form_errors(form)
            context = {
                "error": True,
                "message": message,
                "form": form,
                "instance": instance,
            }
            return render(request, "manager/gallery_add.html", context=context)
    else:
        form = GalleryimageForm(instance=instance)
        context = {
            "form": form,
            "instance": instance,
        }
        return render(request, "manager/gallery_add.html", context=context)




