const person = {
    firstName: "Arthur",
    lastName: "Morgan",
    fullName: () => {
        return `${this}`;
    }
}

console.log(person.fullName());