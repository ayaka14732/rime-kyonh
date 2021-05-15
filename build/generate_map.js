import fs from 'fs';
import Qieyun from 'qieyun';
import QieyunExamples from 'qieyun-examples-node';

const kyonh_map = [];
const baxter_map = [];

for (const 音韻地位 of Qieyun.iter音韻地位()) {
    const { 描述 } = 音韻地位;

    const kyonh = QieyunExamples.kyonh(音韻地位);
    const baxter = QieyunExamples.baxter(音韻地位);

    kyonh_map.push(描述 + '\t' + kyonh);
    baxter_map.push(描述 + '\t' + baxter);
}

fs.writeFileSync('cache/kyonh.txt', kyonh_map.join('\n') + '\n');
fs.writeFileSync('cache/baxter.txt', baxter_map.join('\n') + '\n');
