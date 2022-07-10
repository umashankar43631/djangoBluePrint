from django.shortcuts import render
# from django.shortcuts import get_object_or_404
from .models import Login
from django.db.models import Avg

# Create your views here.
customers = Login.objects.all()
customer_count = customers.count()
# avg_rating = customers.aggregate(Avg("rating"))  -> returns {{"rating__avg": value}}, {"rating__min": value}
# Sorting By Specific Field
# customers = Login.objects.all().order_by("field Name") -> Ascending order
# customers = Login.objects.all().order_by("-field Name") ->(-) Descending order

def index(request):
    # try:
        # customer = Login.objects.get(pk=id)
    # except:    
    #   raise Http404()
    # or customer = get_object_or_404(Login, pk=id)   
    return render(request, 'firstApp/index.html', 
    {
        "customerDetails": customers,
        "customer_count": customer_count,
    })
def LoginDetails(request, slug):
    cust1 = Login.objects.get(slug=slug)
    return render(request, 'firstApp/loginDetails.html',{
        'title': cust1.username,
    })