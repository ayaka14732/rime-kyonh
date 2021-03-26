# rime-middle-chinese

Ayaka’s fork of the [rime-middle-chinese](https://github.com/biopolyhedron/rime-middle-chinese) input schema

## Project Structure

- `build`: Build script
- `zyenpheng.*`: 使用古韻羅馬字的中古拼音方案（根據原古韻羅馬字方案修改而成）
- `ayaka_2021.*`: 使用綾香中古拼音 2021 版（開發中）的中古拼音方案

## Build

Prepare `build/ayaka_2021.js`.

```sh
npm install
mkdir -p cache
node build/generate_map.js
wget -nc -P cache https://raw.githubusercontent.com/hhliow/cedict_middle_chinese/1a046d7/words_certain.tsv
python build/build1.py
python build/uniqsort.py
python build/build2.py
python build/build_unspaced.py
```
