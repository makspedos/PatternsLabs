from builder import Builder
from query import Query


class MySQLBuilder(Builder):
    def __init__(self):
        self.query = Query()

    def select(self, table: str, columns: list[str]):
        self.query.table = table
        self.query.columns = columns

    def where(self, conditions: str):
        self.query.where.append(conditions)

    def limit(self, number: int):
        self.query.limit = number

    def getSql(self)->str:
        columns = ", ".join(self.query.columns)
        result = f'Mysql query: Select {columns} from {self.query.table}'
        if self.query.where:
            result += f" WHERE {' '.join(self.query.where)}"
        if self.query.limit:
            result += f' Limit {self.query.limit}'
        return result + ';'

    def reset(self):
        self.query = Query()
