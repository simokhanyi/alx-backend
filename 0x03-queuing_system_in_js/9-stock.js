const express = require('express');
const redis = require('redis');
const { promisify } = require('util');
const { listProducts, getItemById } = require('./data');

const app = express();
const port = 1245;
const client = redis.createClient();

client.on('connect', () => {
  console.log('Connected to Redis');
});

// Function to reserve stock by itemId
const reserveStockById = (itemId, stock) => {
  client.set(`item.${itemId}`, stock);
};

// Async function to get current reserved stock by itemId
const getCurrentReservedStockById = async (itemId) => {
  const getAsync = promisify(client.get).bind(client);
  const reservedStock = await getAsync(`item.${itemId}`);
  return reservedStock ? parseInt(reservedStock) : 0;
};

// Route to list all products
app.get('/list_products', (req, res) => {
  const formattedProducts = listProducts.map(product => ({
    itemId: product.itemId,
    itemName: product.itemName,
    price: product.price,
    initialAvailableQuantity: product.stock
  }));
  res.json(formattedProducts);
});

// Route to get product details by itemId
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  const currentQuantity = await getCurrentReservedStockById(itemId);
  const productDetails = {
    itemId: product.itemId,
    itemName: product.itemName,
    price: product.price,
    initialAvailableQuantity: product.stock,
    currentQuantity: currentQuantity
  };

  res.json(productDetails);
});

// Route to reserve product by itemId
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);

  if (!product) {
    return res.json({ status: 'Product not found' });
  }

  const currentQuantity = await getCurrentReservedStockById(itemId);

  if (currentQuantity >= product.stock) {
    return res.json({ status: 'Not enough stock available', itemId: itemId });
  }

  reserveStockById(itemId, currentQuantity + 1);
  res.json({ status: 'Reservation confirmed', itemId: itemId });
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
