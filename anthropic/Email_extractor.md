# Email extractor

```
[SYSTEM]: Precisely copy any email addresses from the following text and then write them, one per line. Only write an email address if it's precisely spelled out in the input text. If there are no email addresses in the text, write "N/A".  Do not say anything else.
[USER]: Phone Directory:
John Latrabe, 555-232-1995, [[email protected]]
Josie Lana, 555-759-2905, [[email protected]]
Keven Stevens, 555-980-7000, [[email protected]]
Phone directory will be kept up to date by the HR manager.
```

## Example Output

```txt

[email protected]
[email protected]
[email protected]

```

# Links
1. https://docs.anthropic.com/claude/page/email-extractor