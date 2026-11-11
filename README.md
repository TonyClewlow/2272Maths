# 2272 Maths

A website for pupils with the scheme of work, topic slides, videos and practice questions for each year group.

## How the site is made

- `source/year7/scheme-of-work.xlsx` is the Year 7 scheme of work.
- `tools/parse.py` reads the spreadsheet and writes `source/year7/year7.json`.
- `tools/build.py` puts that data into `tools/template.html` and writes `index.html`, which is the page GitHub Pages serves.

To rebuild after changing the spreadsheet:

```
python3 tools/parse.py source/year7/scheme-of-work.xlsx source/year7/year7.json
python3 tools/build.py tools/template.html source/year7/year7.json index.html
```

The site name is set once, as `SITE_NAME` in `tools/template.html`.
