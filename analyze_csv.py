"""Summarize STRUSENSE CSV samples. Sample input may be simulated; check its provenance."""
import csv, sys, statistics
from pathlib import Path

def main(path):
    rows=[]
    with open(path, newline='', encoding='utf-8') as f:
        for r in csv.DictReader(f):
            rows.append(float(r['vibration_index']))
    if not rows:
        raise SystemExit('No data rows found')
    print(f'Rows: {len(rows)}')
    print(f'Mean: {statistics.mean(rows):.3f}')
    print(f'Min: {min(rows):.3f}')
    print(f'Max: {max(rows):.3f}')
    print('Reminder: summary does not diagnose cracks; confirm whether data are simulated or measured.')
if __name__ == '__main__':
    if len(sys.argv)!=2: raise SystemExit('Usage: python analysis/analyze_csv.py path/to/data.csv')
    main(Path(sys.argv[1]))
