from TextInput import TextInput
from PlainTextFilter import PlainTextFilter
from MarkdownFormat import MarkdownFormat
from DangerousHTMLTagsFilter import DangerousHTMLTagsFilter
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from InputFormat import InputFormat

def display_comment_as_a_website(format: InputFormat, text: str) -> None:
    print(format.format_text(text))

if __name__ == "__main__":
    dangerous_comment = """
Hello! Nice blog post!
Please visit my <a href='http://www.iwillhackyou.com'>homepage</a>.
<script src="http://www.iwillhackyou.com/script.js">
performXSSAttack();
</script>
"""

    naive_input = TextInput()
    print("Website renders comments without filtering (unsafe):")
    display_comment_as_a_website(naive_input, dangerous_comment)
    print("\n\n")

    filtered_input = PlainTextFilter(naive_input)
    print("Website renders comments after stripping all tags (safe):")
    display_comment_as_a_website(filtered_input, dangerous_comment)
    print("\n\n")

    dangerous_forum_post = """
# Welcome

This is my first post on this **gorgeous** forum.

<script src="http://www.iwillhackyou.com/script.js">
  performXSSAttack();
</script>
"""

    naive_input = TextInput()
    print("Website renders a forum post without filtering and formatting (unsafe, ugly):")
    display_comment_as_a_website(naive_input, dangerous_forum_post)
    print("\n\n")

    text = TextInput()
    markdown = MarkdownFormat(text)
    filtered_input = DangerousHTMLTagsFilter(markdown)
    print("Website renders a forum post after translating markdown markup and filtering some dangerous HTML tags and attributes (safe, pretty):")
    display_comment_as_a_website(filtered_input, dangerous_forum_post)
    print("\n\n")