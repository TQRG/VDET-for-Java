import * as vscode from 'vscode';

import { SidebarProvider } from './SidebarProvider';


export function activate(context: vscode.ExtensionContext) {
	const sidebarProvider = new SidebarProvider(context.extensionUri);

	context.subscriptions.push(
		vscode.window.registerWebviewViewProvider(
			"vdet-sidebar", // match package.json
			sidebarProvider
		)
	);

	context.subscriptions.push(
		vscode.commands.registerCommand('vdet-java.helloWorld', () => {
			vscode.window.showInformationMessage('Hello from vdet-java!');
		})
	);

	context.subscriptions.push(
		vscode.commands.registerCommand('vdet-java.active-file-prediction', async () => {
			// TODO: open sidebar with specific keyboard keys
		})
	);

}

export function deactivate() { }
