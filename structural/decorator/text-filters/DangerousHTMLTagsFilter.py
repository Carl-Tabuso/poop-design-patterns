from TextFormat import TextFormat
from re import sub, Match, IGNORECASE

class DangerousHTMLTagsFilter(TextFormat):
    __dangerous_tag_patterns = [r"<script.*?>([\s\S]*)?</script>"]
    __dangerous_attributes = ["onclick", "onkeypress"]

    def format_text(self, text: str) -> str:
        text = super().format_text(text)

        for pattern in self.__dangerous_tag_patterns:
            text = sub(pattern, "", text, flags=IGNORECASE)

        for attribute in self.__dangerous_attributes:
            def repl_callback(matches: Match[str]) -> str:
                inner = sub(fr"{attribute}=", "", matches.group(1), flags=IGNORECASE)
                return f"<{inner}>"

            text = sub(r"<(.*?)>", repl_callback, text)

        return text
