
from seleniumbase import sb_cdp
from bs4 import BeautifulSoup
import pandas as pd
import os

class SteamDB:
    def __init__(self):
        self.all_tables = []
    def __reset_tables__(self):
        """
        Reset the tables
        """
        self.all_tables = []

    def openBrowser(self):
        """ 
        Open the browser and navigate to the SteamDB charts page and show all Games DB.
        """
        url = "https://steamdb.info/charts/"
        sb = sb_cdp.Chrome(url, lang="en")
        sb.sleep(2.5)
        sb.internalize_links()
        sb.select_option_by_text("#dt-length-0", "All")
        sb.sleep(1)
        self.__parser_all(sb.get_page_source())
        self.total_games = len(self.rows)

    def __parser_all(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        # Save all <tr> elements inside #table-apps > tbody
        self.rows = soup.select("#table-apps > tbody > tr")

    def parser_one_by_rank(self, num_tr):
        """
        Parse the data from SteamDB with the given index (index start from 1)
        """
        tr = self.rows[num_tr]
        appid = tr.get("data-appid")
        cells = tr.find_all("td")
        parsed = {"rank": cells[0].get_text(strip=True).replace(".", ""),
                  "name": cells[2].get_text(strip=True),
                  "Current": cells[3].get_text(strip=True),
                  "24h_Peak": cells[4].get_text(strip=True),
                  "All-Time_Peak": cells[4].get_text(strip=True),
                  "appid": appid}
        self.all_tables.append(parsed)
        return parsed

    def parser_one_by_appid(self, aID:str):
        """
        Parse the data from SteamDB with the given appid
        """
        for tr in self.rows:
            appid = tr.get("data-appid")
            if aID == appid:
                cells = tr.find_all("td")
                parsed_rows  = [cell.get_text(strip=True) for cell in cells]
                row = {
                    "rank": parsed_rows[0].replace(".", ""),
                    "name": parsed_rows[2],
                    "Current": parsed_rows[3],
                    "24h_Peak": parsed_rows[4],
                    "All-Time_Peak": parsed_rows[5],
                    "appid": appid
                }
                self.all_tables.append(row)
                return row
        return {}

    def parser_one_by_name(self, name: str):
        """
        Parse the data from SteamDB with the given game name
        """
        for tr in self.rows:
            appid = tr.get("data-appid")
            cells = tr.find_all("td")

            parsed_rows  = [cell.get_text(strip=True) for cell in cells]
            if parsed_rows[2].lower() == name.lower():
                row = {
                    "rank": parsed_rows[0].replace(".", ""),
                    "name": parsed_rows[2],
                    "Current": parsed_rows[3],
                    "24h_Peak": parsed_rows[4],
                    "All-Time_Peak": parsed_rows[5],
                    "appid": appid
                }
                self.all_tables.append(row)
                return row
        return {}

    def save_to_csv(self, filename: str="steamDB.csv"):
        """
        Save the data to a csv file
        """
        os.makedirs("Result", exist_ok=True)
        # Save DataFrame
        df = pd.DataFrame(self.all_tables)
        df.to_csv(f"Result/{filename}", index=False, encoding='utf-8-sig')
        return f"Saved {len(self.all_tables)} games to {filename}"

    def save_to_parquet(self, filename: str="steamDB.parquet"):
        """
        Save the data to a parquet file
        """
        os.makedirs("Result", exist_ok=True)
        # Save DataFrame
        df = pd.DataFrame(self.all_tables)
        df.to_parquet(f"Result/{filename}", index=False, encoding='utf-8-sig')
        return f"Saved {len(self.all_tables)} games to {filename}"