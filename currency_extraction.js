// Define the regex pattern for currency amounts
const currencyPattern = /\$\d{1,3}(,\d{3})*(\.\d{2})?/g;

// Sample data for currency amounts
const testCurrencyData = ['$5.00', '$999.99', '$12,345.67', '$100', '$1,234', '$45.5'];

// Function to match the regex pattern
function matchCurrency(text) {
    return text.match(currencyPattern);
}

// Test the pattern on the test data
testCurrencyData.forEach(data => {
    const matches = matchCurrency(data);
    console.log(`Input: ${data}, Matches: ${matches}`);
});
