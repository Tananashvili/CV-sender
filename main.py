import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from msgsender import send_email
import time


def get_statement_info():
    df = pd.read_excel("urls.xlsx")
    urls = df["urls"].tolist()
    positions = []
    i = 1

    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        try:
            header = soup.select_one("div#job > span").text.replace("\n", " ")
        except AttributeError:
            header = ""
        try:
            email = soup.find_all("a", href=re.compile(r"mailto:"))[0].text
        except IndexError:
            email = ""

        positions.append({"url": url, "header": header, "email": email})
        print(f"{i}/{len(urls)}")
        i += 1

    df = pd.DataFrame(positions)
    df.to_excel("positions.xlsx", index=False)


def send_emails():
    key_word = "მონაცემთა"  # INPUT YOUR DESIRED KEY WORD IN POSITIONS
    df = pd.read_excel("positions.xlsx")
    num_rows = df.shape[0]
    i = 1
    for index, row in df.iterrows():
        to_email = row["email"]
        subject = row["header"]
        
        if key_word in subject:
            send_email(to_email, subject)
            print(f"Sent {i}")
            i += 1
            time.sleep(2)

if __name__ == "__main__":
    send_emails()
