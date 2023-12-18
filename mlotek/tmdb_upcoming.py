import sys,os
import json
import requests as req


def tmdb_api_call(requestURL, parameters):
    response = req.get(url=requestURL,params=parameters)
if response.status_code != 200:
    print(response.json())
    exit()
data = response.json()
return json.dumps(data)

def get_upcoming_movies_by_page(api_key, page_number=1):
    requestURL = "https://api.themoviedb.org/3/movie/upcoming"
    parameters = {"api_key" : api_key, "page" : page_number }
    return tmdb_api_call(requestURL,parameters)


    def main():
        api_key = "dffbd398yt434wijhfeo9hf9owo"
        checkpoint_file = os.path.join(os.environ["SPLUNK_HOME"],'etc','apps','bin','checkpoint','checkpoint.txt')
        upcoming_movie_list = get_upcoming_movies_by_page(api_key,1)
        data = json.dumps(upcoming_movie_list)
        stream_to_splunk(checkpoint_file, data["results"])

if __name__ == "__main__":
    main()