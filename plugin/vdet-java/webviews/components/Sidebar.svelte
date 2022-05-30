<script lang="ts">
    var time:string|null = null;
    var data:any = null;
    var filename:string|null = null;
    var error:boolean = false;
    var isLoading = false;
    var warning = false;

    window.addEventListener('message', event => {
    isLoading = false;
    warning = false;

    const message = event.data; // The JSON data our extension sent

    switch (message.command) {
        case 'codeSelectionPrediction':
            {
                filename = message.filename;
                data = message.predictions;
                time = message.time;
            }
            break;
            case 'completeFilePrediction':
            {
                filename = message.filename;
                data = message.predictions;
                time = message.time;
            }
            break;
            case 'onError':
            {
                error = true;
                data = message.error;
            }
            break;
    }
    });
</script>

<style>
    #sb-div {
        padding: 4%;
    }

    #sb-main-div {
        display: flex;
        align-items: center;
        margin-bottom: 10%;
    }

    #sb-head-div {
        margin-bottom: 5%;
    }

    #sb-info-div {
        margin-bottom: 3%;
    }

    #sb-info-p {
        font-size: small;
        font-weight: lighter;
        line-height: 1.6;
    }

    #sb-results-error-div {
        background-color: #444;
        border: 1px solid rgb(45, 45, 45);
        display: flex;
        padding: 5%;
    }

    #sb-info-warnign-div{
        background-color: #444;
        border: 1px solid rgb(45, 45, 45);
        padding: 2%;
    }

    #sb-btn {
        font-weight: bold;
        border-radius: 2px;
        margin: 2%;
    }

    #sb-btn-warning {
        font-weight: bold;
        border-radius: 2px;
        margin: 2%;
        color: var(--vscode-button-secondaryForeground);
        background: rgb(220, 136, 9);        
    }

    #sb-btn-warning:hover {
        color: var(--vscode-button-secondaryForeground);
        background: rgb(176, 85, 10);
    }

    #sb-btn:hover {
        color: var(--vscode-button-secondaryForeground);
        background: #043f6f;
    }

    .tooltip {
        position: relative;
    }

    .tooltip::before {
        background-color: rgb(206, 200, 200);
        border: 1px solid rgb(102, 99, 99);
        border-radius: 5px;
        color: #444;
        content: attr(data-title);
        display: none;
        font-size: smaller;
        font-weight: lighter;
        font-style: italic;
        padding: 4%;
        position: absolute;
        right:2px;
        left: 2px;
        top: 90%;
        z-index: 1;
    }

    .tooltip:hover{
        transition-duration: 0.4s;
    }

    .tooltip:hover::before {
        display: block;
    }

    #sb-results-p {
        font-size: small;
        font-style: italic;
    }

    #sb-results-p-filename{
        font-size: small;
        font-style: italic;
        font-weight: bold;
        word-break: break-all;
        color: white;
    }

    #sb-results-div {
        background-color: #444;
        border: 1px solid rgb(45, 45, 45);
        padding: 5%;
    }

    #sb-results-error-p {
        margin: 2%;
    }

    hr {
        border: none;
        height: 1px;
        color: rgb(45, 45, 45); 
        background-color: rgb(45, 45, 45);
    }

    #sb-results-p-linenr {
        color: rgb(28, 155, 0);
        font-weight: bolder;
    }

    #info-loading {
        font-size: large;
    }

    #info-warning {
        font-weight: bold;
        font-size: small;
        text-transform: uppercase;
        color:rgb(220, 136, 9);
        margin: 5%;
        text-align: center;
    }

    @keyframes dots {
    from {color: rgb(0, 117, 185); transform: translate(0, -10%);}
    to {color: white; transform: translate(0, 0);}
    }

    .dot {
    display: inline-block;
    font-size: 250%;
    }

    .dot:nth-child(1) {
    animation: dots .5s infinite alternate linear;
    }

    .dot:nth-child(2) {
    animation: dots 1s infinite alternate linear;
    }

    .dot:nth-child(3) {
    animation: dots 1.5s infinite alternate linear;
    }

    .progress {
        padding:0;
        width:90%;
        height:15px;
        overflow:hidden;
        background:#e5e5e5;
        border-radius:6px;
    }

    .bar {
        position:relative;
        float:left;
        min-width:1%;
        height:100%;
        background:cornflowerblue;
    }

    .percent {
        position:absolute;
        top:50%;
        left:50%;
        transform:translate(-50%,-50%);
        margin:0;
        font-size: x-small;
        color:white;
        font-style: italic;
    }

    #sb-results-p-labels {
        margin: 3% 0% 1% 0%;
        color: white;
        text-transform: uppercase;
        font-size: smaller;
        font-weight: bold;
    }

</style>


<div id="sb-div">
    <div id="sb-head-div">
        <img class="center" alt="VDet for Java logo" src="https://i.ibb.co/7KcSH1y/VDet-for-Java.png"/>
    </div>

    <div id="sb-info-div">
        <p id="sb-info-p">A transformer-based VSCode extension for vulnerability detection in Java source code. Using a novel deep learning architecture, this tool identifies vulnerable code and related CWEs in specific code selections or the entire Java file. <b>Click for predictions:</b> </p>
    </div>

    <div id="sb-main-div">
        <button 
            class="tooltip"
            data-title="Click to analyze the selected code from the active text editor."
            id="sb-btn"
            on:click={()=> { vscode.postMessage({ type : 'onCodeSelection' }); isLoading = true; time=null; }}>
            Code Selection
        </button>
        <button 
            class="tooltip"
            data-title="Click to analyze the complete code from the active text editor."
            id="sb-btn"
            on:click={()=> { vscode.postMessage({ type: 'onCompleteFile' }); isLoading = true; time=null;}}> 
            Complete File
        </button> 
        <!-- <button 
            class="tooltip"
            data-title="Click to analyze all files form the project."
            id="sb-btn-warning"
            on:click={()=> { vscode.postMessage({ type: 'allFiles' }); isLoading = true; warning = true; time=null;}}> 
            All project
        </button> -->
    </div>

    {#if isLoading}
        <p id="info-loading">Loading <span class="dot">.</span><span class="dot">.</span><span class="dot">.</span></p>
        {#if warning}
            <div id="sb-info-warnign-div">
                <p id="info-warning">⚠️ This action may take some time! </p>
            </div>
        {/if}
    {:else}
        {#if data}
            {#if error}
            <!-- Display error messages -->
                <div id="sb-results-error-div">
                    <h1 id="sb-results-error-p">⚠️ </h1>
                    <p id="sb-results-error-p">{data}</p>
                </div>
            {:else}
            <!-- Display results -->
            <div id="sb-results-div">
                <p id="sb-results-p">Analyzing </p> 
                <p id="sb-results-p-filename"> {filename}</p>

                <hr>
                <div>
                    {#each data as section}
                    <!-- Display code section/lines -->
                    <p id="sb-results-p-linenr">{section.range}: </p>
                        {#each section.labels as label}
                                {#if label[0] == "True"}
                                    <p id="sb-results-p-labels">⚠️ Vulnerable</p>
                                    <div class="progress">
                                        <div class="bar" style='width:{label[1]*100}%; background:red;'>
                                            <p class="percent">{Math.ceil(label[1]*100)}%</p>
                                        </div>
                                    </div>   
                                {:else if label[0] == "False"}
                                    <div></div>
                                {:else}
                                    <p id="sb-results-p-labels">CWE {label[0]}</p>
                                    <div class="progress">
                                        <div class="bar" style='width:{label[1]*100}%'>
                                            <p class="percent">{Math.ceil(label[1]*100)}%</p>
                                        </div>
                                    </div>
                                {/if}
                        {/each}

                    <hr style="margin:5%" >
                    {/each}
                </div>
            </div>
            {/if}
        {/if}
    {/if}

    {#if time}
    <div>
        <small>Executed in {time} ms.</small>
    </div>
    {/if}

</div>