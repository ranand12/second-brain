async function loadReadingList() {
    const mappingResponse = await fetch('file_mapping.json');
    const fileMapping = await mappingResponse.json();

    const response = await fetch('Reading List 23fae7025b0f44f4bfa3c0789a2bd8fe.csv');
    const csvData = await response.text();

    const parsedData = Papa.parse(csvData, {
        header: true,
        skipEmptyLines: true
    });

    const readingListContainer = document.getElementById('reading-list');

    parsedData.data.forEach(item => {
        const markdownFile = fileMapping[item.Name];
        let href = item.Column; // Fallback to original URL

        if (markdownFile) {
            const url = item.Column || '#';
            const createdOn = item['created on'] || '';
            const title = item.Name || 'Article';
            href = `viewer.html?file=${encodeURIComponent(markdownFile)}&url=${encodeURIComponent(url)}&created=${encodeURIComponent(createdOn)}&title=${encodeURIComponent(title)}`;
        }

        const cardLink = document.createElement('a');
        cardLink.href = href;
        cardLink.className = 'card-link';
        cardLink.target = '_blank';

        const card = document.createElement('div');
        card.className = 'card';

        const titleElement = document.createElement('h3');
        titleElement.textContent = item.Name;

        const descriptionElement = document.createElement('p');
        descriptionElement.textContent = item.Column; // Using URL as description

        card.appendChild(titleElement);
        card.appendChild(descriptionElement);
        cardLink.appendChild(card);
        readingListContainer.appendChild(cardLink);
    });
}

// Load the Papa Parse library and then load the reading list
const script = document.createElement('script');
script.src = 'https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.3.2/papaparse.min.js';
script.onload = () => {
    loadReadingList();
};
document.head.appendChild(script);