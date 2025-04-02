const express = require("express");
const axios = require("axios");
const app = express();

let keepRunning = true; // Flag to control the loop

app.get("/api", (req, res) => {
    console.log("Node.js API called");

    // Simulate anomalies
    const random = Math.random();
    if (random < 0.1) {
        // 10% chance of returning a 500 error
        console.error("Simulated server error");
        return res.status(500).json({ error: "Internal Server Error" });
    } else if (random < 0.2) {
        // 10% chance of introducing a delay
        console.warn("Simulated delay in response");
        setTimeout(() => {
            res.json({ message: "Delayed response from Node.js API!" });
        }, 3000); // 3-second delay
    } else {
        // Normal response
        res.json({ message: "Hello from Node.js API!" });
    }
});

// Function to continuously hit the API with a delay
function hitApiContinuously() {
    const interval = setInterval(async () => {
        if (!keepRunning) {
            clearInterval(interval); // Stop the interval when the flag is false
            return;
        }
        try {
            const response = await axios.get("http://localhost:4000/api");
            console.log("API Response:", response.data);
        } catch (error) {
            console.error("Error hitting API:", error.message);
        }
    }, 2000); // 2-second delay
}

// Start hitting the API after the server starts
const server = app.listen(4000, () => {
    console.log("Node.js API running on port 4000");
    hitApiContinuously();
});

// Handle process termination
function gracefulShutdown() {
    console.log("Stopping continuous API requests...");
    keepRunning = false; // Set the flag to false to stop the loop
    server.close(() => {
        console.log("Node.js API stopped.");
        process.exit(0); // Exit the process
    });
}

process.on("SIGINT", gracefulShutdown); // Handle Ctrl+C
process.on("SIGTERM", gracefulShutdown); // Handle Docker stop
