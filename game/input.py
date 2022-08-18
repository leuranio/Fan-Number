CARRET: str = '::'


class OnlyNumber(Exception):
    ...


def enter() -> None:
    typing()


def digit() -> int:
    try:
        digit: int = int(typing())
        return digit
    except ValueError:
        raise OnlyNumber


def decline() -> bool:
    return not confirm()


def confirm() -> bool:
    typed_value: str = typing()[0]
    return True if typed_value == 'y' else False


def typing() -> str:
    return input(f'{CARRET} ')
