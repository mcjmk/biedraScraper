# biedraScraper 
`biedraScraper` is a simple Python script to scrap the newest prices from [zakupy.biedronka.pl](https://zakupy.biedronka.pl) using Selenium and save them to XLSX file using Pandas.


## Requirements
- Python 3.11+
- [uv](https://github.com/astral-sh/uv) package manager

Core dependencies (managed by uv):
- numpy 2.2.2+
- openpyxl 3.1.5+
- pandas 2.2.3+
- selenium 4.28.1+

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mcjmk/biedraScraper.git
   cd biedraScraper
   ```

2. Set up environment and install dependencies:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv sync
   ```

## Usage 

```bash
uv run src/biedrascraper/main.py
```

After running the script, the scraped prices will be saved in the `biedra_{today}.xlsx`. Enjoy! :)

## Project Structure

The code is split into a few files in the `src/biedrascraper` directory:

- `config.py` - URL and category configurations
- `fetch.py` - scraping logic using Selenium
- `save.py` - saving data to different formats
- `main.py` - main script that puts it all together