from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect

from app.forms import CustomersModelForm
from app.models import Customers


# Create your views here.
from django.core.paginator import Paginator
from django.shortcuts import render


def customers(request):
    search_query = request.GET.get('Search', '')
    customers = Customers.objects.all()
    paginator = Paginator(customers, 2)
    page_number = request.GET.get('page')
    customers = paginator.get_page(page_number)
    if search_query:
        customers = Customers.objects.filter(Q(name__icontains=search_query) | Q(email__icontains=search_query))
    context = {
        'customers': customers
    }
    return render(request,'app/customers.html',context)

def customers_details(request,slug):
    customer1 = Customers.objects.get(slug=slug)
    context = {
        'customer1':customer1
    }
    return render(request,'app/customer_details.html', context)

# @login_required
def add_customer(request):
    if request.method == 'POST':
        form = CustomersModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('customers')

    else:
        form = CustomersModelForm()

    context = {
        'form': form,
    }
    return render(request, 'app/add_customer.html', context)



def edit_customer(request,pk):
    customer = Customers.objects.get(id=pk)
    form = CustomersModelForm(instance=customer)
    if request.method == "POST":
        form = CustomersModelForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customers')

    context = {
        'form': form,
        'customer':customer
    }
    return render(request,'app/edit_customer.html',context)


def delete_customers(request,pk):
    customer = Customers.objects.filter(id=pk).first()
    if customer:
        customer.delete()
        return redirect('customers')
    context = {
        'customer':customer
    }
    return render(request,'app/customers.html',context)

def login(request):
    return render(request,'app/login.html')

def register(request):
    return render(request,'app/register.html')
