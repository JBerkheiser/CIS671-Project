import time
import os
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

host = "https://apinext.collegefootballdata.com"
apiKeyFile = "apikey.txt"
apiKey = ""
with open(apiKeyFile, 'r') as keyFile:
    apiKey = keyFile.read()

configuration = cfbd.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)


# Enter a context with an instance of the API client
with cfbd.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cfbd.AdjustedMetricsApi(api_client)
    year = 56 # int | Optional year filter (optional)
    team = 'team_example' # str | Optional team filter (optional)
    conference = 'conference_example' # str | Optional conference abbreviation filter (optional)
    position = 'position_example' # str | Optional position abbreviation filter (optional)

    try:
        api_response = api_instance.get_adjusted_player_passing_stats(year=year, team=team, conference=conference, position=position)
        print("The response of AdjustedMetricsApi->get_adjusted_player_passing_stats:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdjustedMetricsApi->get_adjusted_player_passing_stats: %s\n" % e)
