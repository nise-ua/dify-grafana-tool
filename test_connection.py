import asyncio
import os
from tools.utils import GrafanaMCPWrapper

async def test_connection():
    # Load from environment or replace with your test values
    url = os.getenv("GRAFANA_URL", "https://your-grafana.com")
    token = os.getenv("GRAFANA_SERVICE_ACCOUNT_TOKEN", "your-token")
    
    print(f"Testing connection to {url}...")
    wrapper = GrafanaMCPWrapper(url, token)
    
    try:
        print("Listing datasources via MCP...")
        result = await wrapper.call_tool("list_datasources", {})
        print("Success! Result:")
        print(result)
    except Exception as e:
        print(f"Error: {e}")
        print("\nMake sure:")
        print("1. mcp-grafana is installed: pip install mcp-grafana")
        print("2. GRAFANA_URL and GRAFANA_SERVICE_ACCOUNT_TOKEN are correct.")

if __name__ == "__main__":
    asyncio.run(test_connection())
