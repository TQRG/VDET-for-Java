import * as _vscode from "vscode";

declare global {
    const vscode: {
        postMessage: ({type:string}) => void
    };
}