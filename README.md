# ProtCAVE

**ProtCAVE** (Protein Conditional Variational Autoencoder) is a framework for conditional generation of protein sequences using a Conditional Variational Autoencoder (CVAE).  
It allows generation of protein sequences conditioned on family labels, supporting data-driven protein design and diversity exploration.

## Features

- Converts and preprocesses Pfam sequence datasets for machine learning
- Supports flexible family selection and subsetting
- Scripts for data statistics and conditional sampling
- Ready for CVAE-based protein sequence modeling

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/px172/ProtCAVE.git
cd ProtCAVE
```

### 2. Download the dataset
```bash
bash download.sh
```

### 3. Preprocess the data
All preprocessing scripts are in the src/ directory.
#### Convert sharded CSV files to a single JSONL file
```
python src/convert_shards_to_jsonl.py
```

#### Count family sizes
```
python src/count_family_members.py data/random_split/train.jsonl
```

#### Filter a subset of families for prototyping
```
python src/filter_by_family.py data/random_split/train.jsonl data/random_split/train_subset.jsonl PF13649.6 PF00560.33 PF13508.7 PF06580.13 PF02397.16 1000
```

### Data
Data
Raw and processed data files are not included in this repository due to size.
Please use the included scripts to download and generate datasets.

### Directory Structure 
```
ProtCAVE/
├── src/                   # Data preprocessing scripts
├── data/                  # Datasets (gitignored)
├── download.sh            # Dataset download script
├── .gitignore
└── README.md
```

### License
MIT License

### Contact
Maintainer: px172