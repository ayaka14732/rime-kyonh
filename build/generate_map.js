import fs from 'fs';
import Qieyun from 'qieyun';
import QieyunExamples from 'qieyun-examples-node';

const qieyun_examples_ayaka_2021 = new Function('音韻地位', '字頭', fs.readFileSync('build/ayaka_2021.js', { encoding: 'utf-8' }));

const kyonh_map = [];
const baxter_map = [];
const ayaka_2021_map = [];

for (const 音韻地位 of Qieyun.iter音韻地位()) {
    const { 描述 } = 音韻地位;

    const kyonh = QieyunExamples.kyonh(音韻地位);
    const baxter = QieyunExamples.baxter(音韻地位);
    const ayaka_2021 = qieyun_examples_ayaka_2021(音韻地位);

    kyonh_map.push(描述 + '\t' + kyonh);
    baxter_map.push(描述 + '\t' + baxter);
    ayaka_2021_map.push(描述 + '\t' + ayaka_2021);
}

fs.writeFileSync('cache/kyonh.txt', kyonh_map.join('\n') + '\n');
fs.writeFileSync('cache/baxter.txt', baxter_map.join('\n') + '\n');
fs.writeFileSync('cache/ayaka_2021.txt', ayaka_2021_map.join('\n') + '\n');
