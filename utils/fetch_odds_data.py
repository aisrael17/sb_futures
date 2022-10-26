from dotenv import load_dotenv
import json
import os


# Load environment and get API data
def get_req_url(cat, api_key, regions='us'):
	"""
	Given a category, region, and API Key, returns a string that can be 
	used to make an API call to The Odds API
	"""
	
	return f'https://api.the-odds-api.com/v4/sports/{cat}/odds/?apiKey={api_key}&regions={regions}'

# Get API Data

# Clean

# Keep track of best book/best price for each team

# Save to .csv

