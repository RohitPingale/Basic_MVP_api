
# Loan Eligibility API

## Tools used:
1. FastAPI  
2. Pydantic  
3. Uvicorn  
4. Python  

---

## Implemented API:
**POST** `/loan-eligibility/`  

---

## Installation:
```bash
pip install -r requirements.txt
```

Start the FastAPI server:
```bash
uvicorn main:app --reload
```

Check API documentation:  
- [http://localhost:8000/docs](http://localhost:8000/docs)  
- [http://localhost:8000/redoc](http://localhost:8000/redoc)  

---
## Results:
1. Sample Result:
![Screenshot (21)](https://github.com/user-attachments/assets/97b0815f-7e9b-4c26-b4fe-e314b1302f0b)
2. Citizenship,age condition:
   ![Screenshot (23)](https://github.com/user-attachments/assets/da901b1e-a02f-49cb-aabc-53a23bc1fb4c)
![Screenshot (22)](https://github.com/user-attachments/assets/9aa97937-a6b1-4e5b-b526-a451030974e5)



## Workflow:

### 1. Take input:
Sample input:
```json
{
  "citizenship": true,
  "age": 80,
  "monthly_income": 60000,
  "ownership_of_property": true,
  "existing_credit": 0,
  "employer": "string",
  "credit_history_score": 320,
  "previous_loans": 0,
  "expected_loan_amount": 1200000
}
```

### 2. Calculate Loan Eligibility Score:
- The eligibility score is calculated using a weighted scoring system.  
- Importance weights for each attribute (example for home loans):  
    - **Citizenship** – 15%  
    - **Age** – 10%  
    - **Monthly Income** – 20%  
    - **Ownership of Property** – 5%  
    - **Existing Credit** – 15%  
    - **Employer** – 5%  
    - **Credit History Score** – 15%  
    - **Previous Loans** – 5%  
    - **Expected Loan Amount** – 10%  

### 3. Rules for Eligibility:
- **Citizenship** – Must be a citizen.  
- **Age** – Must be between **21** and **65** years.  
- If any of the above rules fail, eligibility score = **0** and a rejection reason is provided.  

### 4. Score Calculation:
- **Monthly Income**: Higher monthly income increases score.  
- **Ownership of Property**: Increases score if the user owns property.  
- **Existing Credit**: High existing credit reduces score.  
- **Credit History Score**: Better credit history increases score.  
- **Previous Loans**: No previous loans increase score.  
- **Age**: Between 21 and 65 increases score.  
- **Citizenship**: Being a citizen increases score.  

### 5. Generate Recommendation:
- **Score > 75%** → "Highly likely to be approved"  
- **Score > 50%** → "Likely to be approved"  
- **Score ≤ 50%** → "Unlikely to be approved"  

### Example Response:
```json
{
    "eligibility_score": 68.5,
    "recommendation": "Likely to be approved"
}
```

---

## File Structure:
### `main.py`:
- Implements FastAPI endpoints.  
- Validates input using **Pydantic** models.  
- Calculates loan eligibility score based on importance weights and rules.  
- Generates a human-readable recommendation.  

### `requirements.txt`:
- FastAPI  
- Uvicorn  
- Pydantic  

---

## Further Improvements:
✅ Use of ML modelling.  
✅ Better employer-based scoring (MNC, SME, Startup).  
✅ More complex eligibility logic.  
✅ Dynamic adjustment of importance weights based on loan type.  
✅ Better handling of edge cases and input errors.  

--- 
