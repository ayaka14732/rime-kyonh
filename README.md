# rime-kyonh

Ayaka’s fork of the rime input schema for Koxyonh’s Romanization of Middle Chinese (古韻羅馬字)

Original version: [rime-middle-chinese](https://github.com/biopolyhedron/rime-middle-chinese)

## Build

```sh
npm install
mkdir -p cache
wget -nc -P cache https://raw.githubusercontent.com/hhliow/cedict_middle_chinese/1a046d7/words_certain.tsv
node build/generate_map.js
python build/build1.py
python build/uniqsort.py
python build/build_unspaced.py
```
