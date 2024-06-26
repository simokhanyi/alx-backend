// Array of products
const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, stock: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, stock: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, stock: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, stock: 5 }
];

// Function to get product by itemId
function getItemById(id) {
  return listProducts.find(product => product.itemId === id);
}

module.exports = { listProducts, getItemById };
