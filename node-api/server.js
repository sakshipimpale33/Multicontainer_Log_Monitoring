const express = require("express");
const app = express();

app.get("/api", (req, res) => {
    console.log("Node.js API called");
    res.json({ message: "Hello from Node.js API!" });
});

app.listen(4000, () => {
    console.log("Node.js API running on port 4000");
});
