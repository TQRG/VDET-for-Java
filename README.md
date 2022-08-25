# VDET for Java

![VDET in action](https://s4.gifyu.com/images/ezgif-3-2c63f0a5ea.gif)

> Automatic vulnerability detection is of paramount importance to promote the security of an application and should be exercised at the earliest stages within the software development life cycle (SDLC) to reduce the risk of exposure. Despite the advancements with state-of-the-art deep learning techniques in software vulnerability detection, the development environments are not yet leveraging their performance. In this work, we integrate the Transformers architecture, one of the main highlights of advances in deep learning for Natural Language Processing, within a developer-friendly tool for code security. We introduce VDet for Java, a transformer-based VS Code extension that enables one to discover vulnerabilities in Java files. Our preliminary model evaluation presents an accuracy of 98.9\% for multi-label classification and can detect up to 21 vulnerability types. 

**Check our [Youtube 📺](https://youtu.be/OjiUBQ6TdqE) video to see how VDET works.** 



## Features
- Scan a complete file (recommended)
- Scan a specific code piece highlighted by the user (useful when there are syntax errors)


**List of CWEs**: 113, 129, 134, 15, 190, 191, 197, 23, 319, 26, 269, 400, 470, 606, 643, 690, 78, 789, 80, 89, 90


## Setup

Tested with ![Windows](https://svgshare.com/i/ZhY.svg) ![VSCode version](https://badgen.net/badge/VSCode/v1.70/blue) ![Python version](https://badgen.net/badge/Python/v3.10.2/blue) ![NodeJS version](https://badgen.net/badge/NodeJS/v16.15.0/blue) ![Git version](https://badgen.net/badge/Git/v2.35.1.windows.2/blue) 

### 1. Start plugin-backend
To run plugin-backend server (from dir: `plugin-backend/`):

1. Install required packages (listed at requirements.txt):
    ```
    pip install -r requirements.txt
    ```
2. Make sure you have a serialized pretrained model and multi-label binarizer (ours are available [here](https://drive.google.com/drive/folders/1QXzoY0lfNUZwgot2Px_VZCHr6QyhJjFj?usp=sharing)). Then, create your ```.env``` file (from the provided template, in the same location) and add the paths to the serialized objects.

3. Start the server (it runs on port 5000 by default):
    ```
    python server.py 
    ```
    
Check the available routes (they can be used without the extension):
**1. Analyse code section (with line interval):**
    ```  POST /predict/section ```

**2. Analyse complete file:**
    ```  POST /predict/file ```

### 2. Start VS Code extension
To run the extension (from dir: `plugin/vdet-java/`)

1. Make sure you have Node.js and Git installed
2. Install yo and generator-code
    ```
    npm install -g yo generator-code
    ```
3. Install required packages
    ```
    npm install
    ```
4. Start the extension by pressing F5. A new VS Code window should open ✨

**Note:** if you have any trouble starting the extension, please check ["VS Code: Your First Extension"](https://code.visualstudio.com/api/get-started/your-first-extension) tutorial.

___
<br>

*More info about this work [here](https://repositorio-aberto.up.pt/handle/10216/142743)*.