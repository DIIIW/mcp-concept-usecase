import os
from dotenv import load_dotenv
load_dotenv()
import httpx

AITABLE_KEY = os.getenv("AITABLE_KEY")
BASE_URL = "https://aitable.ai/fusion/v1/datasheets/dstu7MRYThBwdgYp7p"
headers  = {'Authorization': AITABLE_KEY}

def get_aitable_record(maxRecords:int):
    """
    Retrieve a limited number of records from the Airtable API.

    Args:
        maxRecords (int): The maximum number of records to fetch.
        
    """
    params = {'maxRecords': maxRecords}
    r = httpx.get(BASE_URL + "/records", headers=headers, params=params)
    print(r.json())
    return 

def get_filter_record(conditions:str, maxRecords:int):
    """
    Retrieve Airtable records that match a specific filter condition.

    Args:
        conditions (str): A valid Airtable formula expression for filtering.
            This must follow Airtable's formula syntax.
        maxRecords (int): The maximum number of records to fetch. default 5. 

    Description:
        Sends a GET request to the Airtable API and returns only the records 
        that match the specified filter formula. The `conditions` string 
        should be formatted according to Airtable's `filterByFormula` rules.

    Example:
        get_filter_record("{team} = 'Team A'")
        # Retrieves all records where the 'team' field is exactly 'Team A'.

        get_filter_record("AND({status} = 'active', {score} > 80)")
        # Retrieves all records where 'status' is 'active' and 'score' is greater than 80.
    """
    params = {'filterByFormula': f'{conditions}',
              'maxRecords': maxRecords}
    print(params)
    r = httpx.get(BASE_URL + "/records", headers=headers, params=params)
    return r.json()

if __name__ == "__main__":
    # get_aitable_record(maxRecords=5)
    result = get_filter_record(conditions ="{team} = 'Team A'")
    print(result)