from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Local Applications imports
from ..forms import *


@login_required
def add_item(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    items_added, items_not_add = (0, 0)

    try:
        if request.method == 'POST':

            itemformset = ItemFormset(request.POST)

            if itemformset.is_valid():
                for form in itemformset:

                    item = form.cleaned_data.get('item')
                    item_qty = form.cleaned_data.get('qty')

                    if item is None or item_qty is None:
                        items_not_add += 1
                    else:
                        invoice_obj = invoice.invoiceitem_set.create(item=item, qty=item_qty)
                        invoice_obj.save()
                        items_added += 1
                        del invoice_obj

                if items_added > 0:
                    messages.success(request, '%d items added successfully to invoice !' % items_added)

                if items_not_add > 0:
                    messages.warning(request,
                                     "%d items have been discarded since some fields were empty." % items_not_add)

            else:
                messages.warning(request, "Form not valid. Most form fields were empty")
                # if form is invalid re-render the invoice
                return render(request, 'invoice/invoice.html', {
                    'title': 'Invoice ' + str(invoice_id),
                    'invoice': invoice,
                    'formset': itemformset,
                })

    except (KeyError, Invoice.DoesNotExist):
        return render(request, 'invoice/view_invoice.html', {
            'invoice': invoice,
            'error_message': 'Not all fields were completed.',
        })
    else:
        return HttpResponseRedirect(reverse('invoice:invoice', args=(invoice.id,)))


# Delete invoiceitem from invoice
@login_required
def delete_item(request, invoiceitem_id, invoice_id):
    item = get_object_or_404(InvoiceItem, pk=invoiceitem_id)
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    try:
        item.delete()
        messages.warning(request, 'Item deleted successfully from invoice! ')
    except (KeyError, InvoiceItem.DoesNotExist):
        return render(request, 'invoice/view_invoice.html', {
            'invoice': invoice,
            'error_message': 'Item does not exist.',
        })
    else:
        return HttpResponseRedirect(reverse('invoice:invoice', args=(invoice.id,)))
