from pydantic import BaseModel, Field
from typing import List

# Schema for the request body
class QARequest(BaseModel):
    questions:List[str] = Field(...,description="List of  medical questions to be answered")
    context:str = Field(...,description="The medical context to extract the answers from")
    
    class Config:
        json_schema_extra = {
            "example": {
                "questions": [
                    "Has the patient ever taken glyburide for their diabetes mellitus?",
                    "What dose of Lasix was given for edema management?",
                    "What antibiotic was given for pneumonia?",
                    "What was used to treat the patient's anxiety?",
                    "What was the cardiac output measurement?"
                ],
                
                "context": """Mrs. Wetterauer is a 54-year-old female with coronary artery disease status post inferior myocardial infarction in March of 1997, with sick sinus syndrome, status post permanent pacemaker placement, and paroxysmal atrial fibrillation controlled with amiodarone; also with history of diabetes mellitus and hypertension. On 1/11, she experienced severe respiratory distress and was unable to be intubated on the field. She was ultimately intubated at Sirose, and an echocardiogram showed an ejection fraction of 25 to 30 percent with flat CKs. She was diuresed six liters and a right heart catheterization showed a pulmonary artery pressure of 40/15, wedge of 12, and cardiac output of 5.2. Hemodynamics indicated her cardiac output was dependent on her SVR. At the outside hospital, a right upper lobe infiltrate was noted and she was given gentamicin 250 mg times one, and clindamycin 600 mg. She was diagnosed with pneumonia and treated with clindamycin, which caused resolution of her white count. She was also given Solu-Medrol 40 mg intravenous q.6 hours for possible asthma, and had an increase in her Lasix and lisinopril dose, as well as her amiodarone. Her last admission was on 10/6 for atypical chest pain, and she was placed on Bactrim Double Strength b.i.d. times a total of seven days, as well as Lovenox 60 mg b.i.d., aspirin 325 p.o. q.d., lisinopril 40 mg p.o. b.i.d., digoxin 0.25, Lopressor 100 mg b.i.d., Zantac, Albuterol, Flovent, Solu-Medrol, and amiodarone 300 mg once a day. Home medications include amiodarone 200 mg p.o. q.d., Glyburide 5 mg p.o. q.d., Lopressor 50 mg p.o. b.i.d., Prempro 0.625/2.5 p.o. q.d., lisinopr"""}
        }
        
# Schema for the answer body        
class QAAnswer(BaseModel):
    question:str = Field(...,description="The medical question")
    answer:str = Field(...,description="The extracted answer from the context")
    
    class Config:
        json_schema_extra = {
            "example": {
                "question": "Has the patient had Cisapride?",
                "answer": "Cisapride 10 mg p.o. q.i.d."
            }
        }
# Schema for the response body        
class QAResponse(BaseModel):
    answers:List[QAAnswer] = Field(...,description="List of answers to the medical questions")
    
    class Config:
        json_schema_extra = {
            "example": {
                "answers": [
                    {
                        "question": "Has the patient had Cisapride?",
                        "answer": "Cisapride 10 mg p.o. q.i.d."
                    },
                    {
                        "question": "What gastrointestinal medications were added?",
                        "answer": "Prilosec and Cisapride"
                    },
                    {
                        "question": "What test showed a borderline to minimal anterior reversible defect?",
                        "answer": "exercise tolerance test with MIBI"
                    },
                    {
                        "question": "Was the patient ruled out for myocardial infarction?",
                        "answer": "ruled out for a myocardial infarction with serial CPK and serial troponin, both of which showed 0.0"
                    }
                ]
            }
        }