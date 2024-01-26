const allEvens = arrOfNums => (arrOfNums.every(num => (num % 2 == 0)));

console.log(allEvens([1,2,3]));