import asyncio
import os
import sys
from typing import Any, Dict, List, Optional
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

class GrafanaMCPWrapper:
    def __init__(self, url: str, token: str):
        self.url = url
        self.token = token
        # The mcp-grafana server is usually run as 'mcp-grafana' or 'python -m mcp_grafana'
        # Since it's installed via pip, it should be in the path.
        self.server_params = StdioServerParameters(
            command="mcp-grafana",
            args=[],
            env={
                **os.environ,
                "GRAFANA_URL": self.url,
                "GRAFANA_SERVICE_ACCOUNT_TOKEN": self.token,
            }
        )

    async def call_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Any:
        async with stdio_client(self.server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                result = await session.call_tool(tool_name, arguments)
                
                # The result from MCP session.call_tool is a CallToolResult
                # We need to extract the content.
                if result.isError:
                    raise Exception(f"MCP Tool Error: {result.content}")
                
                # Usually MCP tool results are a list of content blocks
                return "\n".join([c.text for c in result.content if hasattr(c, 'text')])

    async def list_tools(self) -> List[Any]:
        async with stdio_client(self.server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                return await session.list_tools()
