from django.shortcuts import render

# Create your views here.
def index(request):
	# latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {
	}
	return render(request, 'dashboard/index.html', context)