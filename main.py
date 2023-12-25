<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pyperclip Web App</title>
</head>
<body>
    <h1>Pyperclip Web App</h1>

    <form action="/copy" method="post">
        <label for="message">Enter a message:</label>
        <input type="text" id="message" name="message" required>
        <button type="submit">Copy</button>
    </form>

    <p><a href="/paste" target="_blank">Paste the copied message</a></p>
</body>
</html>

