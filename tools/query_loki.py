import asyncio
from dify_plugin.entities.tool import ToolInvokeMessage
from dify_plugin.interface.tool import Tool
from tools.utils import GrafanaMCPWrapper

class QueryLokiTool(Tool):
    def _invoke(self, tool_parameters: dict) -> ToolInvokeMessage:
        url = self.runtime.credentials.get('grafana_url')
        token = self.runtime.credentials.get('grafana_token')
        wrapper = GrafanaMCPWrapper(url, token)
        
        args = {"query": tool_parameters.get('query')}
        if tool_parameters.get('datasourceUID'):
            args['datasourceUID'] = tool_parameters['datasourceUID']

        try:
            result = asyncio.run(wrapper.call_tool("query_loki", args))
            return self.create_text_message(result)
        except Exception as e:
            return self.create_text_message(f"Error: {str(e)}")
