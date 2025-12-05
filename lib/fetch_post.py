import requests  # external package installed with pip

def fetch_data():
    # Send a GET request to a free API
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    # If the request was successful (status code 200), return the JSON data
    if response.status_code == 200:
        return response.json()
    else:
        # If something goes wrong, return an empty dictionary
        return {}

# This block ensures the code only runs when the script is executed directly
if __name__ == "__main__":
    post = fetch_data()  # call the function

    # Print the title from the returned data
    print("Fetched Post Title:", post.get("title", "No title found"))