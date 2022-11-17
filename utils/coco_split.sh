git clone https://github.com/akarazniewicz/cocosplit.git
cd cocosplit
pip install -r requirements.txt -q
python cocosplit.py --having-annotations --multi-class -s 0.8 path../instances_default.json path../train.json path../test.json