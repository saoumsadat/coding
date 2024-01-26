// DO NOT TOUCH!!! (please)
const airplaneSeats = [
    ['Ruth', 'Anthony', 'Stevie'],
    ['Amelia', 'Pedro', 'Maya'],
    ['Xavier', 'Ananya', 'Luis'],
    ['Luke', null, 'Deniz'],
    ['Rin', 'Sakura', 'Francisco']
];

// YOUR CODE GOES BELOW THIS LINE:
for(let i = 0; i < airplaneSeats.length; i++){
    for(let j = 0; j < airplaneSeats[i].length; j++){
        if (!(airplaneSeats[i][j])){
            airplaneSeats[i][j] = "Hugo"
        }
    }
}
console.log(airplaneSeats)