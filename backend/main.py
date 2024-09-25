import os
import requests
from helper import authenticate_access_token
from model import MutualFundScheme, UserLogin
from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv  # Import load_dotenv to load the .env file

# Load environment variables from .env file
load_dotenv()


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

EMAIL= os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
RAPID_API_KEY = os.getenv("RAPID_API_KEY")
RAPID_API_URL = os.getenv("RAPID_API_URL")


@app.get("/")
def hello():
    return {
        "statusCode": 200,
        "body": "hey there",
    }


@app.post("/login")
def login(user_data: UserLogin):
    """
    endpoint for dummy login and returning the dummpy access token
    """
    print (user_data.email,EMAIL,user_data.password,PASSWORD)
    if user_data.email == EMAIL and user_data.password == PASSWORD:
        return {"access_token": ACCESS_TOKEN}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")


@app.get("/all-schemes", dependencies=[Depends(authenticate_access_token)])
def get_all_schemes():
    """
    Endpoint to get all the fund details
    """
    url = "https://" + RAPID_API_URL + "/latest"

    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": RAPID_API_URL
    }
    query_params = {"Scheme_Type": "Open"}

    response = requests.get(url, headers=headers, params=query_params)

    if response.status_code == 200:
        schemes_data = response.json()
        schemes = [
            MutualFundScheme(**scheme).dict() for scheme in schemes_data
        ]
        return schemes
    else:
        raise HTTPException(
            status_code=response.status_code,
            detail="Failed to fetch all schemes"
        )


@app.get("/fund-family", dependencies=[Depends(authenticate_access_token)])
def get_fund_family(family: str = Header(...)):
    """
    Endpoint to get details for the perticular fund family
    """
    url = "https://" + RAPID_API_URL + "/latest"

    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": RAPID_API_URL
    }
    query_params = {
        "Scheme_Type": "Open",
        "Mutual_Fund_Family": family
    }

    response = requests.get(url, headers=headers, params=query_params)

    if response.status_code == 200:
        schemes_data = response.json()
        schemes = [
            MutualFundScheme(**scheme).dict() for scheme in schemes_data
        ]
        return schemes
    else:
        raise HTTPException(
            status_code=response.status_code,
            detail="Failed to fetch fund family"
        )


@app.post("/purchase", dependencies=[Depends(authenticate_access_token)])
def purchase_units(
    isin: str = Header(...), units: int = Header(...)
):
    """
    Endpoint to purchase of units for a selected mutual fund
    """
    url = "https://" + RAPID_API_URL + "/master"

    querystring = {"ISIN": isin}

    headers = {
        "X-RapidAPI-Key": RAPID_API_KEY,
        "X-RapidAPI-Host": RAPID_API_URL
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        respons_json = response.json()
        is_bought = False
        for opt in respons_json:
            if opt["Purchase_Allowed"]:
                if opt["Minimum_Purchase_Amount"] < units:
                    print(
                        f"cannont buy the mutal fund id: {opt['Unique_No']}"
                    )
                else:
                    is_bought = True
                    print(
                        f"Purchased {units} units of scheme with code {isin}"
                    )
                    break

        if not is_bought:
            return {
                "message": "units not satisfying the min desired values"
            }
        else:
            # now we can update the in our db, be it sql or mongo
            # after having the payment flow
            return {
                "message": f"Successfully purchased {units} units"
            }
    else:
        raise HTTPException(
            status_code=response.status_code,
            detail="Failed to purchase"
        )