from django.shortcuts import render

# Create your views here.

def dayend(request):
    return render(request,'fullpost/dayendsale/dayendsale.html')
