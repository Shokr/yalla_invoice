# Third Party imports
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

# Local Applications imports
from ..forms import *


@login_required
def customer_list(request):
    """
    List all Customers
    """
    customers = Customer.objects.all()

    context = {
        'title': 'Customer List',
        'customers': customers,
    }
    return render(request, 'invoice/customers.html', context)


@login_required
def customer(request, customer_id):
    """
      Displays the details for a particular customer with their invocies.
    """
    customer = get_object_or_404(Customer, pk=customer_id)
    invoices = Invoice.objects.filter(customer=customer).order_by('-date_created')
    context = {
        'title': "Customer info - %s" % customer.name,
        'customer': customer,
        'invoices': invoices,
    }
    return render(request, 'invoice/customer.html', context)


# View for creating a new customer.
@login_required
def new_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New Customer created successfully')
            return redirect('invoice:customer_list')
    else:
        form = CustomerForm()

    context = {'form': form}
    template_name = 'invoice/new_customer.html'

    return render(request, template_name, context)


# Update customer
@login_required
def update_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer details updated successfully')
            return HttpResponseRedirect(reverse('invoice:customer',
                                                args=(customer.id,)))
    else:
        form = CustomerForm(instance=customer)
    context = {
        'form': form,
    }
    template_name = 'invoice/customer.html'
    return render(request, template_name, context)


# Delete customer
@login_required
# @user_passes_test(lambda u: u.groups.filter(name='xmen').count() == 0, login_url='invoice/all_invoice.html')
def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    customer.delete()
    messages.success(request, "Customer successfully deleted.")
    return HttpResponseRedirect(reverse('invoice:customer_list'))
