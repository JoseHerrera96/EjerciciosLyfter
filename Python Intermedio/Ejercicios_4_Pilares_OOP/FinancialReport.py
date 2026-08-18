# 1. Class for exporting to PDF (Extra functionality)
class PDFExporter:
    def export_pdf(self):
        return f"Exporting '{self.title}' to PDF format..."

# 2. Class for recording dates (Extra functionality)
class DateRecord:
    def show_creation_date(self):
        import datetime
        return f"Created on: {datetime.date.today()}"

# 3. Main Base Class
class Document:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def read(self):
        return f"Reading document: {self.title}"

# 4. Multiple Inheritance: We combine the base class with the additional classes
class FinancialReport(Document, PDFExporter, DateRecord):
    def __init__(self, title, content, author):
        super().__init__(title, content)
        self.author = author

# Usage of the resulting class
report = FinancialReport("Balance 2023", "Income and expenses...", "Finance Department")

# Method from the main class (Document)
print(report.read())
# Output: Reading document: Balance 2023

# Method inherited from the first additional class
print(report.export_pdf())
# Output: Exporting 'Balance 2023' to PDF format...

# Method inherited from the second additional class
print(report.show_creation_date())
# Output: Created on: 2026-08-09