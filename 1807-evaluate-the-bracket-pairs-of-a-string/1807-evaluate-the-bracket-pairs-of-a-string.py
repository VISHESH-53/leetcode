class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = dict(knowledge)
        return re.sub(r"\((\w+)\)", lambda m: d.get(m[1], "?"), s)