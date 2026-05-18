document.addEventListener("DOMContentLoaded", function() {
    // Find all file input rows inside your image and video inlines
    const fileInputs = document.querySelectorAll('.inline-related input[type="file"]');
    
    fileInputs.forEach(input => {
        const row = input.closest('tr') || input.closest('.form-row');
        if (!row) return;

        // Create a custom drag zone wrapper
        const dragZone = document.createElement('div');
        dragZone.className = 'custom-drag-zone';
        dragZone.innerHTML = '<p>✨ Drag & Drop file here or <span>Browse</span></p>';
        
        // Hide the ugly default input button style but keep it active
        input.style.opacity = '0';
        input.style.position = 'absolute';
        input.style.width = '100%';
        input.style.height = '100%';
        input.style.top = '0';
        input.style.left = '0';
        input.style.cursor = 'pointer';

        // Style the container dynamically
        dragZone.style.position = 'relative';
        dragZone.style.border = '2px dashed #FFD700'; /* Match your yellow accent brand color */
        dragZone.style.padding = '20px';
        dragZone.style.background = '#f9f9f9';
        dragZone.style.borderRadius = '8px';
        dragZone.style.textAlign = 'center';
        dragZone.style.marginTop = '5px';

        // Append the elements together
        input.parentNode.insertBefore(dragZone, input);
        dragZone.appendChild(input);

        // Visual effects when hovering a file over the box
        input.addEventListener('dragenter', () => dragZone.style.background = '#fff9d6');
        input.addEventListener('dragleave', () => dragZone.style.background = '#f9f9f9');
        input.addEventListener('drop', () => dragZone.style.background = '#f9f9f9');
    });
});