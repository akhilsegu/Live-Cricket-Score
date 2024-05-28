# Live Cricket Score

This Python script scrapes live cricket scores from the Cricbuzz website for a specific match in the Indian Premier League (IPL) 2021. It continuously fetches the score and prints it to the console.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- BeautifulSoup4 (`pip install beautifulsoup4`)
- Requests (`pip install requests`)

## Usage

1. Clone or download this repository to your local machine.

2. Navigate to the directory containing the script.

3. Run the script using the following command:
   python live_cricket_score_scraper.py

4. The script will start fetching the live score and print it to the console. It will continue to do so until you interrupt the process (e.g., by pressing Ctrl+C).

## Customization

If you want to scrape the live score of a different match, you can modify the `url` variable in the script to the desired match URL from the Cricbuzz website.

## Important points

- The script fetches the live score every 20 seconds. You can adjust the interval by modifying the `time.sleep(20)` line in the script.

- Ensure that you use this script responsibly and respect the website's terms of service. Excessive scraping may lead to IP bans or other restrictions.



