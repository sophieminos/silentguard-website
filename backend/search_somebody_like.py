import requests, json

def get_api_key_google():
    return "AIzaSyA3TuIANXlP4ZOFS34bAE2q0BZyWeKdElE"

def get_cse_id():
    return "a04e3ae5247164828"

def get_hibp_api_key():
    return "884eb0be459744129082410c71ded598"

def build_query(infos, file_type=None):
    base_query = f'"{infos["first_name"]} {infos["last_name"]}"'
    return base_query

def search_google_api(query, api_key, cse_id):
    url = "https://www.googleapis.com/customsearch/v1"
    all_results = []
    start_index = 1
    max_results = 10  # Nombre maximum de résultats retournés
    links = {}
    count = 0

    while count < max_results:
        params = {
            "q": query,
            "key": api_key,
            "cx": cse_id,
            "start": start_index,
            "num": 10,
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if "items" in data:
                for site in data["items"]:
                    link = site["link"]
                    # Inclure LinkedIn France ou tout autre lien
                    if "linkedin.com" in link:
                        if "fr." in link:
                            count += 1
                            links[f"lien google {count}"] = link
                    else:
                        count += 1
                        links[f"lien google {count}"] = link

                    # Arrêter lorsque 10 résultats valides sont atteints
                    if count >= max_results:
                        break
            # Arrêter si aucune page suivante n'est disponible
            if "nextPage" not in data.get("queries", {}):
                break
        else:
            print(f"Erreur API Google : {response.status_code}")
            break

        start_index += 10

    return links




def search_sites_by_pseudo(pseudo):
    """Recherche des informations sur un pseudo spécifique sur des sites connus."""
    sites_to_search = [
        f"https://github.com/{pseudo}",
        f"https://twitter.com/{pseudo}",
        f"https://x.com/{pseudo}",
        f"https://www.linkedin.com/in/{pseudo}",
        f"https://www.reddit.com/user/{pseudo}",
        f"https://archive.org/details/@{pseudo}",
        f"https://{pseudo}.blogspot.com",
        f"https://www.9gag.com/u/{pseudo}",
        f"https://www.cnet.com/profiles/{pseudo}/",
        f"https://www.chess.com/member/{pseudo}",
        f"https://www.dailymotion.com/{pseudo}",
        f"https://www.dealabs.com/profile/{pseudo}",
        f"https://{pseudo}.deviantart.com",
        f"https://hub.docker.com/u/{pseudo}/",
        f"https://www.duolingo.com/profile/{pseudo}",
        f"https://www.fiverr.com/{pseudo}",
        f"https://www.flickr.com/people/{pseudo}",
        f"https://my.flightradar24.com/{pseudo}",
        f"https://auth.geeksforgeeks.org/user/{pseudo}",
        f"https://giphy.com/{pseudo}",
        f"https://gitlab.com/{pseudo}",
        f"https://buzzfeed.com/{pseudo}",
        f"https://forum.hackthebox.com/u/{pseudo}",
        f"https://imgur.com/user/{pseudo}",
        f"https://play.google.com/store/apps/developer?id={pseudo}",
        f"https://letterboxd.com/{pseudo}",
        f"https://myspace.com/{pseudo}",
        f"https://help.nextcloud.com/u/{pseudo}/summary",
        f"https://www.nintendolife.com/users/{pseudo}",
        f"https://www.patreon.com/{pseudo}",
        f"https://rarible.com/marketplace/api/v4/urls/{pseudo}",
        f"https://www.researchgate.net/profile/{pseudo}",
        f"https://www.scribd.com/{pseudo}",
        f"https://{pseudo}.slack.com",
        f"https://www.snapchat.com/add/{pseudo}",
        f"https://soundcloud.com/{pseudo}",
        f"https://sourceforge.net/u/{pseudo}",
        f"https://open.spotify.com/user/{pseudo}",
        f"https://steamcommunity.com/groups/{pseudo}",
        f"https://steamcommunity.com/id/{pseudo}/",
        f"https://t.me/{pseudo}",
        f"https://trello.com/{pseudo}",
        f"https://tryhackme.com/p/{pseudo}",
        f"https://www.twitch.tv/{pseudo}",
        f"https://api.mojang.com/users/profiles/minecraft/{pseudo}",
        f"https://vimeo.com/{pseudo}",
        f"https://en.wikipedia.org/wiki/Special:CentralAuth/{pseudo}?uselang=qqx",
        f"https://{pseudo}.wix.com",
        f"https://{pseudo}.wordpress.com/",
        f"https://profiles.wordpress.org/{pseudo}/",
        f"https://xboxgamertag.com/search/{pseudo}",
        f"https://www.youtube.com/@{pseudo}",
        f"https://www.geocaching.com/p/default.aspx?u={pseudo}",
        f"https://gfycat.com/@{pseudo}",
        f"https://last.fm/user/{pseudo}",
        f"https://mastodon.social/@{pseudo}",
        f"https://{pseudo}.skyrock.com/",
        f"https://www.threads.net/@{pseudo}",
        f"https://vk.com/{pseudo}",
    ]

    results = {}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    num = 1
    for idx, site in enumerate(sites_to_search, start=1):
        try:
            response = requests.get(site, headers=headers, timeout=5)
            if response.status_code == 200:
                results[f"lien avec pseudo {num}"] = site
                num += 1
        except requests.exceptions.RequestException:
            pass

    return results

def search_email_breaches(email):
    """Recherche si une adresse e-mail a été compromise via l'API Have I Been Pwned."""
    api_key = get_hibp_api_key()
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {
        "hibp-api-key": api_key,
        "user-agent": "Python-SearchSomebody-App"
    }
    results = {}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            num = 1
            for idx, breach in enumerate(response.json(), start=1):
                results[f"fuite {num}"] = breach['Name']
                num += 1       
    except requests.exceptions.RequestException:
        pass

    return results

def search_somebody_like(first_name, last_name, pseudo="", email=""):
    api_key = get_api_key_google()
    cse_id = get_cse_id()
    infos = {
        "first_name": first_name,
        "last_name": last_name,
        "pseudo": pseudo,
    }

    results = {}

    # Partie 1 : Recherche via Google API
    query = build_query(infos)
    google_results = search_google_api(query, api_key, cse_id)
    results.update(google_results)

    # Partie 2 : Recherche directe par pseudo
    if pseudo:
        pseudo_results = search_sites_by_pseudo(pseudo)
        results.update(pseudo_results)

    # Partie 3 : Recherche par e-mail
    if email:
        email_results = search_email_breaches(email)
        results.update(email_results)

    return results

def main():
    first_name = ""
    last_name = ""
    pseudo = ""
    email = ""
    print(search_somebody_like(first_name, last_name, pseudo, email))

if __name__ == "__main__":
    main()
