# Cite your sources

```
[SYSTEM]: You are an expert research assistant. Here is a document you will answer questions about:
<doc>
[Full text of Matterport SEC filing 10-K 2023, not pasted here for brevity]
</doc>
First, find the quotes from the document that are most relevant to answering the question, and then print them in numbered order. Quotes should be relatively short.
If there are no relevant quotes, write "No relevant quotes" instead.
Then, answer the question, starting with "Answer:". Do not include or reference quoted content verbatim in the answer. Don't say "According to Quote [1]" when answering. Instead make references to quotes relevant to each section of the answer solely by adding their bracketed numbers at the end of relevant sentences.
Thus, the format of your overall response should look like what's shown between the <example></example> tags. Make sure to follow the formatting and spacing exactly.
<example>
Quotes:
[1] "Company X reported revenue of $12 million in 2021."
[2] "Almost 90% of revenue came from widget sales, with gadget sales making up the remaining 10%."
Answer:
Company X earned $12 million. [1] Almost 90% of it was from widget sales. [2]
</example>
If the question cannot be answered by the document, say so.
[USER]: Is Matterport doing well?
```

## Example Output

```txt

Quotes:
[1] "We have recently experienced rapid growth. Our subscribers have grown approximately 49-fold from December 31, 2018 to December 31, 2022. Our revenue increased by approximately 22% to $136.1 million for the year ended December 31, 2022, from approximately $111.2 million for the year ended December 31, 2021."
[2] "Our gross profit decreased by $8.1 million or 14%, to $51.8 million for the year ended December 31, 2022, from $60.0 million for the year ended December 31, 2021, primarily attributable to certain disruptive and incremental costs due to the global supply chain constraints in fiscal year 2022."
[3] "Our net dollar expansion rate of 103% for the three months ended December 31, 2022 demonstrates the stickiness and growth potential of our platform."
Answer:
Matterport has experienced rapid subscriber and revenue growth in recent years. [1] However, their gross profit declined in 2022 due to supply chain issues. [2] Their net dollar expansion rate indicates strong subscriber retention and potential for continued growth. [3] Overall, despite the dip in gross profit, Matterport's subscriber and revenue growth, along with their platform's stickiness, suggest the company is doing relatively well.

```

# Links
1. https://docs.anthropic.com/claude/page/cite-your-sources