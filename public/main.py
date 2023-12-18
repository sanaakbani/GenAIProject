import typer
from rich import print as pprint
from rich.progress import Progress, SpinnerColumn, TextColumn
from questionGenerator import QuestionGenerator
from jsonParser import ResumeJsonParser

app = typer.Typer()

json_parser: ResumeJsonParser = ResumeJsonParser()
question_maker: QuestionGenerator = QuestionGenerator()

# Generate interview questions based on the content of a PDF resume file.
@app.command()
def question(file_path: str):
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Processing...", total=None)
        pprint(question_maker.create_questions(file_path))


if __name__ == "__main__":
    app()