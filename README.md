Canadian Drug Shortages Snapshots
=================================

A repository of snapshots of the drugshortagescanada.ca data. 

Why? Because that website only provides the current state of drug shortages, so
it is impossible to see past versions of shortage reports. 

Look for the daily snapshots here: 
https://github.com/pipitone/drug-shortages-snapshots/commits/master/export.csv

### Setup

If you want to run this yourself, you'll need Python 2: 

```sh
virtualenv venv
source venv/bin/activate

pip install mechanize
python snapshot.py
```
