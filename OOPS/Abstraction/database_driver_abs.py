# 14. Create an abstract class DatabaseDriver with:
# • connect()
# • execute(query)
# • close()
# Implement concrete drivers:
# • MySQLDriver
# • PostgresDriver
# • SQLiteDriver
# Show how abstraction helps switch databases without rewriting main code.

from abc import ABC, abstractmethod
class DatabaseDriver(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def execute(self,query):
        pass
    @abstractmethod
    def close(self):
        pass
class MySQLDriver(DatabaseDriver):
    def connect(self):
        print("Connected to MySQL")
    def execute(self,query):
        print(f"MySQL Executing : {query}")
    def close(self):
        print("MySQL Closed")
class PostgresDriver(DatabaseDriver):
    def connect(self):
        print("Connected to Postgres")
    def execute(self,query):
        print(f"Postgres Executing : {query}")
    def close(self):
        print("postgres Closed")
class SQLiteDriver(DatabaseDriver):
    def connect(self):
        print("Connected to SQLite")
    def execute(self,query):
        print(f"SQLite Executing : {query}")
    def close(self):
        print("SQLite Closed")
def run_query(driver: DatabaseDriver):
    driver.connect()
    driver.execute("SELECT * FROM users")
    driver.close()
d=[MySQLDriver(),PostgresDriver(),SQLiteDriver()]
for i in d:
    run_query(i)