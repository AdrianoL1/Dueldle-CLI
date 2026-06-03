import asyncio
import typer
from rich.progress import Progress, SpinnerColumn, TextColumn
from crawler.parser import parse_pages
from api import bulk_insert

app = typer.Typer()

@app.command()
def crawl_and_post():
    with Progress(SpinnerColumn(), TextColumn("{task.description}")) as progress:
        progress.add_task("Fetching and parsing champions...", total=None)
        results = asyncio.run(parse_pages())

    with Progress(SpinnerColumn(), TextColumn("{task.description}")) as progress:
        progress.add_task("Sending to API...", total=None)
        asyncio.run(bulk_insert(results))

    typer.echo(f"\nDone. {len(results)} champions parsed.")

if __name__ == "__main__":
    app()
