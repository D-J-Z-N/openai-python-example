from ai_client import CustomOpenAIClient
from rich.console import Console

console = Console()


def main():

    ai = CustomOpenAIClient()

    console.print(
        "[bold purple]Hello, this is example of the AI client, that responds in Lithuanian.[/bold purple]")
    console.print(
        "[bold blue]You can chat with the AI model or type 'exit' to quit.[/bold blue]")


    while True:
        user_input = console.input("[bold green]You: [/bold green]")

        if user_input.strip().lower() in ["exit"]:
            console.print("[bold purple]Goodbye![/bold purple]")
            break

        try:
            response = ai.send_message(user_input)
            console.print(f"[bold yellow]AI:[/bold yellow] {response}")

        except Exception as e:
            console.print(
                f"[bold red]Error: {e}[/bold red]")
            continue

if __name__ == "__main__":
    main()
