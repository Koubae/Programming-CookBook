/* Automatic Timer from 100 to 0

*/
(function mainTimer() {
    var timer = document.getElementById("Timer");
    timer.textContent  = "100";
    
    
    function resetTime($timer) {
        clearInterval($timer);
        timer.textContent  = "100";
        counter = 0
        var interval2 = setInterval(() =>{ 
            counter += 1
            if (counter === 1) {
                clearInterval(interval2);
                mainTimer();
            }
        }, 0);
    
        
    }
    
    function _Timer () {
    
        var Timer = {
        
            startTimer:  function Timer() {
                var currentTime = parseInt(timer.textContent);
                timer.textContent  = currentTime - 1;
                if (parseInt(timer.innerText) == -1) {
                    resetTime(interval);
                }
            },    
        
        }
        
        var interval = setInterval(Timer.startTimer, 1000);
    
    }
    
    _Timer();

})();