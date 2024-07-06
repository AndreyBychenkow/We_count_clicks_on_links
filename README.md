# Description
This script allows you to shorten links via the VK API and get view statistics for already shortened links.

## Installation

1. ### Create a virtual environment and activate it:

`python -m venv venv`

`source venv/bin/activate`  # Для Linux/Mac

`venv\Scripts\activate`  # Для Windows

2. ### Install dependencies:

`pip install -r requirements.txt`

3. ### Create a `.env` file in the root directory of the project and add your VK access token to it:

`echo ACCESS_TOKEN=your_access_token_vk > .env`

## Usage

### Run the script with the command:

`python Counting clicks.py`

### Follow the instructions in the console:

1. Enter the link when prompted.
2. If the link has already been shortened, you will see the number of views.
3. If the link is not shortened, you will receive a new shortened link.

## Checking the result

- To check the link shortening:
 * Enter a long link (for example, https://www.example.com)
 * You should see the message "Shortened link: https://vk.cc/XXXXXX"
 
- To check statistics:
 * Enter the previously shortened link (for example, https://vk.cc/XXXXXX)
 *You should see the message "Number of views: X"
 
 **If you see these messages, then the script is working correctly.**
 
 ## Troubleshooting
 
**If you receive an authorization error, make sure that:**
1. The `.env` file was created correctly
2. The `.env` file contains a valid VK access token
3. The token has the necessary access rights (utils)

## Notes

* This script assumes you have a valid VK API access token.

* It distinguishes between input URLs to either shorten them or fetch statistics based on whether they are VK short links (vk.cc).

* Error handling is provided for failed API requests or invalid URLs.

 
 
