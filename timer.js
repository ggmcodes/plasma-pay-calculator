// Pomodoro Timer Functionality for Sunset Study Club
let timeLeft = 25 * 60; // 25 minutes in seconds
let totalTime = 25 * 60;
let timerInterval = null;
let isRunning = false;
let sessionsCompleted = 0;

function updateDisplay() {
    const minutes = Math.floor(timeLeft / 60);
    const seconds = timeLeft % 60;
    const timerDisplay = document.getElementById('timerDisplay');
    if (timerDisplay) {
        timerDisplay.textContent = 
            `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    }
    
    // Update progress bar
    const progress = ((totalTime - timeLeft) / totalTime) * 100;
    const progressFill = document.getElementById('progressFill');
    if (progressFill) {
        progressFill.style.width = `${100 - progress}%`;
    }
}

function startTimer() {
    if (!isRunning) {
        isRunning = true;
        const startBtn = document.getElementById('startBtn');
        const pauseBtn = document.getElementById('pauseBtn');
        const sessionInfo = document.getElementById('sessionInfo');
        
        if (startBtn) startBtn.style.display = 'none';
        if (pauseBtn) pauseBtn.style.display = 'inline-block';
        if (sessionInfo) sessionInfo.textContent = 'Focus time! Stay concentrated in your peaceful space...';
        
        timerInterval = setInterval(() => {
            if (timeLeft > 0) {
                timeLeft--;
                updateDisplay();
            } else {
                completeSession();
            }
        }, 1000);
    }
}

function pauseTimer() {
    if (isRunning) {
        isRunning = false;
        clearInterval(timerInterval);
        const startBtn = document.getElementById('startBtn');
        const pauseBtn = document.getElementById('pauseBtn');
        const sessionInfo = document.getElementById('sessionInfo');
        
        if (startBtn) {
            startBtn.style.display = 'inline-block';
            startBtn.textContent = 'Resume';
        }
        if (pauseBtn) pauseBtn.style.display = 'none';
        if (sessionInfo) sessionInfo.textContent = 'Paused - Resume when ready to continue your focus';
    }
}

function resetTimer() {
    isRunning = false;
    clearInterval(timerInterval);
    timeLeft = totalTime;
    updateDisplay();
    
    const startBtn = document.getElementById('startBtn');
    const pauseBtn = document.getElementById('pauseBtn');
    const sessionInfo = document.getElementById('sessionInfo');
    const timerContainer = document.querySelector('.timer-container');
    
    if (startBtn) {
        startBtn.style.display = 'inline-block';
        startBtn.textContent = 'Start';
    }
    if (pauseBtn) pauseBtn.style.display = 'none';
    if (sessionInfo) sessionInfo.textContent = 'Ready to focus in your peaceful space';
    if (timerContainer) timerContainer.classList.remove('completed');
}

function completeSession() {
    isRunning = false;
    clearInterval(timerInterval);
    sessionsCompleted++;
    
    const startBtn = document.getElementById('startBtn');
    const pauseBtn = document.getElementById('pauseBtn');
    const sessionInfo = document.getElementById('sessionInfo');
    const timerContainer = document.querySelector('.timer-container');
    
    if (startBtn) {
        startBtn.style.display = 'inline-block';
        startBtn.textContent = 'Start';
    }
    if (pauseBtn) pauseBtn.style.display = 'none';
    if (sessionInfo) {
        sessionInfo.textContent = `Beautiful work! Session ${sessionsCompleted} completed. Time for a mindful break.`;
    }
    if (timerContainer) timerContainer.classList.add('completed');
    
    // Play gentle completion sound
    playCompletionSound();
}

function playCompletionSound() {
    try {
        const audioContext = new (window.AudioContext || window.webkitAudioContext)();
        
        // Create a gentle, zen-like completion sound
        const createGentleTone = (startTime, frequency = 220) => {
            const oscillator = audioContext.createOscillator();
            const gainNode = audioContext.createGain();
            
            oscillator.connect(gainNode);
            gainNode.connect(audioContext.destination);
            
            oscillator.frequency.value = frequency;
            oscillator.type = 'sine';
            
            // Gentle envelope - soft attack, long decay
            const attackTime = 0.1;
            const decayTime = 2.0;
            const maxVolume = 0.1; // Very soft
            
            gainNode.gain.setValueAtTime(0, startTime);
            gainNode.gain.linearRampToValueAtTime(maxVolume, startTime + attackTime);
            gainNode.gain.exponentialRampToValueAtTime(0.001, startTime + decayTime);
            
            oscillator.start(startTime);
            oscillator.stop(startTime + decayTime);
        };
        
        // Play a gentle meditation bell sound
        createGentleTone(audioContext.currentTime, 440); // A4 note
    } catch (error) {
        console.log('Audio not available');
    }
}

function setTimer(minutes) {
    // Stop any running timer
    if (isRunning) {
        clearInterval(timerInterval);
        isRunning = false;
    }
    
    totalTime = minutes * 60;
    timeLeft = totalTime;
    updateDisplay();
    
    // Reset UI state
    const startBtn = document.getElementById('startBtn');
    const pauseBtn = document.getElementById('pauseBtn');
    const sessionInfo = document.getElementById('sessionInfo');
    const timerContainer = document.querySelector('.timer-container');
    
    if (startBtn) {
        startBtn.style.display = 'inline-block';
        startBtn.textContent = 'Start';
    }
    if (pauseBtn) pauseBtn.style.display = 'none';
    if (timerContainer) timerContainer.classList.remove('completed');
    if (sessionInfo) sessionInfo.textContent = `${minutes} minute peaceful focus session selected`;
    
    // Update active button
    document.querySelectorAll('.time-option').forEach(option => {
        option.classList.remove('active');
    });
    event.target.classList.add('active');
}

// Initialize when page loads
document.addEventListener('DOMContentLoaded', function() {
    updateDisplay();
    
    // Register Service Worker for PWA functionality
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('sw.js')
            .then(reg => console.log('Service Worker registered'))
            .catch(err => console.log('Service Worker registration failed'));
    }
    
    // Prevent pull-to-refresh on mobile for better UX
    document.body.addEventListener('touchmove', (e) => {
        if (e.touches.length > 1) {
            e.preventDefault();
        }
    }, { passive: false });
});