document.addEventListener("DOMContentLoaded", function() {
    // Inject custom styles directly into the head of the page
    const style = document.createElement('style');
    style.innerHTML = `
        /* Transform default file inputs into premium drop rows */
        .inline-related input[type="file"] {
            padding: 15px !important;
            background: #242424 !important;
            border: 2px dashed #FFD700 !important;
            color: #fff !important;
            border-radius: 8px !important;
            width: 100% !important;
            box-sizing: border-box !important;
            margin: 5px 0 !important;
            cursor: pointer !important;
        }
        /* Style the choose file text inside the browser container */
        .inline-related input[type="file"]::-webkit-file-upload-button {
            background: #FFD700 !important;
            border: none !important;
            padding: 8px 16px !important;
            border-radius: 4px !important;
            color: #000 !important;
            font-weight: bold !important;
            margin-right: 10px !important;
            cursor: pointer !important;
        }
    `;
    document.head.appendChild(style);
});