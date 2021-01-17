<h1>PYGEN</h1>
<h2>Command-line python project generator</h2>

<strong>NOTE: these instructions presume prior knowledge of basic command line instructions and (obviously) Python already being installed.</strong>

<p>Pygen creates a simple file structure for new Python projects at a directory of your choice!
To get started, follow these steps (this assumes prior knowledge of basic command line functions):</p>
<ol>
    <li>Clone this repo and change directory into the root 'pygen' folder. So the command line should be something like this:<pre><code>/your/path/pygen</code></pre></li>
    <li>In that same level as the root project folder, create a new .env file. When created, add the following line inside the file: <pre><code>DEST_PATH=Your_Directory_Here</code></pre>
    <div>Your_Directory_Here will instead be the <strong>ABSOLUTE PATH</strong> of where you want to save your folder at. (No quotation marks are needed).</div>
    <div>e.g.: DEST_PATH=C:\Documents\PythonProjects</div>
    </li>
    <li>In the command line again, run the package installer with the line:<pre><code>pip install -r requirements.txt</code></pre>This will install any necessary python libraries (in this case, only the <strong>python-dotenv</strong> library is required. This library is needed to pull the info from the .env file!</li>
    <li>Now, with the command line at the root directory of 'pygen', run the command: <pre><code>python pygen your-folder-name</code></pre> It will then save a new directory at the specified path from the DEST_PATH variable with the name of "your-folder-name"</li>
    <li>After being run, the program will output a path (after the line saying "You can peep the file here). Navigate to the new folder to find a new project waiting for you! :D</li>
</ol>
