from django.shortcuts import render
from django.http import HttpResponse

tax_rate=0.15
def Default(request):
    return HttpResponse("This is a site to calculate tax")

def caltax(request, tax):
    cal=(tax*tax_rate)+tax
    return HttpResponse(f"The total price after the tax is: {cal}")

def tax(request): 
 return render(request ,"tax/taxrate.html",{"taxx":tax_rate*100})

