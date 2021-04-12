# rime-middle-chinese

Ayaka’s fork of the [rime-middle-chinese](https://github.com/biopolyhedron/rime-middle-chinese) input schema

## Project Structure

- `build`: Build script
- `kyonh.*`: 使用古韻羅馬字的中古拼音方案（根據原古韻羅馬字方案修改而成）

## Build

### Build `kyonh`

```sh
npm install
mkdir -p cache
node build/generate_map.js
wget -nc -P cache https://raw.githubusercontent.com/hhliow/cedict_middle_chinese/1a046d7/words_certain.tsv
python build/build1.py
python build/uniqsort.py
python build/build_unspaced.py
```
