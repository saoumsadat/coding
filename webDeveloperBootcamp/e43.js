function returnDay(num) {
    if (num <= 0 || num >= 8) {
        return null;
    }
    const days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
    return days[num - 1];
}
