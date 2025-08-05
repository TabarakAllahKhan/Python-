import requests


url = " https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=e428bffeb69e4f519041a85d7a4a5503"

response=requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Check if the 'articles' key exists and is a list
    if 'articles' in data and isinstance(data['articles'], list):
        # Iterate over each article in the 'articles' list
        for article in data['articles']:
            # Access the 'title' and 'description' keys from each article dictionary
            title = article.get('title')
            description = article.get('description')

            # Print the title and description, checking for None values
            if title:
                print(f"Title: {title}")
            if description:
                print(f"Description: {description}\n")  # Add a newline for better readability
    else:
        print("The 'articles' key was not found or is not a list in the response.")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    # Print the full response text for more details if the status code is not 200
    print(response.text)

