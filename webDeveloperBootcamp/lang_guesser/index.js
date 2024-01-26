import {franc} from 'franc';
import colors from 'colors';
import langs from 'langs';

const checkStr = process.argv[2];
// const checkStr = 'এটি একটি ভাষা একক IBM স্ক্রিপ্ট';
console.log(checkStr);
const langCode = franc(checkStr) || 'und';

try {
    const langObj = langs.where("2T", langCode);
    const lang = langObj.name;
    console.log(lang.green);
} catch {
    if (langCode === 'und') {
        console.log("SORRY, COULDN'T FIGURE IT OUT".red);
    } else {
        console.log(`SORRY, COULDN'T FIND A LANGUAGE FOR CODE: ${langCode}`.red);
    }
}