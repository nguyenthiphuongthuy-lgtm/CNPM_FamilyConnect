class AIService:
    @staticmethod
    def semantic_search(query: str) -> list:
        # Tìm kiếm ngữ nghĩa AI
        return [{"result": f"Kết quả tìm kiếm AI dựa trên ngữ nghĩa cho '{query}'"}]

    @staticmethod
    def explain_relationship(person_a: str, person_b: str) -> str:
        return f"Dựa trên cây gia đình, {person_a} gọi {person_b} là Chú Họ (thế hệ thứ 3)."

    @staticmethod
    def summarize_content(text: str) -> str:
        return f"Tóm tắt AI: {text[:50]}..."