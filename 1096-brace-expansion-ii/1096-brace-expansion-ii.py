class Words(frozenset):
    __or__  = lambda a, b: Words(frozenset.__or__(a, b))
    __mul__ = lambda a, b: Words(x + y for x in a for y in b)


class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        code = expression.translate(str.maketrans("{},", "()|"))
        code = re.sub(r"[a-z]+", r"Words(['\g<0>'])", code)
        code = re.sub(r"\)(?=[(W])", ")*", code)
        return sorted(eval(code))