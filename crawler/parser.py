import crawler
from utils import normalize_gender, normalize_species
from bs4 import BeautifulSoup, SoupStrainer, Tag

async def parse_pages() -> dict:
    champions_slugs: list = await crawler.get_champions_slugs()
    raw_pages: list = await crawler.get_champions_pages(champions_slugs)

    champion_infobox = SoupStrainer("div", class_="infobox champion-upd")
    universe_infobox = SoupStrainer("div", class_="infobox theme-client")

    schema_list = []

    for i, v in enumerate(champions_slugs):
        soup_wiki = BeautifulSoup(raw_pages[i][v]["wiki"], "lxml", parse_only=champion_infobox)
        soup_universe = BeautifulSoup(raw_pages[i][v]["universe"], "lxml", parse_only=universe_infobox)

        schema_list.append(
            {
                "name": v,
                "role": get_role(soup_wiki),
                "release_date": get_field("Release date", soup_wiki).split("-")[0],
                "resource": get_field("Resource", soup_wiki),
                "range_type": get_field("Range type", soup_wiki),
                "species": normalize_species(get_list_field("Species", soup_universe)),
                "pronouns": normalize_gender(get_field("Pronoun", soup_universe)),
                "regions": get_list_field("Region", soup_universe)
            }
        )

    return schema_list

def get_label(text: str, soup: BeautifulSoup) -> Tag | str:
    # bs4 'string' param won't work with <small> tags, so im manually checking if a tag exist
    for div in soup.find_all("div", class_="infobox-data-label"):
        if text.lower() in div.get_text().lower():
            return div
    return None

def get_role(soup: BeautifulSoup) -> str:
    for label in soup.find_all("span", id="champinfo-container"):
        if "Role" in label.text:
            glossary = label.find_next_sibling("span", class_="glossary")
            if glossary:
                for a in glossary.find_all("a"):
                    if a.text.strip():
                        return a.text.strip()
    return "Undefined"

def get_field(label: str, soup: BeautifulSoup) -> str:
    row = get_label(label, soup)
    if not row:
        return f"{label} not found!"
    value: str = row.find_next_sibling("div", class_="infobox-data-value").text.strip()
    return value.split("(")[0].strip()

def get_list_field(label: str, soup: BeautifulSoup) -> list[str]:
    row = get_label(label, soup)
    if not row:
        return []
    value_div = row.find_next_sibling("div", class_="infobox-data-value")
    results = []
    if value_div.find_all("li"):
        for li in value_div.find_all("li"):
            if not li.find("s"):
                results.append(li.text.strip().split("(")[0].strip())
    else:
        for a in value_div.find_all("a"):
            if a.text.strip():
                results.append(a.text.strip())

    return results
