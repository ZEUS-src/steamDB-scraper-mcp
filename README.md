
###

<div align="center">
  <img src="https://img.shields.io/static/v1?message=LinkedIn&logo=linkedin&label=&color=0077B5&logoColor=white&labelColor=&style=for-the-badge" height="25" />
  <img src="https://img.shields.io/static/v1?message=Youtube&logo=youtube&label=&color=FF0000&logoColor=white&labelColor=&style=for-the-badge" height="25" />
  <img src="https://img.shields.io/static/v1?message=Twitter&logo=twitter&label=&color=1DA1F2&logoColor=white&labelColor=&style=for-the-badge" height="25" />
</div>

###

<div align="center">
  <img src="https://visitor-badge.laobi.icu/badge?page_id=ZEUS-src.steamDB-scraper-mcp" />
</div>

###

<h1 align="center">steamDB Scraper - MCP Server 🕹️</h1>

###

<h3 align="left">❓ What is MCP?</h3>

<p align="left">
<b>Model Context Protocol (MCP)</b> is an open standard that enables AI assistants to securely connect with external data sources and tools. MCP servers act as bridges between AI models and various services, allowing for enhanced capabilities like real-time data access, API integrations, and custom tool execution.
</p>

###

<h3 align="left">👩‍💻 About The Project</h3>

<p align="left">
This is a fast, flexible scraping tool built with <strong>SeleniumBase</strong> to automate and extract game data from <a href="https://steamdb.info">SteamDB</a>.<br><br>

⚠️ <strong>Note:</strong> This project uses <strong>SeleniumBase</strong> to bypass <strong>Cloudflare protections</strong>, ensuring reliable access to protected pages.<br><br>

It allows you to:
<ul>
  <li>🔎 Search for specific games</li>
  <li>📦 Or scrape all available games at once</li>
  <li>💾 Save results as clean <code>.csv</code> or <code>.parquet</code> files</li>
</ul>
</p>

###

<h3 align="left">⚙️ Technologies Used</h3>

<div align="left">

<img src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=white" height="28" />
<img src="https://img.shields.io/badge/SeleniumBase-43B02A?style=for-the-badge&logo=selenium&logoColor=white" height="28" />
<img src="https://img.shields.io/badge/BeautifulSoup-FFC107?style=for-the-badge&logo=beautifulsoup&logoColor=black" height="28" />
<img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" height="28" />
<img src="https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white" height="28" />

</div>

###

<h3 align="left">📦 Features</h3>

- ✅ Uses [SeleniumBase](https://github.com/seleniumbase/SeleniumBase) to bypass Cloudflare  
- ✅ Extracts real-time Steam game data  
- ✅ Allows filtering or full scrape  
- ✅ Saves as CSV or Parquet  
- ✅ Easily integratable with MCP

### 🛠 Installation

> **Prerequisites:**  
> - Chrome browser installed  
> - Git installed
<h3 align="left">🐍 Local Setup (Develop & Contribute)</h3>


```bash
# 1. Clone repository
git clone https://github.com/ZEUS-src/steamDB-scraper-mcp.git
cd steamDB-scraper-mcp

# 2. Install UV package manager
curl -LsSf https://astral.sh/uv/install.sh | sh
uv python  # Install Python via UV if you don’t already have it

# 3. Install dependencies
uv sync
uv sync --group dev  # Install dev dependencies

# 4. Install pre-commit hooks
uv run pre-commit install

# 5. Start the server manually for first time (non-headless)
uv run main.py --no-headless --no-lazy-init
```

...

---

<h3 align="left">🧠 Claude Integration</h3>

To use this scraper MCP server inside the Claude desktop app:

1. Go to: **Claude → Settings → Developer → Edit Config**
2. Add the following configuration to your `claude_desktop_config.json` file:

```json
// claude_desktop_config.json
{
  "mcpServers": {
      "SteamDB_MCP": {
        "command": "uv",
        "args": [
          "--directory",
          "/<Absolute-path-to-folder>/SteamDB_MCP",
          "run",
          "main.py"
        ]
      }
  }
  }
