
class Builder:
    def select(self, table:str, columns:list[str]):
        pass

    def where(self, conditions:str):
        pass

    def limit(self, number:int):
        pass

    def getSql(self)->str:
        pass

    def reset(self):
        pass