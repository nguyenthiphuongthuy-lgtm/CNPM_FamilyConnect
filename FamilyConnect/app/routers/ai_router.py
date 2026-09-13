from fastapi import APIRouter
from app.models.schemas import AIQuery
from app.ai_service import AIService

router = APIRouter(prefix="/ai", tags=["7. Dịch vụ hỗ trợ AI"])

@router.post("/semantic-search")
def ai_semantic_search(query: AIQuery):
    return {"results": AIService.semantic_search(query.query)}

@router.get("/explain-relation")
def ai_explain_relation(person_a: str, person_b: str):
    return {"explanation": AIService.explain_relationship(person_a, person_b)}

@router.post("/assistant")
def ai_assistant(query: AIQuery):
    return {"answer": f"Trợ lý AI FamilyConnect: Tôi đã xử lý yêu cầu '{query.query}' của bạn."}