# biedraScraper 
`biedraScraper` is a simple Python script to scrap the newest prices from [zakupy.biedronka.pl](https://zakupy.biedronka.pl) using Selenium and save them to XLSX file using Pandas.


## Requirements

- Python 3.x

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/mcjmk/biedraScraper.git
    cd biedraScraper
    ```
2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
    ```bash
    venv\Scripts\activate
    ```
    - On macOS and Linux:
    ```bash
    source venv/bin/activate
    ```

4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage 
1. Run the script:
    ```bash
    python biedraScraper.py
    ```
2. Check the output file: 

    After running the script, the scraped prices will be saved in the `biedra_{today}.xlsx`. Enjoy! :)
