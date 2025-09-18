const urlParams = new URLSearchParams(window.location.search);
const file = decodeURIComponent(urlParams.get('file'));
const originalUrl = decodeURIComponent(urlParams.get('url'));
const createdOn = decodeURIComponent(urlParams.get('created'));
const title = decodeURIComponent(urlParams.get('title'));

document.querySelector('.viewer-header h1').textContent = title;
document.getElementById('creation-date').textContent = `Saved on: ${createdOn}`;
document.getElementById('original-link').href = originalUrl;

if (file) {
    fetch(file)
        .then(response => response.text())
        .then(text => {
            // Find the end of the metadata to remove it safely
            const lines = text.split('\n');
            let contentStartIndex = 0;
            for (let i = 0; i < lines.length; i++) {
                if (lines[i].startsWith('created on:')) {
                    contentStartIndex = i + 1;
                    break;
                }
            }
            // Skip any blank lines after the metadata
            while (contentStartIndex < lines.length && lines[contentStartIndex].trim() === '') {
                contentStartIndex++;
            }
            const cleanedText = lines.slice(contentStartIndex).join('\n');

            const converter = new showdown.Converter({ tables: true });
            const html = converter.makeHtml(cleanedText);
            const contentDiv = document.getElementById('markdown-content');
            contentDiv.innerHTML = html;

            // Generate Table of Contents
            const toc = document.getElementById('toc');
            const headings = contentDiv.querySelectorAll('h1, h2, h3');
            const tocList = document.createElement('ul');

            headings.forEach((heading, index) => {
                const id = `heading-${index}`;
                heading.id = id;

                const listItem = document.createElement('li');
                listItem.className = `toc-${heading.tagName.toLowerCase()}`;

                const link = document.createElement('a');
                link.href = `#${id}`;
                link.textContent = heading.textContent;

                listItem.appendChild(link);
                tocList.appendChild(listItem);
            });

            if (headings.length > 0) {
                toc.appendChild(tocList);
            }

            // Apply syntax highlighting and add copy buttons
            document.querySelectorAll('pre code').forEach((block) => {
                hljs.highlightElement(block);

                const pre = block.parentNode;
                pre.style.position = 'relative';

                const copyButton = document.createElement('button');
                copyButton.className = 'copy-button';
                copyButton.textContent = 'Copy';
                pre.appendChild(copyButton);

                copyButton.addEventListener('click', () => {
                    navigator.clipboard.writeText(block.textContent).then(() => {
                        copyButton.textContent = 'Copied!';
                        setTimeout(() => {
                            copyButton.textContent = 'Copy';
                        }, 2000);
                    });
                });
            });
        });
}