document.addEventListener("DOMContentLoaded", function() {
    const style = document.createElement('style');
    style.innerHTML = `
        /* Targets the file fields inside Django Admin dynamic rows */
        .inline-related tr.form-row td.field-image input[type="file"],
        .inline-related tr.form-row td.field-video input[type="file"],
        .inline-related .form-row input[type="file"] {
            padding: 20px !important;
            background: #1a1a1a !important;
            border: 2px dashed #FFD700 !important;
            color: #FFD700 !important;
            border-radius: 8px !important;
            cursor: pointer !important;
            display: inline-block !important;
            width: 90% !important;
            margin: 8px 0 !important;
        }
        
        /* Styles the browser click button to match your premium theme */
        .inline-related input[type="file"]::-webkit-file-upload-button {
            background: #FFD700 !important;
            color: #000 !important;
            font-weight: bold !important;
            border: none !important;
            padding: 6px 12px !important;
            border-radius: 4px !important;
            cursor: pointer !important;
        }
    `;
    document.head.appendChild(style);
});