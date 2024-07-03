import json
import urllib.request
import csv
from datetime import datetime

apikey = " "

# List of banks to search for
banks = ['HDFC', 'SBI', 'ICICI', 'Kotak', 'IDFC', 'Axis']


for bank in banks:
    # Construct the API URL for each bank with date range
    url = f"https://gnews.io/api/v4/search?q={bank}&lang=en&country=in&max=45&apikey={apikey}"

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode("utf-8"))
        articles = data["articles"]

        # Specify the CSV file name for each bank
        csv_file_name = f"{bank}_news.csv"

        # Open the CSV file in append mode
        with open(csv_file_name, mode='a', newline='', encoding='utf-8') as csv_file:
            # Create a CSV writer object
            csv_writer = csv.writer(csv_file)

            # If the file is empty, write the header row
            if csv_file.tell() == 0:
                csv_writer.writerow(['Bank', 'Title', 'Description', 'Published At'])

            # Write data for each bank to the CSV file
            for article in articles:
                title = article['title']
                description = article['description']
                published_at = article['publishedAt']

                # Write the data to the CSV file
                csv_writer.writerow([bank, title, description, published_at])

                # Print the data to the console
                print(f"Bank: {bank}")
                print(f"Title: {title}")
                print(f"Description: {description}")
                print(f"Published At: {published_at}")
                print("--------")

            # Inform the user about the CSV file update
            print(f"New data for {bank} has been added to {csv_file_name}")

