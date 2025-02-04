# Franchiser

Download and classify Franchise Disclosure Documents (FDD's).

Franchiser is free software designed for academics to be able to analyze FDD's.

The tool downloads FDD's from California Department of Financial Protection and Innovation.

## Sources

* [docqnet.dfpi.ca.gov](https://docqnet.dfpi.ca.gov/search/)
* [securities.sos.in.gov](https://securities.sos.in.gov/public-portfolio-search/)
* [cards.web.commerce.state.mn.us](https://cards.web.commerce.state.mn.us)
* [apps.dfi.wi.gov](https://apps.dfi.wi.gov/apps/FranchiseSearch/MainSearch.aspx)

## Requirements

* node
* playwright
* python 3.12.2
* PyPDF2 3.0.1

### Python Notes

#### Virtual Environment

``` sh
venv\Scripts\activate
deactivate
```

## How Franchiser Works

### Step 1

* Create a JavaScript array of franchises you want to search for named franchises.
* You can also use the provided in franchises_one.js, franchises_two.js, etc.
* Put your franchises array in franchiser.js, replacing the franchises array there.

Franchises Example

``` JavaScript
const franchises = ['Example Franchise 1', 'Example Franchise 2'];
```

### Step 2

Use franchiser.js to download FDD's.

### Step 3

Use franchiser.py to populate filenames with the Issuance Date.

### Step 4

Grab the revenue numbers and save them to a CSV with company, year, and revenue fields.
