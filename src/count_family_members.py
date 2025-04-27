import json
from collections import Counter

counts = Counter()
with open("data/random_split/train.jsonl") as f:
    for line in f:
        item = json.loads(line)
        counts[item["family_accession"]] += 1

# Top 20 most common families
for fam, count in counts.most_common(20):
    print(f"{fam}: {count}")
