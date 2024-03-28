import argparse
import asyncio
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Optional
from urllib.parse import urljoin

import aiohttp
from bs4 import BeautifulSoup

ANTHROPIC_PROMPT_LIBRARY_BASE = "https://docs.anthropic.com/claude/prompt-library"


@dataclass
class PromptMessage:
    role: str
    content: str


@dataclass
class ExampleBlock:
    content: str
    lang: str


@dataclass
class Prompt:
    title: str
    prompt_messages: list[PromptMessage]
    example_outputs: list[str]
    links: list[str]


def to_valid_filename(string):
    return re.sub(r"[^a-zA-Z0-9_.-]", "_", string)


async def fetch_one(session, prompt_url):
    async with session.get(prompt_url) as response:
        text = await response.text()
        soup = BeautifulSoup(text, "html.parser")

        title = soup.find("h1").text
        print("[Anthropic] Parsing page: ", title)
        table = soup.find("div", class_="rdmd-table-inner")

        if not table:
            print("Error: Table not found")
            return None

        prompt_messages = []
        for row in table.find_all("tr"):
            cells = row.find_all("td")
            if (
                len(cells) < 2
            ):  # Ensuring there are at least 2 cells for role and content
                continue  # Skip rows that do not have enough cells

            role = cells[0].text.strip()
            content = cells[1].text.strip()
            prompt_messages.append(PromptMessage(role=role, content=content))

        example_output_heading = soup.find(id="section-example-output")

        example_outputs = []
        if example_output_heading:
            example_blocks = example_output_heading.find_next("blockquote")
            lang_button = example_blocks.find("div", class_="CodeTabs-toolbar")
            lang = (
                lang_button.find("button", class_="CodeTabs_active").text.strip()
                if lang_button
                else ""
            )
            example_outputs.append(ExampleBlock(content=example_blocks.text, lang=lang))
        else:
            example_outputs.append(
                ExampleBlock(content="No example output found", lang="")
            )

        links = [prompt_url]

        prompt = Prompt(
            title=title,
            prompt_messages=prompt_messages,
            example_outputs=example_outputs,
            links=links,
        )
        return prompt


async def extract_urls(session, homepage):
    async with session.get(homepage) as response:
        text = await response.text()
        soup = BeautifulSoup(text, "html.parser")
        anchors = soup.find_all("a")
        links = []

        for a in anchors:
            href = a.get("href")
            if href and href.startswith("page/"):
                prompt_url = urljoin(homepage, href)
                links.append(prompt_url)
        return links


def save_prompt_md(prompt: Prompt, dir: Path):
    filename = to_valid_filename(prompt.title) + ".md"
    anthropic_dir = dir / "anthropic"
    os.makedirs(anthropic_dir, exist_ok=True)

    prompt_messages_str = "\n".join(
        f"[{msg.role.upper()}]: {msg.content}" for msg in prompt.prompt_messages
    )

    example_outputs_blocks = []
    for block in prompt.example_outputs:
        if block.lang:
            example_outputs_blocks.append(f"```{block.lang}\n{block.content}\n```")
        else:
            example_outputs_blocks.append(f"```txt\n{block.content}\n```")

    example_outputs_str = "\n".join(example_outputs_blocks)
    example_outputs_str = (
        f"## Example Output\n\n{example_outputs_str}\n" if example_outputs_str else "\n"
    )

    links_ordered = [f"{i+1}. {link}" for i, link in enumerate(prompt.links)]
    links_str = "\n".join(links_ordered)

    prompt_md = f"""# {prompt.title}

```
{prompt_messages_str}
```

{example_outputs_str}
# Links
{links_str}"""

    with open(f"{anthropic_dir}/{filename}", "w") as f:
        f.write(prompt_md)


async def fetch_all(base_url: str, outdir: Path, limit: Optional[int] = None):
    async with aiohttp.ClientSession() as session:
        prompt_links = await extract_urls(session, base_url)
        if limit is not None:
            prompt_links = prompt_links[:limit]
        tasks = []
        for link in prompt_links:
            print("[Anthropic] Fetching ", link)
            tasks.append(asyncio.ensure_future(fetch_one(session, link)))
        results = await asyncio.gather(*tasks)
        for prompt in results:
            save_prompt_md(prompt, dir=outdir)


async def run_fetch(output_dir: Path, limit: Optional[int] = None):
    print("[Anthropic] Start fetching prompt library...")
    await fetch_all(ANTHROPIC_PROMPT_LIBRARY_BASE, output_dir, limit)


async def main():
    parser = argparse.ArgumentParser(description="Scrape prompt libraries")
    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        default=Path("./"),
        help="Output directory for scraped prompts",
    )
    parser.add_argument(
        "-l",
        "--limit",
        type=int,
        default=None,
        help="Limit the number of prompts to fetch",
    )
    args = parser.parse_args()

    await run_fetch(args.output_dir, args.limit)


def run():
    asyncio.run(main())


if __name__ == "__main__":
    asyncio.run(main())
