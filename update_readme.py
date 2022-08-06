
import pathlib
import re

root = pathlib.Path(__file__).parent.resolve()


def replace_writing(content, marker, chunk, inline=False):
    r = re.compile(
        r'<!\-\- {} starts \-\->.*<!\-\- {} ends \-\->'.format(marker, marker),
        re.DOTALL,
    )
    if not inline:
        chunk = '\n{}\n'.format(chunk)
    chunk = '<!-- {} starts -->{}<!-- {} ends -->'.format(marker, chunk, marker)
    return r.sub(chunk, content)


if __name__ == '__main__':
    readme_path = root / 'README.md'
    readme = readme_path.open().read()
    entries_md = '\n'.join(
        ["huyuu", "huyuu"]
    )

    # Update entries
    rewritten_entries = replace_writing(readme, 'stats', entries_md)
    readme_path.open('w').write(rewritten_entries)