# VDET-for-Java
Automatic vulnerability detection is of paramount importance to promote the security of an application and should be exercised at the earliest stages within the software development life cycle (SDLC) to reduce the risk of exposure. Despite the advancements with state-of-the-art deep learning techniques in software vulnerability detection, the development environments are not yet leveraging their performance. In this work, we integrate the Transformers architecture, one of the main highlights of advances in deep learning for Natural Language Processing, within a developer-friendly tool for code security. We introduce VDet for Java, a transformer-based VS Code extension that enables one to discover vulnerabilities in Java files. Our preliminary model evaluation presents an accuracy of 85.8% for multi-label classification and can detect up to 21 vulnerability types. The demonstration of our tool can be found at [YouTube](https://youtu.be/OjiUBQ6TdqE).



# Setup 
## 1. Start plugin-backend
To run plugin-backend server (from dir: `plugin-backend/`):

1. Install required packages (listed at requirements.txt):
    ```
    pip install -r requirements.txt
    ```
2. Make sure you have an "assets" folder, with the serialized pretrained model and multi-label binarizer (please, contact us to get ours).
3. Start the server (runs on port 5000):
    ```
    python server.py 
    ```
4. Check server routes: 
    * [POST] `/predict/section` : 
        * input:
        ```
        [
            1: {
                lines: 
                    [
                        <startline: int>,
                        <endline: int>
                    ],
                code: <code: string>
            }
        ]

        ```
        * output:
        ```
            [
                1: {
                    lines: 
                        [
                            <startline: int>,
                            <endline: int>
                        ],
                    predictions: 
                        [
                            (<label: string>, <probability: float>), 
                            (...)
                        ]
                }
            ]
        ```


    * [POST] `/predict/file` : 
        * input:
        ```
        [
            1: {
                name: <method_name: string>,  
                code: <code: string>
            },
            (...)
        ]

        ```
        * output:
        ```
            [
                1: {
                    name: <method_name: string>
                    predictions: 
                        [
                            (<label: string>, <probability: float>), 
                            (...)
                        ]
                },
                (...)
            ]
        ```

## 2. Start VS Code extension
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
4. Start the extension by pressing F5. A new VS Code window should open.

**Note:** if you have any trouble starting the extension, please check ["VS Code: Your First Extension"](https://code.visualstudio.com/api/get-started/your-first-extension) tutorial.
