<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>DTC Bus Service System</title>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: #fff;
}

/* Container */
.container {
    max-width: 1100px;
    margin: auto;
    padding: 20px;
}

/* Header */
.header {
    text-align: center;
    padding: 50px 20px;
}

.header h1 {
    font-size: 3rem;
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    -webkit-background-clip: text;
    color: transparent;
}

.header p {
    margin-top: 10px;
    font-size: 1.1rem;
    color: #ddd;
}

/* Card Layout */
.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 20px;
    margin-top: 30px;
}

/* Card */
.card {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(10px);
    border-radius: 15px;
    padding: 20px;
    transition: 0.3s;
    border: 1px solid rgba(255,255,255,0.1);
}

.card:hover {
    transform: translateY(-8px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.4);
}

.card h2 {
    color: #00c6ff;
    margin-bottom: 10px;
}

.card ul {
    padding-left: 20px;
}

.card li {
    margin: 6px 0;
}

/* Highlight Section */
.highlight {
    margin-top: 40px;
    padding: 25px;
    background: linear-gradient(135deg, #0072ff, #00c6ff);
    border-radius: 15px;
    text-align: center;
}

/* Code Box */
.code {
    background: #111;
    padding: 12px;
    border-radius: 8px;
    margin-top: 10px;
    font-family: monospace;
    font-size: 0.9rem;
    overflow-x: auto;
}

/* Footer */
.footer {
    text-align: center;
    margin-top: 50px;
    padding: 20px;
    color: #bbb;
}
</style>
</head>

<body>

<div class="container">

    <!-- Header -->
    <div class="header">
        <h1>🚌 DTC Bus Service System</h1>
        <p>Smart Bus Management using Python & MySQL</p>
    </div>

    <!-- Overview -->
    <div class="grid">
        <div class="card">
            <h2>📌 Overview</h2>
            <ul>
                <li>Bus tracking & routes</li>
                <li>Staff management</li>
                <li>Earnings tracking</li>
                <li>Customer feedback</li>
                <li>Admin analytics</li>
            </ul>
        </div>

        <div class="card">
            <h2>🗂 Database</h2>
            <ul>
                <li>Bus details & routes</li>
                <li>Staff assignments</li>
                <li>Earnings summary</li>
                <li>Feedback system</li>
                <li>Admin login</li>
            </ul>
        </div>

        <div class="card">
            <h2>⚙ Features</h2>
            <ul>
                <li>User search system</li>
                <li>Admin dashboard</li>
                <li>CRUD operations</li>
                <li>Data visualization</li>
                <li>Secure login</li>
            </ul>
        </div>
    </div>

    <!-- User & Admin -->
    <div class="grid">
        <div class="card">
            <h2>👤 User Panel</h2>
            <ul>
                <li>View buses</li>
                <li>Search routes</li>
                <li>Find stops</li>
                <li>Submit feedback</li>
            </ul>
        </div>

        <div class="card">
            <h2>🔐 Admin Panel</h2>
            <ul>
                <li>Manage buses & staff</li>
                <li>View earnings</li>
                <li>Check feedback</li>
                <li>Generate charts</li>
            </ul>
        </div>

        <div class="card">
            <h2>📊 Visualization</h2>
            <ul>
                <li>Fare comparison</li>
                <li>Earnings insights</li>
                <li>Graph analytics</li>
            </ul>
        </div>
    </div>

    <!-- Flow -->
    <div class="highlight">
        <h2>🔄 System Flow</h2>
        <p><b>User:</b> Search → View → Feedback</p>
        <p><b>Admin:</b> Login → Manage → Analyze</p>
    </div>

    <!-- Setup -->
    <div class="grid">
        <div class="card">
            <h2>🚀 Setup</h2>
            <p>1. Import SQL file</p>
            <p>2. Install dependencies</p>
            <div class="code">
                pip install mysql-connector-python pandas matplotlib tabulate
            </div>
            <p>3. Run project</p>
            <div class="code">
                python main.py
            </div>
        </div>

        <div class="card">
            <h2>📁 Structure</h2>
            <div class="code">
DTC-Bus-Service/
├── database.sql
├── main.py
├── requirements.txt
└── README.html
            </div>
        </div>

        <div class="card">
            <h2>💡 Future Scope</h2>
            <ul>
                <li>Web App (React/Flask)</li>
                <li>Live tracking</li>
                <li>Booking system</li>
                <li>Mobile app</li>
            </ul>
        </div>
    </div>

    <!-- Footer -->
    <div class="footer">
        <p>👨‍💻 Developed by <b>Sandeep semwal</b> | IT Project</p>
    </div>

</div>

</body>
</html>
