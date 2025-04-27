import sys
import json
from collections import defaultdict

def filter_families(input_jsonl, output_jsonl, selected_families, max_per_family=1000, field="family_accession"):
    counts = defaultdict(int)
    selected_set = set(selected_families)
    total_written = 0
    with open(input_jsonl) as fin, open(output_jsonl, 'w') as fout:
        for line in fin:
            item = json.loads(line)
            fam = item[field]
            if fam in selected_set and counts[fam] < max_per_family:
                json.dump(item, fout)
                fout.write('\n')
                counts[fam] += 1
                total_written += 1
    print(f"Wrote {total_written} items to {output_jsonl}")

if __name__ == "__main__":
    # Usage: python filter_by_family.py train.jsonl output.jsonl PF13649.6 PF00560.33 ... [max_per_family]
    input_jsonl = sys.argv[1]
    output_jsonl = sys.argv[2]
    families = sys.argv[3:-1]
    max_per_family = int(sys.argv[-1]) if sys.argv[-1].isdigit() else 1000
    if not families:
        raise ValueError("Please specify at least one family accession.")
    filter_families(input_jsonl, output_jsonl, families, max_per_family)
