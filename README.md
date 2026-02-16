# uijit

**UI Just-In-Time** - A service for casting dynamic AI-generated visualizations to Chromecast and Google TV devices.

## What is uijit?

uijit hosts the Canvas Receiver - a Google Cast receiver application that enables AI agents (like nanobot) to display rich visualizations on your TV in real-time.

## How It Works

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  AI Agent   │────▶│   Canvas    │────▶│   uijit     │────▶│ Chromecast  │
│  (nanobot)  │     │   Server    │     │  Receiver   │     │    TV       │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
      │                   │                   │                   │
      │  A2UI JSON        │  WebSocket        │  Cast SDK         │
      │  (components)     │  (real-time)      │  (custom msg)     │
```

1. **AI Agent** generates A2UI visualization components
2. **Canvas Server** (local) manages surfaces and WebSocket connections
3. **uijit Receiver** (this service) is loaded by Chromecast from GitHub Pages
4. **Chromecast** receives the local Canvas Server URL via Cast messaging and connects

## URLs

| Path | Description |
|------|-------------|
| `/` | Landing page (you are here) |
| `/canvas-receiver/` | Google Cast receiver application |

## For Developers

### Using with nanobot

Configure your Canvas MCP server to use uijit as the receiver URL:

```json
{
  "cast": {
    "receiver_url": "https://uijit.com/canvas-receiver/"
  }
}
```

### Google Cast App Registration

To use this receiver with Chromecast, you need to register it:

1. Go to [Google Cast SDK Developer Console](https://cast.google.com/publish)
2. Register the receiver URL: `https://uijit.com/canvas-receiver/`
3. Use the App ID in your sender application

### Local Development

```bash
# Clone the repository
git clone https://github.com/pigeek/uijit.git
cd uijit

# Serve locally (any static server works)
python -m http.server 8000
# or
npx serve .
```

## Repository Structure

```
uijit/
├── README.md              # This file
├── index.html             # Landing page
└── canvas-receiver/
    └── index.html         # Cast receiver application
```

## Related Projects

- [canvas-mcp](https://github.com/user/canvas-mcp) - MCP server for canvas management
- [androidtvmcp](https://github.com/pigeek/androidtvmcp) - MCP server for Android TV control
- [A2UI](https://github.com/user/A2UI) - Agent-to-User Interface protocol

## License

MIT
