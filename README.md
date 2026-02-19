# uijit

**UI Just-In-Time** - MCP server for A2UI canvas rendering and Chromecast casting.

## What is uijit?

uijit is an MCP (Model Context Protocol) server that enables AI agents to create rich visualizations using the A2UI component format and cast them to Chromecast/Google TV devices in real-time.

This repository also hosts the **Canvas Receiver** - a Google Cast receiver application served via GitHub Pages at [uijit.com](https://uijit.com).

## Installation

```bash
pip install uijit
```

## Usage

### As an MCP server (stdio transport)

```bash
uijit --host 0.0.0.0 --port 8090
```

### With nanobot

Add to your nanobot config:

```json
{
  "tools": {
    "mcpServers": {
      "uijit": {
        "command": "uijit",
        "args": ["--host", "0.0.0.0", "--port", "8090"]
      }
    }
  }
}
```

### MCP Tools

| Tool | Description |
|------|-------------|
| `canvas_create` | Create a new canvas surface |
| `canvas_update` | Update components using A2UI format |
| `canvas_data` | Update data model without re-rendering |
| `canvas_close` | Close and delete a surface |
| `canvas_list` | List all surfaces |
| `canvas_show` | Show/navigate existing surfaces |
| `canvas_get` | Get full state of a canvas |

## How It Works

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  AI Agent   │────▶│   uijit     │────▶│   uijit     │────▶│ Chromecast  │
│  (nanobot)  │     │  MCP Server │     │  Receiver   │     │    TV       │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
      │                   │                   │                   │
      │  A2UI JSON        │  WebSocket        │  Cast SDK         │
      │  (components)     │  (real-time)      │  (custom msg)     │
```

1. **AI Agent** generates A2UI visualization components via MCP tools
2. **uijit MCP Server** manages surfaces, renders HTML, serves via WebSocket
3. **uijit Receiver** (GitHub Pages) is loaded by Chromecast and connects to the server
4. **Chromecast** displays the live-updating visualization

## URLs

| Path | Description |
|------|-------------|
| [uijit.com](https://uijit.com) | Landing page |
| [uijit.com/canvas-receiver/](https://uijit.com/canvas-receiver/) | Google Cast receiver application |

## Google Cast App Registration

To use the receiver with Chromecast:

1. Go to [Google Cast SDK Developer Console](https://cast.google.com/publish)
2. Register the receiver URL: `https://uijit.com/canvas-receiver/`
3. Use the App ID in your sender application

## Repository Structure

```
uijit/
├── index.html                 # Landing page (GitHub Pages)
├── canvas-receiver/
│   └── index.html             # Cast receiver application
├── pyproject.toml             # Python package metadata
├── src/uijit/                 # MCP server source
│   ├── cli.py                 # CLI entry point
│   ├── server.py              # MCP protocol handler
│   ├── canvas_manager.py      # Surface lifecycle management
│   ├── renderer.py            # A2UI → HTML renderer
│   ├── web_server.py          # HTTP/WebSocket server
│   └── models.py              # Data models
└── tests/
    └── test_canvas_manager.py # Tests
```

## Related Projects

- [androidtvmcp](https://github.com/pigeek/androidtvmcp) - MCP server for Android TV control

## License

MIT
