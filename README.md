Canadian Drug Shortages Snapshots
=================================

> *Note: Decomissioned 2019-12-30* 
> The Drug Shortages Canada website now exposes historical edits to the
> shortage/discontinuation reports which makes this project unnecessary. 
>
> Unfortunately, the historical data is not exposed via the web API, but can
> likely be easily scraped. 

A repository of daily snapshots of the drugshortagescanada.ca data. 

Why? Because that website only provides the current state of drug shortages, so
it is impossible to see past versions of shortage reports. 

Look for the daily snapshots here: 
https://github.com/pipitone/drug-shortages-snapshots/commits/master/export.csv

### Export Format
The export format is CSV-like. It actually contains multiple CSV 

### Setup

If you want to run this yourself, you'll need Python 2: 

```sh
virtualenv venv
source venv/bin/activate

pip install mechanize
python snapshot.py
```
## Changelog

2018-08-30 - Exports are now concatenated monthly exports

As of about 2018-05-26 the database stopped allowing exports of greater than
3000 records. Unfortunately, I didn't catch that change until months later,
on 2018-08-30. To work around this limitation, snapshot.py simply requests an
export for each month across a range of years, and concatenates the results into
export.csv. It's not pretty the export data was always going to need some clean
up.
