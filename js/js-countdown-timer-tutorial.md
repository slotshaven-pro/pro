# JavaScript Countdown Timer – Beginner Tutorial

Inspired by: [How To Create A JavaScript Countdown Timer For Beginners”](https://hackr.io/blog/how-to-create-a-javascript-countdown-timer) on Hackr.io

This tutorial shows you how to build a simple countdown timer using HTML, CSS, and JavaScript.
It is written for complete JavaScript beginners and is designed for use in Visual Studio Code (VS Code), not an online compiler.

---

## 1. What You Will Build

You will create a countdown timer that counts down to a specific date and time (for example, New Year).
It will display the remaining days, hours, minutes, and seconds and stop when the countdown reaches zero.

Example behavior:

- Shows something like: `10 Days 05 Hours 19 Minutes 42 Seconds`
- Every second, the numbers update.
- When the countdown finishes, it shows a message like: `Countdown finished!`

---

## 2. Setting Up Your Project in VS Code

### 2.1 Install VS Code

1. Download and install VS Code from the official site.
2. Open VS Code after installation.

### 2.2 Create Your Project Folder

1. Create a new folder on your computer, for example:
   `js-countdown-timer`
2. Open VS Code.
3. Go to **File → Open Folder…** and select the `js-countdown-timer` folder.

### 2.3 Create the Files

Inside VS Code, create three files in the folder:

- `index.html` – your web page
- `style.css` – basic styles (optional, but recommended)
- `script.js` – your JavaScript code

Your folder structure should look like this:

```text
js-countdown-timer/
  index.html
  style.css
  script.js
```

### 2.4 Open the HTML File in a Browser

You can use either of these approaches:

- Right-click `index.html` in your file explorer and open it with a web browser (Chrome, Edge, Firefox, etc.).
- Or, install the **Live Server** extension in VS Code and use **“Open with Live Server”** on `index.html` for automatic reloads when you save.

---

## 3. Create the HTML Structure

Open `index.html` and add the following HTML code:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>JavaScript Countdown Timer</title>
    <link rel="stylesheet" href="style.css" />
  </head>
  <body>
    <div class="container">
      <h1>Countdown Timer</h1>
      <p id="headline">Countdown to New Year</p>

      <div id="countdown">
        <div class="time-box">
          <span id="days">0</span>
          <span class="label">Days</span>
        </div>
        <div class="time-box">
          <span id="hours">0</span>
          <span class="label">Hours</span>
        </div>
        <div class="time-box">
          <span id="minutes">0</span>
          <span class="label">Minutes</span>
        </div>
        <div class="time-box">
          <span id="seconds">0</span>
          <span class="label">Seconds</span>
        </div>
      </div>

      <div id="message" class="hidden">
        <h2>Countdown finished!</h2>
      </div>
    </div>

    <script src="script.js"></script>
  </body>
</html>
```

### Explanation

- `link rel="stylesheet" href="style.css"` connects your CSS file.
- `#headline` describes what the countdown is for.
- The `#countdown` div contains four boxes for days, hours, minutes, and seconds.
- Each time box has:
  - A `<span>` for the value (`id="days"`, `id="hours"`, etc.)
  - A label (`Days`, `Hours`, etc.)
- The `#message` div is hidden at first and will be shown when the countdown ends.
- The `<script src="script.js"></script>` line includes your JavaScript file at the end of the body.

---

## 4. Add Some Basic Styles (Optional but Nice)

Open `style.css` and add the following CSS:

```css
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

body {
  background-color: #0f172a;
  color: #e5e7eb;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

.container {
  text-align: center;
  padding: 2rem;
  border-radius: 1rem;
  background-color: #111827;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
  max-width: 500px;
  width: 100%;
}

h1 {
  font-size: 2rem;
  margin-bottom: 0.5rem;
}

#headline {
  margin-bottom: 1.5rem;
  color: #9ca3af;
}

#countdown {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
}

.time-box {
  flex: 1;
  padding: 1rem;
  border-radius: 0.75rem;
  background-color: #1f2933;
}

.time-box span:first-child {
  display: block;
  font-size: 1.8rem;
  font-weight: bold;
  margin-bottom: 0.25rem;
}

.label {
  font-size: 0.9rem;
  color: #9ca3af;
  text-transform: uppercase;
  letter-spacing: 1px;
}

#message {
  margin-top: 1.5rem;
}

.hidden {
  display: none;
}
```

### Explanation

- Resets margin/padding and sets a clean default font.
- Centers the `.container` both vertically and horizontally.
- Makes each time box look like a small card with rounded corners.
- `.hidden` is a utility class that hides elements using `display: none;`.

You can customize the colors and sizes later.

---

## 5. Writing the Countdown Logic in JavaScript

Now open `script.js`. You will:

1. Choose a target date.
2. Calculate the remaining time between “now” and that target date.
3. Convert this time into days, hours, minutes, and seconds.
4. Update the HTML every second.
5. Stop when the countdown reaches zero and show a message.

### 5.1 Select HTML Elements in JavaScript

Add this code at the top of `script.js`:

```js
// 1. Select the elements we want to update
const daysEl = document.getElementById("days");
const hoursEl = document.getElementById("hours");
const minutesEl = document.getElementById("minutes");
const secondsEl = document.getElementById("seconds");

const countdownEl = document.getElementById("countdown");
const messageEl = document.getElementById("message");
```

### Explanation

- `document.getElementById("days")` finds the `<span id="days">` from your HTML.
- We store each element in a variable (`daysEl`, `hoursEl`, etc.) so we can change their text later.
- `countdownEl` and `messageEl` are used when the countdown is finished.

### 5.2 Choose Your Target Date

Below the previous code, add:

```js
// 2. Set your target date and time
// Example: midnight on January 1, 2026
const targetDate = new Date("January 1, 2026 00:00:00").getTime();
```

You can change the date string to any future date you want.

- `new Date("January 1, 2026 00:00:00")` creates a Date object.
- `.getTime()` converts it to the number of milliseconds since 1 January 1970 (Unix time).

### 5.3 Create the Update Function

Add this function below the target date:

```js
// 3. Create a function that updates the countdown
function updateCountdown() {
  const now = new Date().getTime(); // current time in ms
  const difference = targetDate - now; // remaining time in ms

  // If difference is less than or equal to zero, the countdown is finished
  if (difference <= 0) {
    // Stop the timer
    clearInterval(intervalId);

    // Hide the countdown and show the message
    countdownEl.classList.add("hidden");
    messageEl.classList.remove("hidden");

    return;
  }

  // Time calculations
  const secondsInMs = 1000;
  const minutesInMs = secondsInMs * 60;
  const hoursInMs = minutesInMs * 60;
  const daysInMs = hoursInMs * 24;

  const days = Math.floor(difference / daysInMs);
  const hours = Math.floor((difference % daysInMs) / hoursInMs);
  const minutes = Math.floor((difference % hoursInMs) / minutesInMs);
  const seconds = Math.floor((difference % minutesInMs) / secondsInMs);

  // Update the HTML
  daysEl.textContent = days;
  hoursEl.textContent = String(hours).padStart(2, "0");
  minutesEl.textContent = String(minutes).padStart(2, "0");
  secondsEl.textContent = String(seconds).padStart(2, "0");
}
```

### Explanation (Step by Step)

1. `const now = new Date().getTime();`
   - Gets the current time in milliseconds.

2. `const difference = targetDate - now;`
   - Calculates how many milliseconds are left until the target date.

3. If `difference <= 0`:
   - The countdown is over.
   - `clearInterval(intervalId);` stops the repeating timer.
   - We hide the countdown (`countdownEl`) and show the finished message (`messageEl`).

4. Time unit constants:
   - `secondsInMs = 1000` ⇒ 1 second = 1000 ms
   - `minutesInMs = secondsInMs * 60` ⇒ 60 seconds
   - `hoursInMs = minutesInMs * 60` ⇒ 60 minutes
   - `daysInMs = hoursInMs * 24` ⇒ 24 hours

5. Convert milliseconds to days/hours/minutes/seconds:
   - `days` is the total remaining days.
   - `hours` is the remainder after removing whole days, converted to hours.
   - `minutes` is the remainder after hours, converted to minutes.
   - `seconds` is the remainder after minutes, converted to seconds.

6. Update text on the page:
   - `daysEl.textContent = days;`
   - `String(hours).padStart(2, "0")` ensures we always show two digits (e.g. `04` instead of `4`).

### 5.4 Run the Function Every Second

At the bottom of `script.js`, add:

```js
// 4. Call updateCountdown every second
// Call once immediately so there's no 1-second delay
updateCountdown();

const intervalId = setInterval(updateCountdown, 1000);
```

### Explanation

- `updateCountdown();` runs the function once immediately.
- `setInterval(updateCountdown, 1000);` tells the browser to run `updateCountdown` every 1000 ms (1 second).
- We store the return value of `setInterval` in `intervalId` so we can stop it later with `clearInterval(intervalId)` when the countdown finishes.

---

## 6. Full JavaScript Code for the Countdown Timer

For reference, here is the complete `script.js` file:

```js
// 1. Select elements
const daysEl = document.getElementById("days");
const hoursEl = document.getElementById("hours");
const minutesEl = document.getElementById("minutes");
const secondsEl = document.getElementById("seconds");

const countdownEl = document.getElementById("countdown");
const messageEl = document.getElementById("message");

// 2. Set target date (change this to any future date)
const targetDate = new Date("January 1, 2026 00:00:00").getTime();

// 3. Function to update countdown
function updateCountdown() {
  const now = new Date().getTime();
  const difference = targetDate - now;

  // If countdown is finished
  if (difference <= 0) {
    clearInterval(intervalId);
    countdownEl.classList.add("hidden");
    messageEl.classList.remove("hidden");
    return;
  }

  const secondsInMs = 1000;
  const minutesInMs = secondsInMs * 60;
  const hoursInMs = minutesInMs * 60;
  const daysInMs = hoursInMs * 24;

  const days = Math.floor(difference / daysInMs);
  const hours = Math.floor((difference % daysInMs) / hoursInMs);
  const minutes = Math.floor((difference % hoursInMs) / minutesInMs);
  const seconds = Math.floor((difference % minutesInMs) / secondsInMs);

  daysEl.textContent = days;
  hoursEl.textContent = String(hours).padStart(2, "0");
  minutesEl.textContent = String(minutes).padStart(2, "0");
  secondsEl.textContent = String(seconds).padStart(2, "0");
}

// 4. Start the timer
updateCountdown();
const intervalId = setInterval(updateCountdown, 1000);
```

---

## 7. Optional: Simple “X Seconds Countdown” Version

If you want a simpler version (for example, user enters 10 seconds and it counts down to zero), you can try this alternative script in a **new** file or project.

### 7.1 HTML (Short Version)

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Simple Seconds Countdown</title>
  </head>
  <body>
    <h1>Simple Seconds Countdown</h1>

    <input id="seconds-input" type="number" placeholder="Enter seconds" />
    <button id="start-btn">Start</button>

    <h2 id="display">0</h2>

    <script src="script.js"></script>
  </body>
</html>
```

### 7.2 JavaScript (Short Version)

```js
const inputEl = document.getElementById("seconds-input");
const startBtn = document.getElementById("start-btn");
const displayEl = document.getElementById("display");

let intervalId;

startBtn.addEventListener("click", () => {
  // Clear any previous countdown
  clearInterval(intervalId);

  let remaining = Number(inputEl.value);

  if (isNaN(remaining) || remaining <= 0) {
    displayEl.textContent = "Please enter a positive number.";
    return;
  }

  displayEl.textContent = remaining;

  intervalId = setInterval(() => {
    remaining -= 1;

    if (remaining <= 0) {
      clearInterval(intervalId);
      displayEl.textContent = "Time's up!";
    } else {
      displayEl.textContent = remaining;
    }
  }, 1000);
});
```

### Explanation

- User types a number of seconds.
- When they click “Start”, you store that number in `remaining`.
- Every second, you decrease `remaining` by 1 and update the display.
- When `remaining` reaches 0, stop the timer and show “Time's up!”.

---

## 8. Summary

You learned how to:

- Set up a basic web project in VS Code.
- Build a countdown layout using HTML.
- Style it with CSS to make it more readable.
- Use JavaScript to:
  - Work with dates and times (`Date` and `.getTime()`),
  - Calculate time differences,
  - Convert milliseconds to days/hours/minutes/seconds,
  - Update the page every second with `setInterval`,
  - Stop the countdown when it finishes.

## 9. Reference

Inspiration: Hackr.io – [How To Create A JavaScript Countdown Timer For Beginners](https://hackr.io/blog/how-to-create-a-javascript-countdown-timer)
