# Ouput wikidata containing social media followers for chain food places

import pandas as pd
import requests

def wiki_foodchains():
    # https://ramiro.org/notebook/us-presidents-causes-of-death/
    query = '''PREFIX wikibase: <http://wikiba.se/ontology#>
    PREFIX wd: <http://www.wikidata.org/entity/>
    PREFIX wdt: <http://www.wikidata.org/prop/direct/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

    SELECT ?restaurant ?followers WHERE {
        VALUES ?storetype {wd:Q18534542 wd:Q18509232}
        ?pid wdt:P31 ?storetype .
        ?pid wdt:P8687 ?followers .

        OPTIONAL {
            ?pid rdfs:label ?restaurant filter (lang(?restaurant) = "en") .
        }
        OPTIONAL {
            ?cid rdfs:label ?followers filter (lang(?followers) = "en") .
        }
    }'''

    url = 'https://query.wikidata.org/bigdata/namespace/wdq/sparql'
    data = requests.get(url, params={'query': query, 'format': 'json'}).json()

    # it would be desirable to use 'from_dict' here, but dtype cannot be set to 'dict'
    chain_foods = []
    for item in data['results']['bindings']:
        chain_foods.append({
            'name': item['restaurant']['value'],
            'followers': item['followers']['value']})

    wiki_df = pd.DataFrame(chain_foods)
    wiki_df['followers'] = (wiki_df['followers']).astype(int)
    wiki_df.to_csv('wiki_foodchains.csv')

