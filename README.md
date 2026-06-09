![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![BS4](https://img.shields.io/badge/BeautifulSoup-green?style=for-the-badge&logo=python)

# Dueldle CLI

A command-line ETL application developed with **Python** that automates the process of crawling, transforming, validating, and importing champion data into the Dueldle API.

## Features

* Asynchronous web crawling using `aiohttp`
* HTML parsing with `BeautifulSoup4` and `lxml`
* Data validation and serialization with `Pydantic`
* Bulk insertion of champions into the Dueldle API
* Interactive CLI built with `Typer`
* Rich terminal feedback using `Rich`
* ETL pipeline following the Extract → Transform → Load workflow

## Technologies Used

* Python 3
* aiohttp
* BeautifulSoup4
* lxml
* Pydantic
* Typer
* Rich
* python-dotenv

## Project Structure

* **crawler**: Responsible for fetching and parsing champion data from external sources.
* **models**: Contains Pydantic models used for validation and serialization.
* **utils**: Utility functions for data conversion and transformation.
* **api**: Handles communication with the Dueldle API.
* **main.py**: CLI entry point that orchestrates the ETL process.

## ETL Workflow

1. **Extract**

   * Retrieve champion data from external sources.

2. **Transform**

   * Parse and normalize the collected information.
   * Convert raw values into the format expected by the API.
   * Validate data through Pydantic models.

3. **Load**

   * Send validated champion data to the Dueldle API using bulk requests.

## Running the Project Locally

1. **Clone the repository**

   ```bash
   git clone https://github.com/AdrianoL1/Dueldle-CLI.git
   cd Dueldle-CLI
   ```

2. **Create and activate a virtual environment**

   Linux/macOS:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

   Windows:

   ```powershell
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   Create a `.env` file and provide the required API configuration.

5. **Run the ETL process**

   ```bash
   python main.py crawl-and-post
   ```

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is open-source and available under the MIT License.
