import insightconnect_plugin_runtime
from .schema import ListSavedQuestionsInput, ListSavedQuestionsOutput, Input, Output, Component
# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException

class ListSavedQuestions(insightconnect_plugin_runtime.Action):

    _URI = "api/v2/saved_questions"

    def __init__(self):
        super(self.__class__, self).__init__(
                name='list_saved_questions',
                description=Component.DESCRIPTION,
                input=ListSavedQuestionsInput(),
                output=ListSavedQuestionsOutput())

    def run(self, params={}):
        resource_requester = self.connection.resource_requester
        filter_ = params.get(Input.FILTER)
        tanium_options = {"tanium-options": {"cache_filters": filter_}}
        response = resource_requester.resource_request(self._URI, headers=tanium_options)
        try:
            output = response["data"]
        except KeyError:
            raise PluginException(cause="The response data from the Tanium server was malformed. ",
                                  assistance="Contact support for acceptance. ",
                                  data=f"The response data was:\n {response}")

        return {Output.QUESTIONS: output}
