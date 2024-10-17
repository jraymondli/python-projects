from typing import Generator

def partiallyEndWith(s: str, stop_token: str) -> bool:
    for i in range(1, len(stop_token)):
        if s.endswith(stop_token[:i]):
            return True
    return False

def chunk_stream(text_stream: Generator[str, None, None], stop_token: str) -> Generator[str, None, None]:
    try:
        stream = next(text_stream)
        while True:
            pos = stream.find(stop_token)
            if pos != -1:
                yield stream[:pos]
                break
            elif partiallyEndWith(stream, stop_token):
                nxt_stream = next(text_stream)
                stream += nxt_stream
            else:
                yield stream
                stream = next(text_stream)
    except StopIteration:
        return

def get_chunk(input: list[str]) -> Generator[str, None, None]:
    for item in input:
        yield item

def print_chunk(input_text: list[str]) -> None:
    for chunk in chunk_stream(get_chunk(input_text), "<END>"):
        print(chunk)

# Test cases
input_text = [
    "Hellow, what's your name <END>",
    "How are you"
]

print_chunk(input_text)

input_text1 = [
    "Hellow, what's your name",
    "How are you"
]

print_chunk(input_text1)

input_text2 = [
    "Hello, what's your name <EN",
    "D> How are you"
]

print_chunk(input_text2)

input_text3 = [
    "Hello, what's your name <E",
    "D> How are you"
]

print_chunk(input_text3)
