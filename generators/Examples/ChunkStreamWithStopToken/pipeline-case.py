def partiallyEndWith(s, stop_token):
    for i in range(1, len(stop_token)):
        if s.endswith(stop_token[:i]): return True
    return False

def chunk_stream(text_stream, stop_token):

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


input_text = [
    "Hello, what's your name",
    "How are you"
]

input_text = [
    "Hellow, what's your name <END>",
    "How are you"
]

def get_chunk(input):
    for item in input:
        yield item 

def print_chunk(input_text):
    for chunk in chunk_stream(get_chunk(input_text), "<END>"):
        print(chunk)


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
