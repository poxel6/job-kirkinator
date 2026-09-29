# Job Kirkinator

A small scraper for collecting and analyzing job postings from JobVision.

The project started as a way to not be unemployed anymore.

## What it does

* Scrapes developer job listings from JobVision
* Extracts job URLs and basic information
* Visits individual job postings and collects their keywords
* Extracts other job links from job posting and adds non-duplicates
* Counts how often technologies and skills appear
* Exports the collected data for further analysis and visualization

## Example

```text
Python       21
Git          18
C#           15
Linux        12
Docker       10
```

## Tech stack

* Python
* Selenium
* `uv`
* Counter / standard library

## Running

Clone the repository and install the dependencies:

```bash
git clone https://github.com/poxel6/job-kirkinator
cd job-kirkinator
uv sync
```

Then run:

```bash
uv run src/job_kirkinator/__init__.py
```

## Project structure

```text
src/
└── job_kirkinator/
    ├── pages.py
    ├── scraper.py
    ├── models.py
    └── __init__.py
```

`page.py`: Data to mine, URL and css-selector for each page.
`scraper.py`: JobVisonScraper, constructs the pages and models to a full scraper.
`models`: Models for data being mine.
`__init__.py`: Main file, connects everything together.
