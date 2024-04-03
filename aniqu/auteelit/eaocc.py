from rich.console import Console

console = Console()

def cprint(text, color):
    """Print text with color."""
    console.print(text, style=color)

cprint(f'\n>>> approve LP | {address_wallet} | {error}', 'red')
