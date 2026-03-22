# Biedra Scraper

`biedraScraper` is a simple Selenium-based CLI for collecting current prices from
[zakupy.biedronka.pl](https://zakupy.biedronka.pl) and saving them to a spreadsheet.
You can use that information to analyze prices or optimize your expenses.



## Usage

Run the scraper:

```bash
uv run biedrascraper
```

The scraper will fetch the configured categories and write the results to a file
named `biedra_{today}.xlsx` in the project directory.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/menzhik/biedra-scraper.git
   cd biedra-scraper
   ```

2. Sync dependencies:
   ```bash
   uv sync --all-groups
   ```

## Requirements

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) package manager
- Google Chrome or Chromium installed locally

Core dependencies (managed by uv):
- numpy 2.2.2+
- openpyxl 3.1.5+
- pandas 2.2.3+
- selenium 4.41.0+

## Quality Checks

```bash
uv run mypy
uv run ruff check .
uv run ruff format --check .
```

## Project Structure

The code is split into a few files in the `src/biedrascraper` directory:

- `config.py` - URL and category configurations
- `fetch.py` - scraping logic using Selenium
- `save.py` - saving data to different formats
- `main.py` - main script that puts it all together
