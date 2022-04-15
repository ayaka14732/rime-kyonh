import fs from "fs";
import Qieyun from "qieyun";
import { baxter, kyonh } from "qieyun-examples";

const kyonhMap = [];
const baxterMap = [];

function* 生成音韻地位() {
  yield* Qieyun.iter音韻地位();
  yield* ["並咍上", "滂咍上", "幫三庚入", "見開三B仙入"].map((描述) =>
    Qieyun.音韻地位.from描述(描述)
  );
}

for (const 音韻地位 of 生成音韻地位()) {
  kyonhMap.push(音韻地位.描述 + "\t" + kyonh(音韻地位));
  baxterMap.push(音韻地位.描述 + "\t" + baxter(音韻地位));
}

fs.writeFileSync("cache/kyonh.txt", kyonhMap.join("\n") + "\n");
fs.writeFileSync("cache/baxter.txt", baxterMap.join("\n") + "\n");
