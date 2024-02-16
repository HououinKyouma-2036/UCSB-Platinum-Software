"""
Internal scraper used to query course information from the UCSB API
"""

from django.conf import settings
import requests

"""
Information about the API can be found here: 
<https://developer.ucsb.edu/content/academic-curriculums#/>
"""
def query_UCSB_classes(quarter: str, subjectCode: str = "", pageNumber: int = 1) -> dict:
    # quarter is required to query the UCSB api
    # quarter follows YYYYQ format; Q is an integer [W = 1, S = 2, M = 3, F = 4]
    assert quarter
    assert len(quarter) == 5
    assert quarter.isdigit()
    assert int(quarter[-1]) >= 1 and int(quarter[-1]) <= 4

    # *** Query Parameters ***
    minUnits: int = 1
    maxUnits: int = 12
    pageSize: int = 30 # to be modified
    includeClassSections: bool = True

    # all of the valid parameters found on the api should be input into the url
    url: str = (
        f"https://api.ucsb.edu/academics/curriculums/v3/classes/search?"
        f"quarter={quarter}"
        f"&minUnits={minUnits}"
        f"&maxUnits={maxUnits}"
        f"&pageNumber={pageNumber}"
        f"&pageSize={pageSize}"
        f"&includeClassSections={includeClassSections}"
        f"&subjectCode={subjectCode}"
    )

    # let the UCSB api know what this application is
    headers: dict = {
        "accept": "application/json",
        "ucsb-api-version": "3.0",
        "ucsb-api-key": settings.USCB_API_CONSUMER_KEY
    }

    # send our request and receive the payload
    response: requests.Response = requests.get(url, headers=headers)
    data: dict = response.json()
    return data

if __name__ == "__main__":
    # Example way to query; this should return a list of courses and descriptions
    query = query_UCSB_classes("20241", "CMPSC")
    for i in query["classes"]:
        print(i["courseId"])
        print(i["description"])
    pass 