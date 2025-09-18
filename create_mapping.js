const fs = require('fs');
const path = require('path');
const csv = require('csv-parser');

const csvFilePath = 'Reading List 23fae7025b0f44f4bfa3c0789a2bd8fe.csv';
const mdFilesDirectory = 'Reading List 23fae7025b0f44f4bfa3c0789a2bd8fe';

const articles = [];
const mdFiles = [];

fs.createReadStream(csvFilePath)
  .pipe(csv())
  .on('data', (row) => {
    articles.push(row);
  })
  .on('end', () => {
    fs.readdirSync(mdFilesDirectory).forEach(file => {
        if (path.extname(file) === '.md') {
            mdFiles.push(file);
        }
    });

    const mapping = {};
    articles.forEach(article => {
        const articleName = article.Name.replace(/[^\w\s]/gi, '').substring(0, 20);
        const matchedFile = mdFiles.find(file => file.toLowerCase().includes(articleName.toLowerCase()));
        if (matchedFile) {
            mapping[article.Name] = path.join(mdFilesDirectory, matchedFile);
        }
    });

    fs.writeFileSync('file_mapping.json', JSON.stringify(mapping, null, 2));
    console.log('File mapping created successfully!');
  });
