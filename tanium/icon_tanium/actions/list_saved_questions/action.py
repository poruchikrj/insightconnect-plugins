import insightconnect_plugin_runtime
from .schema import ListSavedQuestionsInput, ListSavedQuestionsOutput, Input, Output, Component
# Custom imports below


class ListSavedQuestions(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_saved_questions',
                description=Component.DESCRIPTION,
                input=ListSavedQuestionsInput(),
                output=ListSavedQuestionsOutput())

    def run(self, params={}):
        # TODO: Implement run function
        return {}
