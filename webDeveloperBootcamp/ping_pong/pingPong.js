//selecting elements
const select = document.querySelector('select');
const p1btn = document.querySelector('#p1btn');
const p2btn = document.querySelector('#p2btn');
const reset = document.querySelector('#reset');
const p1Scr = document.querySelector('#p1-score');
const p2Scr = document.querySelector('#p2-score');

//initial limit
let limit = parseInt(select.value);

//reset
const resetAll = () => {
    p1btn.disabled = false;
    p2btn.disabled = false;
    p1Scr.innerText = p2Scr.innerText = 0;
    p1Scr.style.color = p2Scr.style.color = 'black';
}

//change limit
select.addEventListener('change', () => {
    limit = parseInt(select.value);
    resetAll();
})

//player score change
const changeScr = (pScr) => {
    let currScr = parseInt(pScr.innerText);
    pScr.innerText = currScr + 1;
    console.log(pScr.innerText);
}

//check gameover
const gamerOverCheck = () => {
    if (p1Scr.innerText == limit || p2Scr.innerText == limit) {
        p1btn.disabled = true;
        p2btn.disabled = true;
        return true;
    }
}


//************

//player1
p1btn.addEventListener('click', () => {
    changeScr(p1Scr);
    if (gamerOverCheck()) {
        p1Scr.style.color = 'green'
        p2Scr.style.color = 'red'
    }
})
//player2gamerOverCheck
p2btn.addEventListener('click', () => {
    changeScr(p2Scr);
    if (gamerOverCheck()) {
        p2Scr.style.color = 'green'
        p1Scr.style.color = 'red'
    }
})
//reset
reset.addEventListener('click', () => {
    resetAll();
})