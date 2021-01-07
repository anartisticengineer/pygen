<h1>PYGEN</h1>
<h2>Command-line python project generator</h2>

<p>Steps to initially get started:</p>
<ol>
    <li>In the same level as the root project folder, create a new .env file. When created, add the following line to the file: <div>DEST_PATH=Your_Directory_Here</div>
    <div>Your_Directory_Here will instead be the <strong>ABSOLUTE PATH</strong> of where you want to save your folder at. (No quotation marks are needed).</div>
    <div>e.g.: DEST_PATH=C:\Documents\PythonProjects</div>
    </li>
    <li>You'll also need the 
    <strong>dotenv</strong> library installed in order to access your .env file. From the command line, also run: 
    <a href="https://pypi.org/project/python-dotenv/">pip install python-dotenv</a>
    </li>
    <li>With the command line at the root directory of 'pygen', run the command: python pygen your-folder-name It will then save a new directory at the specified path from the DEST_PATH variable with the name of "your-folder-name"</li>
</ol>
