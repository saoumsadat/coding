// Leave the next line, the form must be assigned to a variable named 'form' in order for the exercise test to pass
const form = document.querySelector('form');
const list = document.querySelector('ul');

form.addEventListener('submit', (e) => {
    e.preventDefault();
    let item = `${form[1].value} ${form[0].value}`;

    const li = document.createElement('li');
    li.innerText = item;

    list.appendChild(li);
    
    form[0].value = "";
    form[1].value = "";
})
