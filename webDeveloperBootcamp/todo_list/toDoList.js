const todos = [];

while (true) {
    let msg = prompt("What would you like to do?");

    if (msg == 'new') {

        newTodo = prompt('Enter new todo');
        todos.push(newTodo);
        console.log(`${newTodo} added to list`)

    } else if (msg == 'list') {

        console.log("*********");
        for (let i = 0; i < todos.length; i++) {
            console.log(`${i}: ${todos[i]}`)
        }
        console.log("*********");

    } else if (msg == 'delete') {

        toDeleteIndex = parseInt(prompt('Enter the index of todo to delete'));
        deletedTodo = todos.splice(toDeleteIndex, 1);
        console.log(`${deletedTodo} todo removed`);
        
    } else if (msg == 'quit') {

        console.log("OK YOU QUIT THE APP");
        break;

    }
}