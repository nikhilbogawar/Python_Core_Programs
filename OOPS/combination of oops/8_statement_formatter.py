# 8. Create:
# • Abstract class StatementFormatter
# • Subclasses: PDFFormatter, JSONFormatter, TextFormatter
# • Overload __call__() so that formatters can be used like functions
# • Overload __repr__ for debugging
# • Demonstrate polymorphic behavior in a reporting pipeline
from abc import ABC, abstractmethod
class StatementFormatter(ABC):
    @abstractmethod
    def __call__(self, data):
        pass
    def __repr__(self):
        return "Formatter object"
class PDFFormatter(StatementFormatter):
    def __call__(self, data):
        return "PDF: " + str(data)
class JSONFormatter(StatementFormatter):
    def __call__(self, data):
        return {"json": data}
class TextFormatter(StatementFormatter):
    def __call__(self, data):
        return "Text: " + str(data)
pipeline = [PDFFormatter(), JSONFormatter(), TextFormatter()]
for fmt in pipeline:
    print(fmt("Report"))