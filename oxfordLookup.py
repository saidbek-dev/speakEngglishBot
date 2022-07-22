import requests

app_id = "974061c5"
app_key = "e54ac9f8faf489955ad6b25c06ca9fc0"
language = "en-gb"

def getDefinitions(word_id):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    res = r.json()
    if 'error' in res.keys():
        return False

    output = {}
    senses = res['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
    definitions = []
    for i,j in enumerate(senses):
        definitions.append(f"{i+1}. {j['definitions'][0].capitalize()}.")
    output['definitions'] = '\n'.join(definitions)

    if res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):
        output['audio'] = res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']

    return output

if __name__=="__main__":
    from pprint import pprint as print
    print(getDefinitions('Great Britain'))
    print(getDefinitions('amevfad'))