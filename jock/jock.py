import requests

def get_random_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    response = requests.get(url)
    data = response.json()
    if data["type"] == "single":
        return data["joke"]
    else:
        return f'{data["setup"]}\n{data["delivery"]}'

if __name__ == "__main__":
    joke = get_random_joke()
    print("Here's a random joke for you:")
    print(joke)