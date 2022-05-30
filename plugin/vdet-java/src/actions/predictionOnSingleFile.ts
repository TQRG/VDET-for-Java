import fetch from "node-fetch";

export async function predictionOnSection(requestBody: { lines: number[]; code: string; }) {
    const response = await fetch(
        'http://127.0.0.1:5000/predict/section',
        {
            method: 'POST',
            body: JSON.stringify(requestBody),
            headers: { 'Content-Type': 'application/json' }
        }
    );

    const predictions = await response.json();
    return predictions;
}

export async function predictionOnSingleFile(requestBody: { lines: number[]; code: string; }[]) {
    const response = await fetch(
        'http://127.0.0.1:5000/predict/file',
        {
            method: 'POST',
            body: JSON.stringify(requestBody),
            headers: { 'Content-Type': 'application/json' }
        }
    );

    const predictions = await response.json();
    return predictions;
}