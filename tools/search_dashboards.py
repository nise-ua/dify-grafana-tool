import asyncio
from dify_plugin.entities.tool import ToolInvokeMessage
from dify_plugin.interface.tool import Tool
from .utils import GrafanaMCPWrapper

class SearchDashboardsTool(Tool):
    def _invoke(self, tool_parameters: dict) -> ToolInvokeMessage:
        url = self.runtime.credentials.get('grafana_url')
        token = self.runtime.credentials.get('grafana_token')
        
        wrapper = GrafanaMCPWrapper(url, token)
        
        # Prepare arguments for official mcp-grafana
        args = {}
        if tool_parameters.get('query'):
            args['query'] = tool_parameters['query']
        if tool_parameters.get('tag'):
            # mcp-grafana might expect a list
            args['tag'] = [t.strip() for t in tool_parameters['tag'].split(',')]
        if tool_parameters.get('starred') is not None:
            args['starred'] = tool_parameters['starred']
        if tool_parameters.get('limit'):
            args['limit'] = tool_parameters['limit']

        try:
            result = asyncio.run(wrapper.call_tool("search_dashboards", args))
            return self.create_text_message(result)
        except Exception as e:
            return self.create_text_message(f"Error: {str(e)}")
