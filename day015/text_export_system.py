"""
Text Export System

Create an object-oriented system that exports a report in different formats.

Requirements:
    - Create a Report class with title and content attributes.
    - Create an abstract Exporter class with an export() method.
    - Create PlainTextExporter, MarkdownExporter, and JsonExporter classes.
    - Each exporter must implement export(report) and return a string.
    - Use json.dumps() to create the JSON representation.
    - Create a ReportService class that receives an exporter.
    - ReportService must delegate exporting to the selected exporter.
    - ReportService must not use if/elif branches to choose the format.
    - ReportService must not use isinstance() to identify concrete exporter types.
    - Use type hints and instance methods.
    - Keep report data separate from export behavior.
    - Do not use global variables.

The task demonstrates abstraction, inheritance, polymorphism, and interchangeable
behavior through a common exporter interface.

Example:
    report = Report("Annual Report", "Revenue increased by 20%")
    service = ReportService(MarkdownExporter())
    print(service.generate(report))
"""

import json
from abc import ABC, abstractmethod


class Report:
    def __init__(self, title: str, content: str) -> None:
        if not isinstance(title, str) or not isinstance(content, str):
            raise TypeError("Title and content must be strings.")

        self.title = title
        self.content = content

    def get_text(self) -> str:
        return self.content


class Exporter(ABC):
    @abstractmethod
    def export(self, report: Report) -> str:
        pass


class PlainTextExporter(Exporter):
    def export(self, report: Report) -> str:
        return f"{report.title}\n{report.get_text()}"


class MarkdownExporter(Exporter):
    def export(self, report: Report) -> str:
        return f"# {report.title}\n{report.get_text()}"


class JsonExporter(Exporter):
    def export(self, report: Report) -> str:
        data = {"title": report.title, "content": report.get_text()}

        return json.dumps(data, ensure_ascii=False, indent=4)


class ReportService:
    def __init__(self, exporter: Exporter) -> None:
        if not isinstance(exporter, Exporter):
            raise TypeError("Exporter must be an instance of Exporter.")

        self.exporter = exporter

    def generate(self, report: Report) -> str:
        return self.exporter.export(report)
