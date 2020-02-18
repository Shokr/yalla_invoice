from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import datetime

# Local Applications imports
from ..forms import *


@login_required
def index(request):

    invoices = Invoice.objects.all().order_by('-date_created')

    context = {
        'title': 'Recent Invoices',
        'invoice_list': invoices,
    }
    return render(request, 'invoice/index.html', context)


# Show big list of all invoices
@login_required
def all_invoices(request):
    invoices = Invoice.objects.order_by('-date_created')

    context = {
        'title': 'All Invoices',
        'invoice_list': invoices,
    }
    return render(request, 'invoice/all_invoice.html', context)


# Show invalid invoices
@login_required
def invalid_invoices(request):
    invoices = Invoice.objects.filter(valid='False').order_by('-date_created')

    context = {
        'title': 'Invalid Invoices',
        'invoice_list': invoices,
    }
    return render(request, 'invoice/invalid_invoices.html', context)


# Display a specific invoice
@login_required
def invoice(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)

    itemformset = ItemFormset()
    context = {
        'title': 'Invoice ' + str(invoice_id),
        'invoice': invoice,
        'formset': itemformset,
    }
    return render(request, 'invoice/invoice.html', context)


# Search for invoice
@login_required
def search_invoice(request):
    id = request.POST['id']
    return HttpResponseRedirect(reverse('invoice:view_invoice', args=(id,)))


# Create new invoice
@login_required
def new_invoice(request):
    # If no customer_id is defined, create a new invoice
    if request.method == 'POST':
        customer_id = request.POST.get("customer_id", "None")
        expiration_date = request.POST.get("expiration_date", datetime.date.today())
        status = request.POST.get("status", 'Unpaid')

        if customer_id == 'None':
            customers = Customer.objects.order_by('name')
            context = {
                'title': 'New Invoice',
                'customer_list': customers,
                'error_message': 'Please select a customer.',
            }
            return render(request, 'invoice/new_invoice.html', context)
        else:
            customer = get_object_or_404(Customer, pk=customer_id)
            i = Invoice(customer=customer,
                        expiration_date=expiration_date, status=status)
            i.save()
            return HttpResponseRedirect(reverse('invoice:invoice', args=(i.id,)))

    else:
        # Customer list needed to populate select field
        customers = Customer.objects.order_by('name')
        context = {
            'title': 'New Invoice',
            'customer_list': customers,
        }
        return render(request, 'invoice/new_invoice.html', context)


# View invoice
@login_required
def view_invoice(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    context = {
        'title': "Invoice " + str(invoice_id),
        'invoice': invoice,
    }
    return render(request, 'invoice/view_invoice.html', context)


# Print invoice
@login_required
def print_invoice(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    context = {
        'title': "Invoice " + str(invoice_id),
        'invoice': invoice,
    }
    return render(request, 'invoice/print_invoice.html', context)


# Invalidate an invoice
@login_required
def invalidate_invoice(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    invoice.valid = False
    invoice.save()
    return HttpResponseRedirect(reverse('invoice:index'))
