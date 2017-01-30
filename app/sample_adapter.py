from chatterbot.logic import LogicAdapter
from chatterbot.conversation import Statement
import nltk


class SampleLogic(LogicAdapter):
    """
    A logic adater that returns a response based on known responses to
    the closest matches to the input statement.
    """

    def can_process(self, statement):
        """
        Check that the chatbot's storage adapter is available to the logic
        adapter and there is at least one statement in the database.
        """
        return self.chatbot.storage.count()

    def process(self, input_statement):

        # Select the closest match to the input statement
        _text = input_statement.text
        tokens = nltk.word_tokenize(_text)
        tagged = nltk.pos_tag(tokens)
        if len(tokens) < 3 :
            response_statement = Statement("Hi, how can I help you?")
            confidence = 1

        return confidence, response_statement
