async function loadReadingList() {
    try {
        const response = await fetch('article_data.json');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const articles = await response.json();
        const readingListContainer = document.getElementById('reading-list');
        readingListContainer.innerHTML = ''; // Clear existing content

        articles.forEach(item => {
            const href = `viewer.html?file=${encodeURIComponent(item.markdown_file)}&title=${encodeURIComponent(item.title)}&url=${encodeURIComponent(item.url)}&created=${encodeURIComponent(item.created_on)}`;

            const cardLink = document.createElement('a');
            cardLink.href = href;
            cardLink.className = 'card-link';
            cardLink.target = '_blank';

            const card = document.createElement('div');
            card.className = 'card';

            const categoryElement = document.createElement('span');
            categoryElement.className = `card-category card-category-${item.category.toLowerCase()}`;
            categoryElement.textContent = item.category;

            const titleElement = document.createElement('h3');
            titleElement.textContent = item.title;

            const summaryElement = document.createElement('p');
            summaryElement.className = 'card-summary';
            summaryElement.textContent = item.summary;

            const tagsContainer = document.createElement('div');
            tagsContainer.className = 'card-tags';
            item.tags.forEach(tag => {
                const tagElement = document.createElement('span');
                tagElement.className = 'card-tag';
                tagElement.textContent = tag;
                tagsContainer.appendChild(tagElement);
            });

            card.appendChild(categoryElement);
            card.appendChild(titleElement);
            card.appendChild(summaryElement);
            card.appendChild(tagsContainer);
            cardLink.appendChild(card);
            readingListContainer.appendChild(cardLink);
        });

    } catch (error) {
        console.error("Could not load or parse article_data.json:", error);
        const readingListContainer = document.getElementById('reading-list');
        readingListContainer.innerHTML = '<p style="color: red;">Error: Could not load article data. Please run the processing script.</p>';
    }
}

// No need for PapaParse anymore, just load the list directly.
loadReadingList();
