from flask import Flask, request, render_template_string, redirect
import os
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    """Create a MySQL connection using environment variables if provided."""
    return mysql.connector.connect(
        host=os.getenv('MYSQL_HOST', '127.0.0.1'),        
        port=int(os.getenv('MYSQL_PORT', '3306')),        
        user=os.getenv('MYSQL_USER', 'root'),
        password=os.getenv('MYSQL_PASSWORD', 'root'),
        database=os.getenv('MYSQL_DATABASE', 'testapp'),
    )

HTML_FORM = '''
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Login</title>
  <style>
    body {
      height: 100vh;
      margin: 0;
      display: flex;
      align-items: center;
      justify-content: center;
      background: #f6f8fa;
      font-family: 'Segoe UI', Arial, sans-serif;
    }
    .login-container {
      background: #fff;
      padding: 2rem 2.5rem 2.5rem 2.5rem;
      border-radius: 18px;
      box-shadow: 0 4px 32px rgba(0,0,0,0.12);
      min-width: 320px;
    }
    .login-container h1 {
      text-align: center;
      margin-bottom: 1.5rem;
      font-size: 1.7rem;
      color: #263159;
      letter-spacing: 1px;
    }
    .login-container label {
      font-weight: 500;
      margin-bottom: 0.3rem;
      display: block;
      color: #444;
    }
    .login-container input[type="text"],
    .login-container input[type="password"] {
      width: 100%;
      padding: 0.65rem;
      margin-bottom: 1.1rem;
      border: 1px solid #cdd4e3;
      border-radius: 8px;
      font-size: 1rem;
      transition: border 0.2s;
    }
    .login-container input[type="text"]:focus,
    .login-container input[type="password"]:focus {
      outline: none;
      border-color: #6499e9;
    }
    .login-container input[type="submit"] {
      width: 100%;
      padding: 0.7rem;
      background: #6499e9;
      color: white;
      font-weight: bold;
      border: none;
      border-radius: 8px;
      font-size: 1.1rem;
      cursor: pointer;
      letter-spacing: 1px;
      transition: background 0.2s;
    }
    .login-container input[type="submit"]:hover {
      background: #476fcf;
    }
  </style>
</head>
<body>
  <form class="login-container" method="post">
    <h1>Login</h1>
    <label for="username">Username</label>
    <input type="text" id="username" name="username" required>
    <label for="password">Password</label>
    <input type="password" id="password" name="password" required>
    <input type="submit" value="Login">
  </form>
</body>
</html>

'''

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect('/success')
    return render_template_string(HTML_FORM)

@app.route('/success')
def success():
    return 'Login successful!'

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, port=port)
