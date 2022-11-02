'''
File containing functions for manipulating Freebase related stuff
'''

import requests


def query_freebase_id_from_wikidata(id: str) -> any:
    '''
    Queries wikidata for the value associated to the freebase id

    :param id: the freebase id to query for

    :return: the associated value, None if could not be found
    '''
    # query as suggested in https://edstem.org/eu/courses/134/discussion/3845
    query = "https://query.wikidata.org/bigdata/namespace/wdq/sparql?format=json&query=PREFIX%20wd%3A%20%3Chttp%3A%2F%2Fwww.wikidata.org%2Fentity%2F%3E%0APREFIX%20wdt%3A%20%3Chttp%3A%2F%2Fwww.wikidata.org%2Fprop%2Fdirect%2F%3E%0APREFIX%20wikibase%3A%20%3Chttp%3A%2F%2Fwikiba.se%2Fontology%23%3E%0A%0ASELECT%20%20%3Fs%20%3FsLabel%20%3Fp%20%20%3Fo%20%3FoLabel%20WHERE%20%7B%0A%20%3Fs%20wdt%3AP646%20%22%2Fm%2F" + \
        id[3:]+"%22%20%0A%0A%20%20%20SERVICE%20wikibase%3Alabel%20%7B%0A%20%20%20%20bd%3AserviceParam%20wikibase%3Alanguage%20%22en%22%20.%0A%20%20%20%7D%0A%20%7D"

    # set a user-agent to avoid error code 429
    response = requests.get(
        query, headers={'User-agent': 'freebsd id finder 9000'})

    if response.ok:
        response = response.json()
    else:
        print("ERROR: error code {} for {}".format(response.status_code, id))
        return None

    result = response['results']['bindings']

    if len(result) == 0:
        return None
    elif len(result) > 1:
        print("weird result for {}".format(id))
        print(result)
        print()

    try:
        value = result[0]['sLabel']['value']
    except:
        print("result contained no value for {}".format(id))
        print(result)
        print()
        value = None

    return value
