mkdir -p data
rm -rf data/webis.zip
wget https://www.dropbox.com/s/d2a9ietckt4vf8u/webis-clickbait-22.zip -O data/webis.zip
rm -f data/train.jsonl
rm -f data/validation.jsonl
rm -f data/README.md
cd data && unzip webis.zip && cd ..
