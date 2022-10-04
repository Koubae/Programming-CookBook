;(function () {
    let background = document.getElementById('background');
    let width = window.innerWidth;
    let height = window.innerHeight;
    const cellSize = Math.floor(width / 64);
    const cellSizeStyle = `${cellSize / 2}px`;
    const ARENA_WIDTH = (width) / 5;
    const ARENA_HEIGHT = (height) / 5;


    const tableGrid = document.createElement('table');
    tableGrid.classList.add('cell-table');
    for (let i = 0; i < ARENA_HEIGHT; i++) {
        let tableRow = tableGrid.insertRow();
        tableRow.classList.add('cell-row');
        for (let y = 0; y < ARENA_WIDTH; y++) {

            const tableCell = tableRow.insertCell();
            tableCell.classList.add('cell');
            tableCell.style.padding = cellSizeStyle;
        }
    }
    background.appendChild(tableGrid);


})();