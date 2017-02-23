from django.shortcuts import render


def index(request):



	# c_aption = About.objects.order_by('publish_date')[0]


	return render(request, 'index.html')