import asyncio
from dify_plugin.entities.tool import ToolInvokeMessage
from dify_plugin.interface.tool import Tool
from tools.utils import GrafanaMCPWrapper

class GetPanelQueriesTool(Tool):
    def _invoke(self, tool_parameters: dict) -> ToolInvokeMessage:
        url = self.runtime.credentials.get('grafana_url')
        token = self.runtime.credentials.get('grafana_token')
        wrapper = GrafanaMCPWrapper(url, token)
        
        args = {"dashboardUID": tool_parameters.get('dashboardUID')}
        if tool_parameters.get('panelID'):
            args['panelID'] = tool_parameters['panelID']

        try:
            result = asyncio.run(wrapper.call_tool("get_panel_queries", args))
            return self.create_text_message(result)
        except Exception as e:
            return self.create_text_message(f"Error: {str(e)}")
