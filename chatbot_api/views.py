from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from .serializers import UserSerializer, GroupSerializer, QASerializer
from .models import QACorpus

from chatterbot import ChatBot
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser

from chatterbot.ext.django_chatterbot.views import ChatterBotViewMixin
from chatterbot.trainers import ListTrainer


qa_set = QACorpus.objects.all()             

class ChatterBotView(ChatterBotViewMixin, APIView):
    parser_classes = (JSONParser,)

    def get(self, request, format=None):

        # Return a method not allowed response
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request, format=None):

        input_statement = request.data.get('text')

        print(input_statement)

        #self.chatterbot.set_trainer(ListTrainer)
        #for each in qa_set:
            #self.chatterbot.train([each.question, each.answer])

        chat_session = self.get_chat_session(request)

        response_data = self.chatterbot.get_response(input_statement, chat_session.id_string)

        print(response_data)

        data = {'question': input_statement, 'answer': response_data.text}

        print(data)

        return Response(data)



class FeedBackTrainView(ChatterBotViewMixin, APIView):
    parser_classes = (JSONParser,)

    def get(self, request, format=None):

        # Return a method not allowed response
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request, format=None):

        input_statement = request.data.get('text')

        input_statement = self.chatterbot.input.process_input_statement(input_statement)

        # Preprocess the input statement
        for preprocessor in self.chatterbot.preprocessors:
            input_statement = preprocessor(self, input_statement)

        chat_session = self.get_chat_session(request)

        statement_data, response_data, _id = self.chatterbot.generate_response(input_statement, chat_session.id_string)

        data = {'for_statement': statement_data.text, 'output_is': response_data.text}

        return Response(data)




class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class QAViewSet(viewsets.ModelViewSet):
    
    queryset = qa_set
    serializer_class = QASerializer

