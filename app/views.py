from django.shortcuts import render

# Create your views here.


def index_view(request):

	return render(request, 'index.html')


def chat_view(request):

	return render(request, 'chat.html')


def train_view(request):

	return render(request, 'train.html')