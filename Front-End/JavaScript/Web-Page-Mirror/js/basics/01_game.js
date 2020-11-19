const btn = document.querySelector('button');
const output = document.querySelector('.output');
const headArea = document.querySelector('h1');
var player = {
    name: 'Fede',
    points: 0
}

output.style.fontSize = '2em';
output.innerHTML = `Welcome ${player.name}<br>Click the Button.`;
btn.addEventListener('click', runCode);

function  runCode() {
    player.points = 0;
    output.innerHTML = "";
    let rolls = getRandom(10);
    console.log(rolls);
    output.innerHTML += `Rolls = ${rolls}. <br>`
    for (let x = 0; x < rolls; x++) {
        let playerRoll = getRandom(6);
        let computerRoll = getRandom(6);
        let message = playGame(playerRoll, computerRoll);
        let val = `${playerRoll} vs ${computerRoll} ${message}`;
        output.innerHTML += `${val} <br>`;
    }
    updateScore(rolls);
    console.log(updateScore);
    console.log(player.points);

}

function getRandom(max) {
    let res = Math.floor(Math.random() * max) +1;
    return res;
}

function playGame(player_score, cpu) {

    let res;
    if (player_score == cpu) {
        res = "Tie Game";
    }
    else if (player_score > cpu) {
        res = "Player 1 Wins!!!";
        player.points++;       
    }
    else {
        res = "CPU Wins :(";
    }
    return res;
}

function updateScore(roundPlayer) {
    headArea.textContent = `Player Points ${player.points} won in
    ${roundPlayer} rounds`;
}