import os
import csv
import json

def csv_shards_to_jsonl(input_dir, output_jsonl):
    """
    Merge all data-* CSV shard files in input_dir into a single output_jsonl file.
    """
    with open(output_jsonl, 'w') as out_f:
        files = sorted(f for f in os.listdir(input_dir) if f.startswith('data-'))
        print(f"Processing {len(files)} files in {input_dir} ...")
        for fname in files:
            fpath = os.path.join(input_dir, fname)
            with open(fpath, 'r') as in_f:
                reader = csv.DictReader(in_f)
                for row in reader:
                    # Keep all fields; you can customize this line to select specific columns
                    json.dump(row, out_f)
                    out_f.write('\n')
    print(f"Saved {output_jsonl}")

base_dir = "data/random_split"   # Change this to your directory if needed
splits = ["train", "dev", "test"]

for split in splits:
    in_dir = os.path.join(base_dir, split)
    out_jsonl = os.path.join(base_dir, f"{split}.jsonl")
    csv_shards_to_jsonl(in_dir, out_jsonl)
