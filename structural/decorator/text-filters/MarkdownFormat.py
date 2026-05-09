from TextFormat import TextFormat
from re import sub, split, match, Match

class MarkdownFormat(TextFormat):
    def format_text(self, text: str) -> str:
        text = super().format_text(text)

        chunks: list[str] = split(r"\n\n", text)

        def __repl_callback(matches: Match[str]) -> str:
            h = len(matches.group(1))
            return f"<h{h}>{str(matches.group(2)).strip()}</h{h}>"

        for i, chunk in enumerate(chunks):
            chunk = chunk.strip()

            if match(r"^#+", chunk):
                chunks[i] = sub(
                    r"^(#+)(.*?)$", 
                    __repl_callback, 
                    chunk
                )
            else:
                chunks[i] = f"<p>{chunk}</p>"

        text = "\n\n".join(chunks)

        text = sub(r"__(.*?)__", r"<strong>\1</strong>", text)
        text = sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)
        text = sub(r"_(.*?)_", r"<em>\1</em>", text)
        text = sub(r"\*(.*?)\*", r"<em>\1</em>", text)

        return text