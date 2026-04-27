import asyncio
from dify_plugin.entities.tool import ToolInvokeMessage
from dify_plugin.interface.tool import Tool
from .utils import GrafanaMCPWrapper

class ListDatasourcesTool(Tool):
    def _invoke(self, tool_parameters: dict) -> ToolInvokeMessage:
        url = self.runtime.credentials.get('grafana_url')
        token = self.runtime.credentials.get('grafana_token')
        wrapper = GrafanaMCPWrapper(url, token)
        
        try:
            result = asyncio.run(wrapper.call_tool("list_datasources", {}))
            return self.create_text_message(result)
        except Exception as e:
            return self.create_text_message(f"Error: {str(e)}")
