from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Question


# Create your views here.
def index(request):
    page = request.GET.get('page', '1')
    question_list = Question.objects.order_by('-create_date')
    paginator = Paginator(question_list, 5)
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    return render(request, 'board/question_list.html', context)
    # return HttpResponse("Hi~")


def detail(request, question_id):
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'board/question_detail.html', context)
