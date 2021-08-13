# Text Mining as Historical Method
HIST 3368 (undergrad) / Hist 6322 (Grad)

Meets 3:00-3:50PM CT MWF                                            

Meetings in Spring 2020 will be partly synchronous (via Zoom), partly asynchronous (via Canvas discussion boards, etc.). 

### About the Course
Computer-powered methods are changing the way that we access information about society. New methods help us to detect change over time, to identify influential figures, and to name turning points. What happens when we apply these tools to a million congressional debates or tweets? This course -- which is appropriate to both computationalists as well as those with a background in the humanities (but not code) -- will teach students how to analyze texts and as data for evidence of change over time. This course is an introduction to the cutting-edge methodologies of textual analysis that are transforming the humanities today.

### About the GitHub Repository
The purpose of this repository is to provide resources for digital-history. It aggregates original Notebooks written by Jo Guldi or her research assistant, Steph Buongiorno, Notebooks written by Southern Methodist University's "Data Team" (Rob Kalescky and Eric Godat), and Notebooks written by scholars in the digital humanities. Authorial credit for copied/forked Notebooks is given in associated README.md files located in the Notebook's parent directory. All code copied/forked from others' repositories are subject to the author's original licensing, not the licensing of the present repository.

#### Initial Clone 
`git clone https://github.com/stephbuon/digital-history.git --recursive`

#### Subsequent Updates
From inside `digital-history` directory:
```
git reset --hard
git pull
git submodule update --recursive 
```
#### Setting Up our M2 Environment for the First Time

After cloning the repository, configure your M2 environment so the digital-history directory can be viewed. Go to __File -> Open from path...__

![placeholdertext](https://github.com/stephbuon/digital-history/blob/master/images/file_open.png)

Then enter the path to the cloned repository:

![placeholdertext](https://github.com/stephbuon/digital-history/blob/master/images/open_filep.png)

### About the Instructor: Professor Jo Guldi, PhD
When I was a PhD student living in Silicon Valley, something amazing happened: Google Books launched the first mass digitization experiment of its kind, releasing scans of the Harvard, Yale, and New York Public Libraries onto the web. I quickly saw that there was potential, in this textual data, for kinds of analysis that had never been attempted before. From that point forward, I helped to found the discipline of "digital history," and I have been applying myself to the study of how computational algorithms can help us learn new things about the past, the present, and ourselves.

I am also a historian of technology who is interested in questions about how we know what is true – whether new technologies or history give us the tools for discerning historical truth in a new way – and when official paper obscures more than it illuminates. My book on the importance of history as a tool for discovering truth, The History Manifesto, was recently named one of the most important books across all fields published in the last twenty years. 

# How to Access Jupyter Lab on M2

1. Go to [hpc.smu.edu](https://www.smu.edu/OIT/Services/HPC)

2. Sign in using your SMU ID and SMU password

3. In the "Dashboard" tab select "JupyterLab" from the "Interactive Apps" drop-down menu.

![placeholdertext](https://github.com/stephbuon/digital-history/blob/master/images/select_jupyter.png?raw=true)

4. Fill in the fields that are required for your Jupyter Lab instance. If custom fields are required, they will be specified in the README file in that week's folder.

![placeholdertext](https://github.com/stephbuon/digital-history/blob/master/images/fields.png?raw=true)

5. Select other options required for your Jupyter instance. For this tutorial:

- Partition: htc
- Number of hours: 3
- Number of nodes: 1
- Cores per node: 1
- GPUs per node: 0
- Memory: 6

![placeholdertext](https://github.com/stephbuon/digital-history/blob/master/images/resources_1.png?raw=true)

6. Select "Launch"

Wait for the job to start on M2. When the job starts a new button "Connect to JupyterLab" button will appear.

7. Select "Connect to JupyterLab"

![placeholdertext](https://github.com/stephbuon/digital-history/blob/master/images/connect_jupyter_1.png?raw=true)

8. The JupyterLab graphical interface will be presented and running on the M2 resource requested. Double click the appropriate notebook to open it.

![placeholdertext](https://github.com/stephbuon/digital-history/blob/master/images/double_click.png?raw=true)

9. When finished using the JupyterLab instance, return to the "My Interactive Sessions" tab in your browser and select "Delete" and "Confirm", when prompted, to cancel the job on M2.
