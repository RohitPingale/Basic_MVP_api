from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# This are random weights I have considered for the calculation of loan
#which are subjecct to change as we change type of  loan eligibility.
home_loan_importance_weights = {
    "citizenship": 0.15,
    "age": 0.10,
    "monthly_income": 0.20,
    "ownership_of_property": 0.05,
    "existing_credit": 0.15,
    "employer": 0.05,
    "credit_history_score": 0.15,
    "previous_loans": 0.05,
    "expected_loan_amount": 0.10
}

class LoanRequest(BaseModel):
    citizenship: bool
    age: int
    monthly_income: float
    ownership_of_property: bool
    existing_credit: float
    employer: str
    credit_history_score: float
    previous_loans: int
    expected_loan_amount: float

    #TODO: Here we can implement AI  model for calcaute the score, but for that we need data to train model for now i have sued the basic formula
def calcaute_score(data,importance_weights = home_loan_importance_weights):
    score = 0
    score += importance_weights["monthly_income"] * (data.monthly_income / data.expected_loan_amount)
    score += importance_weights["ownership_of_property"] * (1 if data.ownership_of_property else 0)
    score += importance_weights["existing_credit"] * (1 - data.existing_credit / data.expected_loan_amount)
    # print(importance_weights["credit_history_score"] , data.credit_history_score / 850)
    score += importance_weights["credit_history_score"] * (data.credit_history_score / 850)
    score += importance_weights["previous_loans"] * (1 if data.previous_loans == 0 else 0.5)
    score += importance_weights["age"] * (1 if 21 <= data.age <= 65 else 0)
    score += importance_weights["citizenship"] * (1 if data.citizenship else 0)
    # score += importance_weights["employer"] * (1 if data.employer else 0) 
    # #TODO Find way to score them based on employers company's like MNC,SME,startup(based on which score is between 0-1)
    return score 

@app.post("/loan-eligibility/")
async def get_loan_eligibility(data: LoanRequest):
    #Two rule metioned in docs
    if not data.citizenship:
        return {"eligibility_score": 0, "recommendation": "Ineligible due to citizenship"}

    if data.age < 21 or data.age > 65:
        return {"eligibility_score": 0, "recommendation": "Ineligible due to age"}

    score = calcaute_score(data)


    score_percentage = round(score  * 100, 2)

    #human-readable recommendation
    if score_percentage > 75:
        recommendation = "Highly likely to be approved"
    elif score_percentage > 50:
        recommendation = "Likely to be approved"
    else:
        recommendation = "Unlikely to be approved"

    return {
        "eligibility_score": score_percentage,
        "recommendation": recommendation
    }

if __name__ == "__main__":
    uvicorn.run(app, host = "0.0.0.0", port= 8000)