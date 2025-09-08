from fastapi import APIRouter, status, HTTPException
from app.services.QAservice import QAService
from app.schemas.schemas import QARequest, QAResponse

router = APIRouter()

qa_model = QAService()

@router.post("/answer",response_model=QAResponse, status_code=status.HTTP_200_OK, tags=["Question Answering"])
async def answer_questions(request: QARequest):
    """Answer questions based on the provided context.

    Args:
        request (QARequest): _description_
    """
    
    try:
        answers = qa_model.answer_questions(request.questions, request.context)
        return QAResponse(answers=answers)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))