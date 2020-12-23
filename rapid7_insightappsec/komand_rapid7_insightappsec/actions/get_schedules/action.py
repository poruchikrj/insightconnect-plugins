import insightconnect_plugin_runtime
from .schema import GetSchedulesInput, GetSchedulesOutput, Input, Output, Component
# Custom imports below
from komand_rapid7_insightappsec.util.endpoints import Schedule
from komand_rapid7_insightappsec.util.resource_helper import ResourceHelper
import json
from insightconnect_plugin_runtime.exceptions import PluginException


class GetSchedules(insightconnect_plugin_runtime.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_schedules',
                description=Component.DESCRIPTION,
                input=GetSchedulesInput(),
                output=GetSchedulesOutput())

    def run(self, params={}):
        # TODO: Implement run function
        sort = params.get(Input.SORT)
        resource_helper = ResourceHelper(self.connection.session, self.logger)
        endpoint = Schedule.get_schedules(self.connection.url)
        response = resource_helper.resource_request(endpoint, method="GET", params={"sort":sort})
        try:
            response = json.loads(response["resource"])
        except json.decoder.JSONDecodeError:
            self.logger.error(f'InsightAppSec response: {response}')
            raise PluginException(cause='The response from InsightAppSec was not in JSON format.', assistance='Contact support for help.'
                            ' See log for more details')
        try:
            metadata = response['metadata']
            data = response['data']
            links = response['links']
        except KeyError:
            self.logger.error(f'InsightAppSec response: {response}')
            raise PluginException(cause='The response from InsightAppSec was malformed.', assistance='Contact support for help.'
                            ' See log for more details')
        return {Output.METADATA:metadata, Output.DATA:data, Output.LINKS:links}