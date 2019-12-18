#!/bin/bash
# Extract shortage and discontinuation reports

if (( $# != 3 )); then
	echo "Extracts shortage and discontinuation reports from export.csv"
	echo
	echo "Usage: $0 <input.csv> <shortages.csv> <discontinuations.csv>"
	exit 1;
fi

infile="${1}"
shortagesfile="${2}"
discontsfile="${3}"

# setup headers
grep "Shortage status" "${infile}" | head -1 > "${shortagesfile}"
grep "Discontinuation status" "${infile}" | head -1 > "${discontsfile}"

# content
grep ',Shortage,' "${infile}" >> "${shortagesfile}"
grep ',Discontinuation,' "${infile}" >> "${discontsfile}"
