from django.shortcuts import render
from .models import Services


def index(request):
	errand_item_list = Services.objects.order_by('publish_date')[0]


	# c_aption = About.objects.order_by('publish_date')[0]


	context = {
		'errand_item_list': errand_item_list
	}

	return render(request, 'index.html', context)