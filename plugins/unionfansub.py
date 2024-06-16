#!/usr/bin/env python
# VERSION: 1.2
# AUTHORS: Koba (CrimsonKoba@protonmail.com)
import os
import tempfile
from configparser import ConfigParser
from urllib import request
from urllib.error import URLError
from urllib.parse import urlencode
from http.cookiejar import CookieJar
from html.parser import HTMLParser

# qtbittorrent
from novaprinter import prettyPrinter
from helpers import retrieve_url


def configuration() -> (dict | None):
    config_file_name = ".uft.ini"
    config_dir = os.path.expanduser("~")
    config_file_path = os.path.join(config_dir, config_file_name)

    config_parser = ConfigParser()

    if os.path.isfile(config_file_path):
        config_parser.read(config_file_path)
        username = config_parser.get("login", "usuario", fallback="")
        password = config_parser.get("login", "contraseña", fallback="")
        return {"username": username, "password": password}
    else:
        config_parser["login"] = {"usuario": "", "contraseña": ""}
        with open(config_file_path, "w") as config_file:
            config_parser.write(config_file)
        return


class Parser(HTMLParser):
    def __init__(self, url):
        super().__init__()

        self.url = url
        self.current_res = {}
        self.current_item = None
        self.in_table = False

    def handle_starttag(self, tag, attrs):
        attr = dict(attrs)

        self.in_table = self.in_table or tag == "table"
        if not self.in_table:
            return

        if tag == "span":
            self.current_item = None

        if attr.get("class") == "name" and tag == "b":
            self.current_item = "name"

        if tag == "a" and "href" in attr:
            link = attr.get("href")

            if link is not None:
                if link.startswith("peerlist.php"):
                    if link.endswith("leechers"):
                        self.current_item = "leech"
                    else:
                        self.current_res["leech"] = 0

                if link.startswith("details.php") and link.endswith("hit=1"):
                    dl = link[:-6].replace("details.php?id=", "download.php?torrent=")
                    self.current_res["link"] = self.url + dl + "&aviso=1"
                    self.current_res["desc_link"] = self.url + link[:-6]
                    self.current_res["engine_url"] = self.url

        if tag == "font":
            if attr.get("color", "#000000"):
                self.current_item = "seeds"
            else:
                self.current_res["seeds"] = 0

    def handle_data(self, data):
        if not self.in_table:
            return

        if self.current_item == "name":
            self.current_res[self.current_item] = data
        if data.endswith("GB") or data.endswith("MB"):
            self.current_res["size"] = data.strip().replace(",", ".")
        if self.current_item == "seeds" and data != "\n":
            self.current_res[self.current_item] = data
        if self.current_item == "leech" and data != "\n":
            self.current_res[self.current_item] = data

    def handle_endtag(self, tag):
        if tag == "table":
            self.in_table = False
        if not self.in_table:
            return

        if tag == "font":
            self.current_item = None

        if self.current_res and tag == "tr":
            prettyPrinter(self.current_res)
            self.current_res = {}
            self.current_item = None


class unionfansub:
    url = "https://torrent.unionfansub.com/"
    name = "Union Fansub"
    supported_categories = {
        "all": "0",
        "tv": "9",
        "anime": "1",
        "movies": "15",
        "music": "16",
        "games": "18",
        "software": "11",
    }

    def __init__(self):
        config = configuration()
        if config is None:
            return
        self._login(config["username"], config["password"])

    def _login(self, username, password):
        login_url = "https://foro.unionfansub.com/member.php?action=login"

        params = urlencode(
            {
                "username": username,
                "password": password,
                "submit": "Iniciar+sesión",
                "action": "do_login",
            }
        ).encode("utf-8")

        header = {
            "Connection": "keep-alive",
            "User-Agent": "qBittorrent/4",
        }

        cj = CookieJar()
        session = request.build_opener(request.HTTPCookieProcessor(cj))

        try:
            session.open(request.Request(login_url, params, header))
            self.session = session
        except URLError as e:
            print("Error al conectarse: {}".format(e.reason))

    def search(self, what, cat="all"):
        categ = self.supported_categories.get(cat)
        url = "{0}browse.php?search={1}&c{2}".format(self.url, what, categ)

        page = 0
        results = []
        parser = Parser(self.url)

        while page <= 10:
            html = retrieve_url(url + "&page=" + str(page))
            parser.feed(html)
            if len(results) < 1:
                break
            del results[:]
            page += 1

        parser.close()

    def download_torrent(self, url):
        f, path = tempfile.mkstemp(".torrent")

        with self.session.open(url) as response:
            file = open(f, "wb")
            file.write(response.read())
            file.close()

        print(f"{path} {url}")
