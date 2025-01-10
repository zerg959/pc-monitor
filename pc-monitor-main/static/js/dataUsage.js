let intervalId;
let currentInterval = 1;
let recordingStartTime = null;
let recordingIntervalId = null;


function updateData() {
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            document.getElementById('lastUpdate').textContent =
             `Last Update: ${data.time}`;
            document.getElementById('cpu-usage').textContent =
             `${data.cpu_percent} %`;
            document.getElementById('ram-usage').textContent = 
            `${data.ram_percent} % (${parseFloat(data.ram_used).toFixed(2)} GB /
             ${parseFloat(data.ram_total).toFixed(2)} GB)`;
            document.getElementById('disk-usage').textContent = 
            `${data.disk_percent} % (${parseFloat(data.disk_used).toFixed(2)} GB /
            ${parseFloat(data.disk_total).toFixed(2)} GB)`;
        });
}

function setIntervalUpdate() {
  const newInterval = parseInt(document.getElementById('intervalInput').value);
  if (newInterval > 0) {
      currentInterval = newInterval
      clearInterval(intervalId); // Clear the previous interval
      intervalId = setInterval(updateData, currentInterval * 1000); // Set the new interval
  } else {
      alert("Interval must be a positive number")
  }
}

function switchRecording() {
  fetch('/switch_recording', { method: 'POST' })
      .then(response => response.json())
      .then(data => {
        const button = document.getElementById('recordingBtn');
        button.textContent = data.is_recording ? 'Stop Recording' : 'Start Recording';

        if (data.is_recording) {
          startRecordingTimer();
        } else {
          stopRecordingTimer();
        }
      });
}

function startRecordingTimer() {
  recordingStartTime = new Date();
  updateRecordingTime();
  recordingIntervalId = setInterval(updateRecordingTime, 1000);
}

function stopRecordingTimer() {
  clearInterval(recordingIntervalId);
  recordingStartTime = null;
  document.getElementById('recordingTime').textContent = `RecordingTime: 00:00:00`;
}

function updateRecordingTime() {
  if (recordingStartTime) {
    const now = new Date();
    const totalTime = Math.floor((now - recordingStartTime) / 1000);
    const hours = Math.floor( totalTime / 3600 )
    const minutes = Math.floor( (totalTime % 3600) / 60);
    const seconds = totalTime % 60;
    const formattedTime = 
    `${String(hours).padStart(2, '0')} :
     ${String(minutes).padStart(2, '0')} :
     ${String(seconds).padStart(2, '0')}`;
     document.getElementById('recordingTime').textContent = `Recording Time: ${formattedTime}`;
  }
}

// Initial setup with the default interval
intervalId = setInterval(updateData, currentInterval * 1000);
