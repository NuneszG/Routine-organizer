const StartButton = document.getElementById('Start');
const PauseButton = document.getElementById('Pause');
const ContinueButton = document.getElementById('Continue');
const RestartButton = document.getElementById('Restart');

const Minutes = document.querySelector('#minutes');
const Seconds = document.querySelector('#seconds');
const Miliseconds = document.querySelector('#miliseconds');

let interval;
let minutes = 0;
let seconds = 0;
let miliseconds = 0;
let pause = false;


StartButton.addEventListener('click', StartTimer);
PauseButton.addEventListener('click', PauseTimer);
ContinueButton.addEventListener('click', ContinueTimer);
RestartButton.addEventListener('click', RestartTimer)

PauseButton.style.display = 'none';
ContinueButton.style.display = 'none';
RestartButton.style.display = 'none';

function StartTimer(){
    interval = setInterval(() => {

        if (!pause){
            miliseconds +=10;
        
            if (miliseconds === 1000){
                seconds ++;

                miliseconds = 0;
            }
            if (seconds === 60){
                minutes ++;

                seconds = 0;
                miliseconds = 0;

            }

            Minutes.textContent = FormatTime(minutes);
            Seconds.textContent = FormatTime(seconds);
            Miliseconds.textContent = FormatMiliseconds(miliseconds);
        }

        StartButton.style.display = 'none';
        PauseButton.style.display = 'block';
        ContinueButton.style.display = 'block';
        RestartButton.style.display = 'block';

    }, 10);
}

function PauseTimer(){
    pause = true;

    StartButton.style.display = 'none';
    ContinueButton.style.display = 'block';
};

function ContinueTimer(){
    pause = false;

    ContinueButton.style.display = 'block';
}

function RestartTimer(){
    pause = true;

    clearInterval(interval);

    Minutes = 0;
    Seconds = 0;
    Miliseconds = 0;
    
    Minutes.textContent = '00';
    Seconds.textContent = '00';
    Miliseconds.textContent = '000';

}

function FormatTime(time){
    return time < 10 ? `0${time}` : time
};

function FormatMiliseconds(time){
    return time < 100 ? `0${time}`.padStart(3, '0') : time
}