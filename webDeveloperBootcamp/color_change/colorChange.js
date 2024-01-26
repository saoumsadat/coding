const btn = document.querySelector('#btn');

const generateRGB = () => {
    const rgb = [];

    for (let i = 0; i < 3; i++) {
        randColorCode = Math.floor((Math.random() * 256));
        rgb[i] = randColorCode;
    }

    const rgbStr = `rgb(${rgb[0]}, ${rgb[1]}, ${rgb[2]})`;
    return rgbStr;
}

const checkDarkBG = (rgb) => {
    const rgbArr = rgb.split(',').map((elem) => {
        numStr = '';
        for (let char of elem) {
            if (char >= '0' && char <= '9') {
                numStr += char;
            }
        }
        return parseInt(numStr);
    });
    
    const sum = rgbArr.reduce((sum, num) => (sum + num));
    console.log(sum);

    return (sum < 200);
}

btn.addEventListener('click', () => {
    color = generateRGB();
    
    console.log(color);

    document.body.style.backgroundColor = color;

    const heading = document.querySelector('h1');
    heading.innerText = color;

    if (checkDarkBG(color)) {
        heading.style.color = 'white';
    } else {
        heading.style.color = 'black';
    }
})
