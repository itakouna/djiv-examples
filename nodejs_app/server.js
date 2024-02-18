// Import required modules
const http = require('http');
fs = require('fs');
fs.readFile('./index.html', function (err, html) {
    if (err) {
        throw err; 
    }       
    server = http.createServer(function(request, response) {  
        response.writeHeader(200, {"Content-Type": "text/html"});  
        response.write(html);  
        response.end();  
    });
    const PORT = process.env.PORT || 3000;
    server.listen(PORT, () => {
        console.log(`Server running on port ${PORT}`);
    });
});
