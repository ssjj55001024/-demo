// 定义全局变量
var p = 1111111111111;
var API_KEY = "a2c903cc-b31e-4547-9299-b6d07b7631ab";

// 加密API Key函数
function encryptApiKey() {
    var t = API_KEY.split("");
    var r = t.splice(0, 8);
    return t.concat(r).join("");
}

// 加密时间戳函数
function encryptTime(e) {
    var t = (1 * e + p).toString().split("");
    var r = Math.floor(Math.random() * 10);
    var n = Math.floor(Math.random() * 10);
    var o = Math.floor(Math.random() * 10);
    return t.concat([r, n, o]).join("");
}

// 组合函数
function comb(e, t) {
    var r = "".concat(e, "|").concat(t);
    return Buffer.from(r).toString('base64'); // Node.js中的Base64编码
}

// 生成API Key函数
function getApiKey() {
    var e = new Date().getTime();
    var t = encryptApiKey();
    e = encryptTime(e);
    return comb(t, e);
}

// 生成并输出API Key
var apiKey = getApiKey();
console.log(apiKey);