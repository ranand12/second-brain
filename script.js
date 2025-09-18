let allArticles = []; // Store all articles globally
const readingListContainer = document.getElementById('reading-list');
const filterBar = document.getElementById('filter-bar');
const activeFilterSpan = document.getElementById('active-filter');
const clearFilterBtn = document.getElementById('clear-filter-btn');


async function loadReadingList() {
    try {
        const response = await fetch('article_data.json');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        allArticles = await response.json();
        displayArticles(allArticles);

    } catch (error) {
        console.error("Could not load or parse article_data.json:", error);
        readingListContainer.innerHTML = '<p style="color: red;">Error: Could not load article data. Please run the processing script.</p>';
    }
}

function displayArticles(articles) {
    readingListContainer.innerHTML = ''; // Clear existing content

    articles.forEach(item => {
        const params = new URLSearchParams({
            file: item.markdown_file,
            title: item.title,
            url: item.url,
            created: item.created_on,
            summary: item.summary,
            category: item.category,
            tags: JSON.stringify(item.tags)
        });
        const href = `viewer.html?${params.toString()}`;

        const cardLink = document.createElement('a');
        cardLink.href = href;
        cardLink.className = 'card-link';

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
            const tagElement = document.createElement('button'); // Change to button for clickability
            tagElement.className = 'card-tag';
            tagElement.textContent = tag;
            tagElement.onclick = (e) => {
                e.preventDefault(); // Prevent link navigation
                e.stopPropagation(); // Stop event from bubbling to the card link
                filterByTag(tag);
            };
            tagsContainer.appendChild(tagElement);
        });

        card.appendChild(categoryElement);
        card.appendChild(titleElement);
        card.appendChild(summaryElement);
        card.appendChild(tagsContainer);
        cardLink.appendChild(card);
        readingListContainer.appendChild(cardLink);
    });
}

function filterByTag(tag) {
    const filteredArticles = allArticles.filter(item => item.tags.includes(tag));
    displayArticles(filteredArticles);
    
    // Show filter bar
    activeFilterSpan.textContent = tag;
    filterBar.classList.remove('filter-bar-hidden');
}

function clearFilter() {
    displayArticles(allArticles);
    filterBar.classList.add('filter-bar-hidden');
}

// Event Listeners
clearFilterBtn.addEventListener('click', clearFilter);

// Initial Load
loadReadingList();