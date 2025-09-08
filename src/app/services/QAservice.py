from typing import List, Dict
from app.core.config import tokenizer,model,MAX_INPUT_LENGTH, device
import torch

class QAService:
    def __init__(self):
        self.model = model
        self.tokenizer = tokenizer
        self.max_input_length = MAX_INPUT_LENGTH
    
    def get_answer(self,start_id,end_id,input_ids):
        answer = self.tokenizer.convert_tokens_to_string(
            self.tokenizer.convert_ids_to_tokens(input_ids[start_id:end_id])
        )
        
        return answer.strip()
    
    def answer_questions(self,questions: List[str], context: str)-> List[Dict[str,str]]:
        answers = []
        
        for question in questions:
            inputs = self.tokenizer(question,context, add_special_tokens=True, return_tensors="pt", truncation=True, max_length=self.max_input_length)
            inputs = {k:v.to(device) for k,v in inputs.items() if k in self.tokenizer.model_input_names}
            input_ids = inputs["input_ids"].tolist()[0]
            
            with torch.no_grad():
                outputs = self.model(**inputs)
                
            
            answer_start = torch.argmax(outputs.start_logits)
            answer_end = torch.argmax(outputs.end_logits)
            
            if answer_start <= answer_end:
                answer = self.get_answer(answer_start, answer_end+1, input_ids)
            else:
                raise ValueError(f"Invalid answer span: start {answer_start} > end {answer_end}")
            
            answers.append({
                "question":question,
                "answer":answer
            })
            
        return answers