// https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/12.png

const container = document.querySelector('#container');

for (let i = 1; i <= 151; i++) {
    let img = document.createElement('img');
    img.setAttribute('src', `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/${i}.png`); 
    

    let num = document.createElement('span');
    num.append(`#${i}`);
    num.setAttribute(`style`, `text-align: center`);
    
    let div = document.createElement('div');
    div.append(img, num);
    div.setAttribute('style', 'display: flex');

    container.append(div);
}

