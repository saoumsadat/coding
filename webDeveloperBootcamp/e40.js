function lastElement(arr){
    if (arr.length == 0) {
        return null;
    }
    return arr[arr.length - 1];
}

console.log(lastElement([]));