# Grafana MCP Plugin for Dify

This plugin wraps the official [Grafana MCP server](https://github.com/grafana/mcp-grafana) to provide advanced Grafana capabilities directly within Dify. It uses the official Model Context Protocol (MCP) to communicate with the Grafana server, ensuring full compatibility and access to the latest features.

## Features

- **Search Dashboards**: Find dashboards by title, tags, or starred status.
- **Get Dashboard Summary**: Get a high-level summary of a dashboard's content.
- **Get Dashboard Properties**: Retrieve the full JSON definition of a dashboard.
- **Get Panel Queries**: Extract data source queries for panels.
- **Query Prometheus**: Execute PromQL queries.
- **Query Loki**: Execute LogQL queries.
- **List Datasources**: List all configured datasources.

## Configuration

To use this plugin, you need:

1. **Grafana URL**: The base URL of your Grafana instance (e.g., `https://grafana.example.com`).
2. **Service Account Token**: A Grafana Service Account token with appropriate permissions (Viewer or Editor, depending on what you want the agent to do).

## Installation

1. Package the plugin folder as a `.zip` or use the Dify CLI to install.
2. In Dify, go to **Plugins** -> **Install from File**.
3. Configure the credentials in the tool provider settings.

## Author

Created by [nise-ua](https://github.com/nise-ua).
